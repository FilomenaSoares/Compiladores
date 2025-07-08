from antlr4 import *
from src.fimlyVisitor import fimlyVisitor
from src.fimlyParser import fimlyParser
from src.tac import TACOperand, TACInstruction, GeradorDeCodigoIntermediario

class CodeGenError(Exception):
    pass

class TACGenerator(fimlyVisitor, GeradorDeCodigoIntermediario):
    def __init__(self):
        super().__init__()
        GeradorDeCodigoIntermediario.__init__(self)

    def visitExpressao(self, ctx:fimlyParser.ExpressaoContext):
        return self.visit(ctx.expressao_logica())

    # O método 'visitExpressao' é o ponto de entrada para qualquer expressão.
    # Garante que sempre retornamos o resultado.
    def visitExpressao_logica(self, ctx: fimlyParser.Expressao_logicaContext):
        left = self.visit(ctx.expressao_comparacao(0))
        
        # Se houver operadores lógicos (&&, ||)...
        if len(ctx.expressao_comparacao()) > 1:
            for i in range(1, len(ctx.expressao_comparacao())):
                # Obtenha o operador ('&&' ou '||')
                op = ctx.getChild(2 * i - 1).getText()
                
                # Obtenha o resultado da expressão da direita
                right = self.visit(ctx.expressao_comparacao(i))
                
                # Crie uma nova variável temporária para armazenar o resultado
                temp = self.new_temp()
                
                # Adicione a instrução TAC simples (ex: _t1 = left && right)
                self.instructions.append(TACInstruction(op, temp, left, right))
                
                # O resultado desta operação se torna o operando 'left' para a próxima iteração
                # Isso permite encadear operações como: a && b || c
                left = temp
                
        return left   
                
    def visitExpressao_comparacao(self, ctx:fimlyParser.Expressao_comparacaoContext):
        left = self.visit(ctx.expressao_aritmetica(0))
        if len(ctx.expressao_aritmetica()) > 1:
            right = self.visit(ctx.expressao_aritmetica(1))
            op = ctx.getChild(1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            return temp # Retorna a variável temporária com o resultado
        return left # Retorna o valor direto se não houver comparação

    def visitExpressao_aritmetica(self, ctx: fimlyParser.Expressao_aritmeticaContext):
        left = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            right = self.visit(ctx.termo(i))
            op = ctx.getChild(2 * i - 1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            left = temp
        return left

    def visitTermo(self, ctx: fimlyParser.TermoContext):
        left = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            right = self.visit(ctx.fator(i))
            op = ctx.getChild(2 * i - 1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            left = temp
        return left

    def visitFator(self, ctx: fimlyParser.FatorContext):
        if ctx.ID(): # Se for um Identificador
            return TACOperand(ctx.ID().getText())
        if ctx.INTEIRO():  # Se for um número Inteiro literal
            return TACOperand(ctx.INTEIRO().getText())
        
        if ctx.FLOAT(): # Se for um número Float literal
            return TACOperand(ctx.FLOAT().getText())

        if ctx.STRING():  #Se for uma String literal
            return TACOperand(ctx.STRING().getText())
        if ctx.expressao(): # Se for uma expressão entre parênteses
            return self.visit(ctx.expressao())
            
        # Se não for nenhum dos acima, lança um erro
        raise CodeGenError(f"Fator não reconhecido na geração de TAC: '{ctx.getText()}'")

    def visitComando_atribuicao(self, ctx: fimlyParser.Comando_atribuicaoContext):
        dest = TACOperand(ctx.ID().getText())
        expr_result = self.visit(ctx.expressao())
        self.instructions.append(TACInstruction('ASSIGN', dest, expr_result))

    def visitComando_condicional(self, ctx: fimlyParser.Comando_condicionalContext):
        cond_result = self.visit(ctx.expressao())
        
        if ctx.SENAO(): # Estrutura if-else
            label_else = self.new_label()
            label_end = self.new_label()
            
            self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_else))
            self.visit(ctx.bloco_comandos(0))
            self.instructions.append(TACInstruction('GOTO', label_end))
            self.instructions.append(TACInstruction('LABEL', label_else))
            self.visit(ctx.bloco_comandos(1))
            self.instructions.append(TACInstruction('LABEL', label_end))
            
        else: # Estrutura if simples
            label_end = self.new_label()
            
            self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
            self.visit(ctx.bloco_comandos(0))
            self.instructions.append(TACInstruction('LABEL', label_end))

    def visitComando_repeticao(self, ctx: fimlyParser.Comando_repeticaoContext):
        label_start = self.new_label()
        label_end = self.new_label()
        
        self.instructions.append(TACInstruction('LABEL', label_start))
        cond_result = self.visit(ctx.expressao())
        self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
        self.visit(ctx.bloco_comandos())
        self.instructions.append(TACInstruction('GOTO', label_start))
        self.instructions.append(TACInstruction('LABEL', label_end))

    def visitComando_ler(self, ctx: fimlyParser.Comando_lerContext):
        var = TACOperand(ctx.ID().getText())
        self.instructions.append(TACInstruction("READ", var))

    def visitComando_escrever(self, ctx: fimlyParser.Comando_escreverContext):
        if ctx.lista_expressao():
            for expr in ctx.lista_expressao().expressao():
                val = self.visit(expr)
                self.instructions.append(TACInstruction("PRINT", val))

    def visitComando_declaracao(self, ctx: fimlyParser.Comando_declaracaoContext):
        var_name = TACOperand(ctx.ID().getText())
        var_type = ctx.tipo().getText()
        self.instructions.append(TACInstruction("DECL", var_name, TACOperand(var_type)))

    def visitBloco_comandos(self, ctx: fimlyParser.Bloco_comandosContext):
        return self.visitChildren(ctx)

    def visitFimly(self, ctx: fimlyParser.FimlyContext):
        return self.visitChildren(ctx)
# tac_generator.py (VERSÃO CORRIGIDA E AJUSTADA PARA SUA GRAMÁTICA)

from antlr4 import *
from src.fimlyVisitor import fimlyVisitor
from src.fimlyParser import fimlyParser
from src.tac import TACOperand, TACInstruction, GeradorDeCodigoIntermediario

class TACGenerator(fimlyVisitor, GeradorDeCodigoIntermediario):
    def __init__(self):
        fimlyVisitor.__init__(self)
        GeradorDeCodigoIntermediario.__init__(self)

    # --- Métodos para expressões (a maioria já estava correta) ---

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
    
    def visitExpressao_comparacao(self, ctx:fimlyParser.Expressao_comparacaoContext):
        left = self.visit(ctx.expressao_aritmetica(0))
        if len(ctx.expressao_aritmetica()) > 1:
            right = self.visit(ctx.expressao_aritmetica(1))
            op = ctx.getChild(1).getText() # Pega o operador de comparação
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            return temp
        return left

    def visitFator(self, ctx: fimlyParser.FatorContext):
        if ctx.ID():
            return TACOperand(ctx.ID().getText())
        if ctx.INTEIRO():
            return TACOperand(ctx.INTEIRO().getText())
        if ctx.FLOAT():
            return TACOperand(ctx.FLOAT().getText())
        if ctx.STRING():
            return TACOperand(ctx.STRING().getText())
        if ctx.expressao():
            return self.visit(ctx.expressao())
        return self.visitChildren(ctx)

    # --- CORREÇÃO EXPRESSIVA: Lógica de Curto-Circuito Iterativa ---
    
    def visitExpressao_logica(self, ctx: fimlyParser.Expressao_logicaContext):
        # Lida com expressões como: a > b && c < d || e == f
        left_result = self.visit(ctx.expressao_comparacao(0))

        for i in range(1, len(ctx.expressao_comparacao())):
            op = ctx.getChild(2 * i - 1).getText()
            temp_result = self.new_temp()

            if op == '&&':
                label_false = self.new_label()
                label_end = self.new_label()
                
                # Se left_result for falso, pulamos o teste de 'right' e o resultado já é falso
                self.instructions.append(TACInstruction('IF_FALSE_GOTO', left_result, label_false))
                
                # Se não pulou, testa o right_result
                right_result = self.visit(ctx.expressao_comparacao(i))
                self.instructions.append(TACInstruction('ASSIGN', temp_result, right_result))
                self.instructions.append(TACInstruction('GOTO', label_end))

                # Se pulou para cá, o resultado da expressão é falso
                self.instructions.append(TACInstruction('LABEL', label_false))
                self.instructions.append(TACInstruction('ASSIGN', temp_result, TACOperand(0))) # 'false'
                self.instructions.append(TACInstruction('LABEL', label_end))

                left_result = temp_result # O resultado se torna o operando esquerdo para a próxima iteração
            
            elif op == '||':
                label_true = self.new_label()
                label_end = self.new_label()

                # Se left_result for verdadeiro, não precisa testar 'right', o resultado já é verdadeiro
                # (Para isso, testamos se é falso e pulamos para o teste, caso contrário, o resultado é true)
                self.instructions.append(TACInstruction('IF_FALSE_GOTO', left_result, label_true))

                # Se não pulou, o resultado é verdadeiro
                self.instructions.append(TACInstruction('ASSIGN', temp_result, TACOperand(1))) # 'true'
                self.instructions.append(TACInstruction('GOTO', label_end))

                # Se pulou para cá, o resultado da expressão depende do lado direito
                self.instructions.append(TACInstruction('LABEL', label_true))
                right_result = self.visit(ctx.expressao_comparacao(i))
                self.instructions.append(TACInstruction('ASSIGN', temp_result, right_result))
                self.instructions.append(TACInstruction('LABEL', label_end))
                
                left_result = temp_result

        return left_result

    # --- CORREÇÃO PRINCIPAL: Nomes dos métodos e acesso aos atributos do contexto ---

    def visitComando_atribuicao(self, ctx: fimlyParser.Comando_atribuicaoContext):
        dest = TACOperand(ctx.ID().getText())
        expr_result = self.visit(ctx.expressao())
        self.instructions.append(TACInstruction('ASSIGN', dest, expr_result))
        return dest

    # CORREÇÃO: O nome da regra do 'if' é 'comando_condicional'.
    def visitComando_condicional(self, ctx: fimlyParser.Comando_condicionalContext):
        # Gramática: SE ABRE_PAR expressao FECHA_PAR bloco_comandos (SENAO bloco_comandos)?
        
        # CORREÇÃO: O acesso à condição é por ctx.expressao()
        cond_result = self.visit(ctx.expressao())
        
        # CORREÇÃO: A verificação do 'else' é pela existência do token SENAO
        if ctx.SENAO(): # Temos um if-else
            label_else = self.new_label()
            label_end = self.new_label()
            
            self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_else))
            # CORREÇÃO: O bloco 'if' é o primeiro 'bloco_comandos'
            self.visit(ctx.bloco_comandos(0))
            self.instructions.append(TACInstruction('GOTO', label_end))
            self.instructions.append(TACInstruction('LABEL', label_else))
            # CORREÇÃO: O bloco 'else' é o segundo 'bloco_comandos'
            self.visit(ctx.bloco_comandos(1))
            self.instructions.append(TACInstruction('LABEL', label_end))
            
        else: # Temos apenas um if
            label_end = self.new_label()
            
            self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
            self.visit(ctx.bloco_comandos(0))
            self.instructions.append(TACInstruction('LABEL', label_end))

        return None

    # CORREÇÃO: O nome da regra do laço é 'comando_repeticao'.
    def visitComando_repeticao(self, ctx: fimlyParser.Comando_repeticaoContext):
        # Gramática: ENQUANTO ABRE_PAR expressao FECHA_PAR FACA bloco_comandos
        
        label_start = self.new_label()
        label_end = self.new_label()
        
        self.instructions.append(TACInstruction('LABEL', label_start))
        # CORREÇÃO: O acesso à condição é por ctx.expressao()
        cond_result = self.visit(ctx.expressao())
        self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
        # CORREÇÃO: O acesso ao bloco de comandos é por ctx.bloco_comandos()
        self.visit(ctx.bloco_comandos())
        self.instructions.append(TACInstruction('GOTO', label_start))
        self.instructions.append(TACInstruction('LABEL', label_end))
        
        return None

    # --- Métodos de Visitação Genéricos ---
    def visitBloco_comandos(self, ctx: fimlyParser.Bloco_comandosContext):
        return self.visitChildren(ctx)

    def visitFimly(self, ctx: fimlyParser.FimlyContext):
        return self.visitChildren(ctx)
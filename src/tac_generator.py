from antlr4 import *
from src.fimlyVisitor import fimlyVisitor
from src.fimlyParser import fimlyParser
from src.tac import TACOperand, TACInstruction, GeradorDeCodigoIntermediario

class CodeGenError(Exception):
    pass

class TACGenerator(fimlyVisitor, GeradorDeCodigoIntermediario):
    def __init__(self):
        fimlyVisitor.__init__(self)
        GeradorDeCodigoIntermediario.__init__(self)

    def visitExpressao_aritmetica(self, ctx: fimlyParser.Expressao_aritmeticaContext):
        try:
            left = self.visit(ctx.termo(0))
            for i in range(1, len(ctx.termo())):
                right = self.visit(ctx.termo(i))
                op = ctx.getChild(2 * i - 1).getText()
                if op not in ['+', '-']:
                    raise CodeGenError(f"Operador aritmético inválido: {op}")
                temp = self.new_temp()
                self.instructions.append(TACInstruction(op, temp, left, right))
                left = temp
            return left
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em expressão aritmética] {str(e)}")

    def visitTermo(self, ctx: fimlyParser.TermoContext):
        try:
            left = self.visit(ctx.fator(0))
            for i in range(1, len(ctx.fator())):
                right = self.visit(ctx.fator(i))
                op = ctx.getChild(2 * i - 1).getText()
                temp = self.new_temp()
                self.instructions.append(TACInstruction(op, temp, left, right))
                left = temp
            return left
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em termo] {str(e)}")
    
    def visitExpressao_comparacao(self, ctx:fimlyParser.Expressao_comparacaoContext):
        try:
            left = self.visit(ctx.expressao_aritmetica(0))
            if len(ctx.expressao_aritmetica()) > 1:
                right = self.visit(ctx.expressao_aritmetica(1))
                op = ctx.getChild(1).getText() # Pega o operador de comparação
                temp = self.new_temp()
                self.instructions.append(TACInstruction(op, temp, left, right))
                return temp
            return left
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em expressão de comparação] {str(e)}")

    def visitFator(self, ctx: fimlyParser.FatorContext):
        try:
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
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em fator] {str(e)}")
    
    def visitExpressao_logica(self, ctx: fimlyParser.Expressao_logicaContext):
        try:
            left_result = self.visit(ctx.expressao_comparacao(0))

            for i in range(1, len(ctx.expressao_comparacao())):
                op = ctx.getChild(2 * i - 1).getText()
                temp_result = self.new_temp()

                if op == '&&':
                    label_false = self.new_label()
                    label_end = self.new_label()
                    
                    self.instructions.append(TACInstruction('IF_FALSE_GOTO', left_result, label_false))
                    right_result = self.visit(ctx.expressao_comparacao(i))
                    self.instructions.append(TACInstruction('ASSIGN', temp_result, right_result))
                    self.instructions.append(TACInstruction('GOTO', label_end))

                    self.instructions.append(TACInstruction('LABEL', label_false))
                    self.instructions.append(TACInstruction('ASSIGN', temp_result, TACOperand(0))) # 'false'
                    self.instructions.append(TACInstruction('LABEL', label_end))

                    left_result = temp_result
                
                elif op == '||':
                    label_true = self.new_label()
                    label_end = self.new_label()

                    self.instructions.append(TACInstruction('IF_FALSE_GOTO', left_result, label_true))
                    self.instructions.append(TACInstruction('ASSIGN', temp_result, TACOperand(1))) # 'true'
                    self.instructions.append(TACInstruction('GOTO', label_end))

                    self.instructions.append(TACInstruction('LABEL', label_true))
                    right_result = self.visit(ctx.expressao_comparacao(i))
                    self.instructions.append(TACInstruction('ASSIGN', temp_result, right_result))
                    self.instructions.append(TACInstruction('LABEL', label_end))
                    
                    left_result = temp_result
                else:
                    raise CodeGenError(f"Operador lógico inválido: {op}")

            return left_result
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em expressão lógica] {str(e)}")

    def visitComando_atribuicao(self, ctx: fimlyParser.Comando_atribuicaoContext):
        try:
            dest = TACOperand(ctx.ID().getText())
            expr_result = self.visit(ctx.expressao())
            self.instructions.append(TACInstruction('ASSIGN', dest, expr_result))
            return dest
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em atribuição] {str(e)}")

    def visitComando_condicional(self, ctx: fimlyParser.Comando_condicionalContext):
        try:
            cond_result = self.visit(ctx.expressao())
            
            if ctx.SENAO(): # if-else
                label_else = self.new_label()
                label_end = self.new_label()
                
                self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_else))
                self.visit(ctx.bloco_comandos(0))
                self.instructions.append(TACInstruction('GOTO', label_end))
                self.instructions.append(TACInstruction('LABEL', label_else))
                self.visit(ctx.bloco_comandos(1))
                self.instructions.append(TACInstruction('LABEL', label_end))
                
            else: # if simples
                label_end = self.new_label()
                
                self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
                self.visit(ctx.bloco_comandos(0))
                self.instructions.append(TACInstruction('LABEL', label_end))

            return None
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em comando condicional] {str(e)}")

    def visitComando_repeticao(self, ctx: fimlyParser.Comando_repeticaoContext):
        try:
            label_start = self.new_label()
            label_end = self.new_label()
            
            self.instructions.append(TACInstruction('LABEL', label_start))
            cond_result = self.visit(ctx.expressao())
            self.instructions.append(TACInstruction('IF_FALSE_GOTO', cond_result, label_end))
            self.visit(ctx.bloco_comandos())
            self.instructions.append(TACInstruction('GOTO', label_start))
            self.instructions.append(TACInstruction('LABEL', label_end))
            
            return None
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em comando repetição] {str(e)}")
    
    def visitComando_ler(self, ctx: fimlyParser.Comando_lerContext):
        try:
            var = TACOperand(ctx.ID().getText())
            self.instructions.append(TACInstruction("READ", var))
            return var
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em comando ler] {str(e)}")

    def visitComando_escrever(self, ctx: fimlyParser.Comando_escreverContext):
        try:
            if ctx.lista_expressao():
                for expr in ctx.lista_expressao().expressao():
                    val = self.visit(expr)
                    self.instructions.append(TACInstruction("PRINT", val))
            else:
                pass
            return None
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em comando escrever] {str(e)}")

    def visitComando_declaracao(self, ctx: fimlyParser.Comando_declaracaoContext):
        try:
            var_name = TACOperand(ctx.ID().getText())
            var_type = ctx.tipo().getText()
            self.instructions.append(TACInstruction("DECL", var_name, TACOperand(var_type)))
            return None
        except Exception as e:
            raise CodeGenError(f"[Erro na geração de código intermediário em comando declaração] {str(e)}")

    def visitBloco_comandos(self, ctx: fimlyParser.Bloco_comandosContext):
        return self.visitChildren(ctx)

    def visitFimly(self, ctx: fimlyParser.FimlyContext):
        return self.visitChildren(ctx)

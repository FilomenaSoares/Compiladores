from antlr4 import *
from src.fimlyVisitor import fimlyVisitor
from src.fimlyParser import fimlyParser
from src.tac import TACOperand, TACInstruction, GeradorDeCodigoIntermediario

class TACGenerator(fimlyVisitor, GeradorDeCodigoIntermediario):
    def __init__(self):
        fimlyVisitor.__init__(self)
        GeradorDeCodigoIntermediario.__init__(self)

    # Expressões aritméticas com múltiplos termos (ex: a + b - c)
    def visitExpressao_aritmetica(self, ctx: fimlyParser.Expressao_aritmeticaContext):
        left = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            right = self.visit(ctx.termo(i))
            op = ctx.getChild(2 * i - 1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            left = temp
        return left

    # Termos com multiplicação/divisão
    def visitTermo(self, ctx: fimlyParser.TermoContext):
        left = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            right = self.visit(ctx.fator(i))
            op = ctx.getChild(2 * i - 1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            left = temp
        return left

    # Comparações: ==, !=, >, <, etc
    def visitExpressao_comparacao(self, ctx: fimlyParser.Expressao_comparacaoContext):
        left = self.visit(ctx.expressao_aritmetica(0))
        if ctx.getChildCount() == 3:
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.expressao_aritmetica(1))
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            return temp
        return left

    # Expressões lógicas com E (&&), OU (||)
    def visitExpressao_logica(self, ctx: fimlyParser.Expressao_logicaContext):
        left = self.visit(ctx.expressao_comparacao(0))
        for i in range(1, len(ctx.expressao_comparacao())):
            right = self.visit(ctx.expressao_comparacao(i))
            op = ctx.getChild(2 * i - 1).getText()
            temp = self.new_temp()
            self.instructions.append(TACInstruction(op, temp, left, right))
            left = temp
        return left

    # Literais e identificadores
    def visitFator(self, ctx: fimlyParser.FatorContext):
        if ctx.ID():
            return TACOperand(ctx.ID().getText())
        if ctx.INTEIRO():
            return TACOperand(ctx.INTEIRO().getText())
        if ctx.FLOAT():
            return TACOperand(ctx.FLOAT().getText())
        if ctx.STRING():
            return TACOperand(ctx.STRING().getText())
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expressao())
        return self.visitChildren(ctx)

    # Atribuição: var = expr;
    def visitComando_atribuicao(self, ctx: fimlyParser.Comando_atribuicaoContext):
        var = ctx.ID().getText()
        expr = self.visit(ctx.expressao())
        dest = TACOperand(var)
        self.instructions.append(TACInstruction('=', dest, expr))
        return dest

    # Comando composto
    def visitBloco_comandos(self, ctx: fimlyParser.Bloco_comandosContext):
        for comando in ctx.comandos():
            self.visit(comando)

    # Visit para lista de comandos
    def visitComandos(self, ctx: fimlyParser.ComandosContext):
        return self.visitChildren(ctx)

    # Visit para o programa completo
    def visitFimly(self, ctx: fimlyParser.FimlyContext):
        for comando in ctx.comandos():
            self.visit(comando)
        return None

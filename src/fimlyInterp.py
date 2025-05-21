from src.fimlyVisitor import fimlyVisitor

class FimlyExecutor(fimlyVisitor):
    def __init__(self):
        self.variaveis = {}

    def visitFimly(self, ctx):
        for declaracao in ctx.comando_declaracao():
            self.visit(declaracao)
        for comando in ctx.comandos():
            self.visit(comando)

    def visitComando_declaracao(self, ctx):
        nome = ctx.ID().getText()
        self.variaveis[nome] = 0  # Inicializa com 0 ou None, depende do tipo

    def visitComando_atribuicao(self, ctx):
        nome = ctx.ID().getText()
        valor = self.visit(ctx.expressao())
        self.variaveis[nome] = valor

    def visitComando_ler(self, ctx):
        nome = ctx.ID().getText()
        valor = input(f"Digite o valor de {nome}: ")
        if nome in self.variaveis:
            try:
                valor = int(valor)
            except ValueError:
                try:
                    valor = float(valor)
                except ValueError:
                    pass
            self.variaveis[nome] = valor

    def visitComando_escrever(self, ctx):
        if ctx.lista_expressao():
            valores = self.visit(ctx.lista_expressao())
        for valor in valores:
            if isinstance(valor, str):
                valor = valor.replace("\\n", "\n")
            print(valor, end="")

    def visitLista_expressao(self, ctx):
        return [self.visit(exp) for exp in ctx.expressao()]

    def visitComando_condicional(self, ctx):
        condicao = self.visit(ctx.expressao())
        if condicao:
            self.visit(ctx.bloco_comandos(0))
        elif ctx.SENAO():
            self.visit(ctx.bloco_comandos(1))

    def visitComando_repeticao(self, ctx):
        while self.visit(ctx.expressao()):
            self.visit(ctx.bloco_comandos())

    def visitBloco_comandos(self, ctx):
        for comando in ctx.comandos():
            self.visit(comando)

    def visitExpressao(self, ctx):
        return self.visit(ctx.expressao_logica())

    def visitExpressao_logica(self, ctx):
        resultado = self.visit(ctx.expressao_comparacao(0))
        for i in range(1, len(ctx.expressao_comparacao())):
            op = ctx.getChild(2 * i - 1).getText()
            direito = self.visit(ctx.expressao_comparacao(i))
            if op == '&&':
                resultado = resultado and direito
            elif op == '||':
                resultado = resultado or direito
        return resultado

    def visitExpressao_comparacao(self, ctx):
        esquerda = self.visit(ctx.expressao_aritmetica(0))
        if ctx.expressao_aritmetica(1):
            direita = self.visit(ctx.expressao_aritmetica(1))
            op = ctx.getChild(1).getText()
            if op == '==': return esquerda == direita
            elif op == '!=': return esquerda != direita
            elif op == '<': return esquerda < direita
            elif op == '<=': return esquerda <= direita
            elif op == '>': return esquerda > direita
            elif op == '>=': return esquerda >= direita
        return esquerda

    def visitExpressao_aritmetica(self, ctx):
        resultado = self.visit(ctx.termo(0))
        for i in range(1, len(ctx.termo())):
            op = ctx.getChild(2 * i - 1).getText()
            direito = self.visit(ctx.termo(i))
            if op == '+': resultado += direito
            elif op == '-': resultado -= direito
        return resultado

    def visitTermo(self, ctx):
        resultado = self.visit(ctx.fator(0))
        for i in range(1, len(ctx.fator())):
            op = ctx.getChild(2 * i - 1).getText()
            direito = self.visit(ctx.fator(i))
            if op == '*': resultado *= direito
            elif op == '/': resultado //= direito  # ou usar divisão real se preferir
        return resultado

    def visitFator(self, ctx):
        if ctx.INTEIRO():
            return int(ctx.INTEIRO().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.ID():
            nome = ctx.ID().getText()
            return self.variaveis.get(nome, 0)
        elif ctx.expressao():
            return self.visit(ctx.expressao())
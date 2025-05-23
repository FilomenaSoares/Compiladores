from src.fimlyVisitor import fimlyVisitor
from src.fimlyParser import fimlyParser

class FimlySemanticAnalyzer(fimlyVisitor):
    def __init__(self):
        self.tabela_declaracoes = {}

    def log(self, mensagem):
        print(f'[Log Semântico]: {mensagem}')

    def erro_semantico(self, ctx, mensagem):
        linha = ctx.start.line
        coluna = ctx.start.column + 1
        erro_formatado = f'\033[91m[Erro semântico] (linha {linha}, coluna {coluna}): {mensagem}\033[0m'
        print(erro_formatado)
        raise Exception(erro_formatado)

    #  Verificação da declaração duplicada de variável
    def visitComando_declaracao(self, ctx: fimlyParser.Comando_declaracaoContext):
        nome_variavel = ctx.ID().getText()
        tipo_variavel = ctx.tipo().getText()
        if nome_variavel in self.tabela_declaracoes:
            self.erro_semantico(ctx, f"A variável '{nome_variavel}' já foi declarada.")
        else:
            self.tabela_declaracoes[nome_variavel] = {'type': tipo_variavel}
            self.log(f"Variável '{nome_variavel}' declarada como '{tipo_variavel}'")
        return None

    #  Verifica se variavel foi declarada antes de ser usada
    def visitComando_atribuicao(self, ctx: fimlyParser.Comando_atribuicaoContext):
        nome_variavel = ctx.ID().getText()
        if nome_variavel not in self.tabela_declaracoes:
            self.erro_semantico(ctx, f"A variável '{nome_variavel}' não foi declarada antes de ser usada.")
        else:
            tipo_expressao = self.visit(ctx.expressao())
            tipo_variavel = self.tabela_declaracoes[nome_variavel]['type']
            if tipo_expressao is None or not self.tipos_compatíveis(tipo_variavel, tipo_expressao):
                self.erro_semantico(ctx, f"Tipos incompatíveis: variável '{nome_variavel}' é do tipo '{tipo_variavel}' e expressão é do tipo '{tipo_expressao}'")
        return None

    #  Verificação da declaração prévia dentro de expressões (expr aritimeticas, logicas e condiçional)
    def visitFator(self, ctx: fimlyParser.FatorContext):
        if ctx.ID():
            nome_variavel = ctx.ID().getText()
            if nome_variavel not in self.tabela_declaracoes:
                self.erro_semantico(ctx, f"A variável '{nome_variavel}' foi usada dentro da expressão sem ter sido declarada.")
                return "erro"
            return self.tabela_declaracoes[nome_variavel]['type']
        elif ctx.INTEIRO():
            return 'int'
        elif ctx.FLOAT():
            return 'float'
        elif ctx.STRING():
            return 'string'
        elif ctx.expressao():
            return self.visit(ctx.expressao())
        return None

    #  verificação de divisão por zero, verifica se ela foi declarada.
    def visitTermo(self, ctx: fimlyParser.TermoContext):
        fatores = ctx.fator()

        # Obtem os tokens dos operadores MULTIPLICA e DIVISAO
        multipl = ctx.MULTIPLICA()
        divis = ctx.DIVISAO()

        # Reúne todos os operadores com suas posições para manter ordem correta
        tokens_op = []
        tokens_op += [(tok.symbol.tokenIndex, '*') for tok in multipl]
        tokens_op += [(tok.symbol.tokenIndex, '/') for tok in divis]
        tokens_op.sort(key=lambda x: x[0])
        operadores = [op for _, op in tokens_op]

        for i in range(1, len(fatores)):
            operador = operadores[i - 1] if operadores else None
            fator_ctx = fatores[i]
            # Aqui fazemos a verificação de divisão por zero
            if operador == '/':
                if fator_ctx.INTEIRO() and fator_ctx.getText() == '0':
                    self.erro_semantico(ctx, "Divisão por zero detectada.")
            self.visit(fator_ctx)

        #  Verificação de tipo em operações matemáticas, ele descobre o tipo de cada termo.
        tipos = [self.visit(f) for f in fatores]
        return self.tipo_comum(tipos)

    #  Verificação de tipo em operações matemáticas, ele descobre o tipo de cada termo.
    def visitExpressao_aritmetica(self, ctx: fimlyParser.Expressao_aritmeticaContext):
        tipos = [self.visit(t) for t in ctx.termo()]
        return self.tipo_comum(tipos)

    #Verifica se os dois lados de uma comparação (==, <, etc) são do mesmo tipo
    def visitExpressao_comparacao(self, ctx: fimlyParser.Expressao_comparacaoContext):
        tipo_esquerdo = self.visit(ctx.expressao_aritmetica(0))
        if len(ctx.expressao_aritmetica()) > 1:
            tipo_direito = self.visit(ctx.expressao_aritmetica(1))
            if tipo_esquerdo != tipo_direito and tipo_esquerdo and tipo_direito:
                self.erro_semantico(ctx, f"Não é possível comparar valores de tipos diferentes: '{tipo_esquerdo}' e '{tipo_direito}'")
            return 'bool'
        else:
            return tipo_esquerdo

    # garante que os valores usados em operações lógicas (&&, ||, etc) são booleanos
    def visitExpressao_logica(self, ctx: fimlyParser.Expressao_logicaContext):
        if len(ctx.expressao_comparacao()) == 1:
            return self.visit(ctx.expressao_comparacao(0))

        for subexpr in ctx.expressao_comparacao():
            tipo = self.visit(subexpr)
            if tipo != 'bool':
                self.erro_semantico(ctx, f"Operações lógicas só funcionam com valores booleanos, mas recebeu '{tipo}'")
        return 'bool'
    
    # Auxiliares
    #Garante que string não se misture com números, permite que int e float interajam
    def tipos_compatíveis(self, tipo1, tipo2):
        if tipo1 == tipo2:
            return True
        if tipo1 in ('int', 'float') and tipo2 in ('int', 'float'):
            return True
        return False

    #Determina qual tipo domina numa operação.
    def tipo_comum(self, tipos):
        if not tipos:
            return 'erro'
        if 'erro' in tipos:
            return 'erro'
        if 'string' in tipos:
            return 'string'
        if 'float' in tipos:
            return 'float'
        if 'int' in tipos:
            return 'int'
        return 'erro'

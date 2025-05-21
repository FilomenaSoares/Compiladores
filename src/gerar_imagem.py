import os
from antlr4 import *
from src.fimlyLexer import fimlyLexer
from src.fimlyParser import fimlyParser
from antlr4.tree.Tree import TerminalNode

class ParseTreeGenerator:
    def __init__(self):
        self.node_counter = 0
        self.output = []

    def new_node(self, label):
        node_name = f"n{self.node_counter}"
        label = label.replace('"', r'\"')
        self.output.append(f'{node_name} [label="{label}"];')
        self.node_counter += 1
        return node_name

    def add_edge(self, parent, child):
        self.output.append(f"{parent} -> {child};")

    def visit(self, ctx):
        if ctx is None:
            return self.new_node("null")

        if isinstance(ctx, TerminalNode):
            return self.new_node(f"'{ctx.getText()}'")

        rule_name = type(ctx).__name__.replace("Context", "")
        node = self.new_node(rule_name)

        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            child_node = self.visit(child)
            self.add_edge(node, child_node)

        return node

def gerar_arquivo_dot(arquivo_fonte, output_dot_path):
    input_stream = FileStream(arquivo_fonte, encoding='utf-8')
    lexer = fimlyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = fimlyParser(token_stream)
    tree = parser.fimly()

    generator = ParseTreeGenerator()
    generator.visit(tree)

    dot_graph = "digraph G {\n" + "\n".join(generator.output) + "\n}"

    with open(output_dot_path, "w", encoding='utf-8') as f:
        f.write(dot_graph)

    print(f"Arquivo {output_dot_path} criado.")

def converter_dot_para_png(dot_path, output_png):
    comando = f"dot -Tpng {dot_path} -o {output_png}"
    os.system(comando)
    print(f"Imagem {output_png} gerada.")

def gerar_arvore_e_imagem(arquivo_fonte, pasta_destino="imagens"):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    nome_base = os.path.splitext(os.path.basename(arquivo_fonte))[0]
    dot_path = os.path.join(pasta_destino, f"{nome_base}.dot")
    png_path = os.path.join(pasta_destino, f"{nome_base}.png")

    gerar_arquivo_dot(arquivo_fonte, dot_path)
    converter_dot_para_png(dot_path, png_path)

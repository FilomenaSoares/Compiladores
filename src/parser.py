from antlr4 import *
from src.fimlyLexer import fimlyLexer
from src.fimlyParser import fimlyParser
from src.CustomErrorListener import CustomErrorListener
from src.ast_visualizer import ASTVisualizer

def parse_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    
    # Etapa léxica
    lexer = fimlyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Etapa sintática
    parser = fimlyParser(token_stream)

    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Ponto de entrada da gramática (ajuste se seu nome for diferente)
    tree = parser.fimly()

    if error_listener.tem_erro:
        print("Erro sintático detectado. Abortando.")
        return None

    # AST fictícia baseada na estrutura da árvore
    visualizer = ASTVisualizer()
    root = visualizer.create_node("programa")

    # Aqui você pode melhorar a conversão da árvore de derivação para AST
    for child in tree.children:
        node_name = f"{type(child).__name__}: {child.getText()}"
        node = visualizer.create_node(node_name, parent=root)

    return root

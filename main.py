from antlr4 import *
from src.fimlyLexer import fimlyLexer
from src.fimlyParser import fimlyParser
from src.parser import parse_file
from src.CustomErrorListener import CustomErrorListener
from src.scanner import scan_file
from src.fimlySemanticAnalyzer import FimlySemanticAnalyzer
from src.gerar_imagem import gerar_arvore_e_imagem
from src.tac_generator import TACGenerator

def mostrar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            conteudo = file.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")

def main():
    arquivo_fimly = "codigo.fimly"  # Nome do arquivo a ser lido

    # Mostrar conteúdo do arquivo no terminal
    print("\n=== Conteúdo do arquivo ===")
    mostrar_arquivo(arquivo_fimly)

    # Scanner
    tokens, tem_erro_lexico = scan_file(arquivo_fimly)
    if tem_erro_lexico:
        print("Erros léxicos encontrados. Encerrando.")
        return

    # Parser
    input_stream = FileStream(arquivo_fimly, encoding='utf-8')
    lexer = fimlyLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = fimlyParser(token_stream)

    parser.removeErrorListeners()
    error_listener = CustomErrorListener()
    parser.addErrorListener(error_listener)

    arvore = parser.fimly()

    if error_listener.tem_erro:
        print("Erros sintáticos encontrados. Encerrando.")
        return

    # Análise Semântica
    analisador = FimlySemanticAnalyzer()
    try:
        analisador.visit(arvore)
    except Exception as e:
        print(e)
        print("Análise semântica encerrada devido a erro.")
        return

    # Geração da AST (caso queira a imagem)
    gerar_arvore_e_imagem(arquivo_fimly, pasta_destino="imagens")

    # Geração de código intermediário (TAC)
    gerador = TACGenerator()
    gerador.visit(arvore)

    # Exibir as instruções TAC geradas
    print("\n=== Código Intermediário (TAC) ===")
    for instrucao in gerador.instructions:
        print(instrucao)

if __name__ == "__main__":
    main()

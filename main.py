import argparse
from antlr4 import *
from src.fimlyLexer import fimlyLexer
from src.fimlyParser import fimlyParser
from src.CustomErrorListener import CustomErrorListener
from src.scanner import scan_file
from src.fimlySemanticAnalyzer import FimlySemanticAnalyzer
from src.tac_generator import TACGenerator
from src.llvm_generator import LLVMGenerator  # Importe a classe que mostrei antes!

def mostrar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")

def main():
    parser = argparse.ArgumentParser(description="Compilador Fimly")
    parser.add_argument("arquivo", help="Arquivo fonte .fimly")
    parser.add_argument("--gerar-tac", action="store_true", help="Gerar arquivo .tac com código intermediário")
    parser.add_argument("--gerar-ast", action="store_true", help="Gerar imagem da AST")
    parser.add_argument("--gerar-llvm", action="store_true", help="Gerar código LLVM IR (.ll)")
    args = parser.parse_args()

    codigo_fimly = args.arquivo

    print("\n=== Conteúdo do arquivo ===")
    mostrar_arquivo(codigo_fimly)

    # Scanner (Análise léxica)
    tokens, tem_erro_lexico = scan_file(codigo_fimly)
    if tem_erro_lexico:
        print("Erros léxicos encontrados. Encerrando.")
        return

    # Parser (Análise sintática)
    try:
        input_stream = FileStream(codigo_fimly, encoding='utf-8')
    except FileNotFoundError:
        print(f"Arquivo {codigo_fimly} não encontrado. Encerrando.")
        return

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
        print(f"Erro semântico: {e}")
        print("Análise semântica encerrada devido a erro.")
        return

    # Gerar AST (imagem) se solicitado
    if args.gerar_ast:
        from src.gerar_imagem import gerar_arvore_e_imagem
        gerar_arvore_e_imagem(codigo_fimly, pasta_destino="imagens")

    # Gerar código intermediário TAC
    gerador = TACGenerator()
    try:
        gerador.visit(arvore)
    except Exception as e:
        print(f"Erro na geração do código intermediário: {e}")
        return

    # Exibir TAC no terminal
    print("\n=== Código Intermediário (TAC) ===")
    for instrucao in gerador.instructions:
        print(instrucao)

    # Salvar TAC em arquivo se solicitado
    if args.gerar_tac:
        nome_saida = codigo_fimly.rsplit('.', 1)[0] + '.tac'
        try:
            with open(nome_saida, 'w', encoding='utf-8') as f:
                for instrucao in gerador.instructions:
                    f.write(str(instrucao) + '\n')
            print(f"\nArquivo TAC gerado: {nome_saida}")
        except Exception as e:
            print(f"Erro ao salvar arquivo TAC: {e}")

    # Gerar código LLVM IR se solicitado
    if args.gerar_llvm:
        llvm_gen = LLVMGenerator(gerador.instructions)
        codigo_llvm = llvm_gen.generate()

        nome_llvm = codigo_fimly.rsplit('.', 1)[0] + '.ll'
        try:
            with open(nome_llvm, 'w', encoding='utf-8') as f:
                f.write(codigo_llvm)
            print(f"\nArquivo LLVM IR gerado: {nome_llvm}")
        except Exception as e:
            print(f"Erro ao salvar arquivo LLVM IR: {e}")

if __name__ == "__main__":
    main()

#Para executar o compilador, use o seguinte comando no terminal
 #python main.py seu_codigo.fimly --gerar-tac --gerar-llvm --gerar-ast

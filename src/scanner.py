from antlr4 import *
from src.fimlyLexer import fimlyLexer
from src.CustomErrorListener import CustomErrorListener

def scan_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    lexer = fimlyLexer(input_stream)
    
    lexer.removeErrorListeners()
    error_listener = CustomErrorListener()
    lexer.addErrorListener(error_listener)

    tokens = CommonTokenStream(lexer)
    tokens.fill()

    print("TOKENS RECONHECIDOS:")
    for token in tokens.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type]
            print(f"<{token_name}, '{token.text}', Linha {token.line}, Coluna {token.column}>")

    return tokens, error_listener.tem_erro

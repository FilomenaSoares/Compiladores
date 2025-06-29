# 📘 Compilador - Fimly

Este repositório contém o desenvolvimento de um compilador para uma linguagem fictícia, baseada em elementos do **C** e do **Portugol**, com base em uma gramática criada por **Emmylly** e **Filomena Soares**, definida no arquivo `fimly.g4`.

O compilador é implementado utilizando a ferramenta **ANTLR4** com a linguagem **Python**, e possui etapas completas de análise léxica, sintática, semântica, geração de código intermediário (TAC), geração de árvore sintática (AST) em imagem e geração de código LLVM IR.

---

## 📑 Índice

1. [🎯 Objetivo](#-objetivo)
2. [🌐 Linguagem Fimly](#-linguagem-fimly)
3. [🧠 Gramática Fimly](#-gramática-fimly)
4. [🧾 Tokens da Linguagem Fimly](#-tokens-da-linguagem-fimly)
   - [📌 Palavras-chave](#-palavras-chave)
   - [🧩 Tipos de dados](#-tipos-de-dados)
   - [➕ Operadores e Símbolos](#-operadores-e-símbolos)
   - [🧱 Delimitadores](#-delimitadores)
   - [🆔 Literais e Identificadores](#-literais-e-identificadores)
   - [🧹 Espaços em branco e Comentários](#-espaços-em-branco-e-comentários)
5. [✨ Funcionalidades](#-funcionalidades)
6. [🛠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
7. [🚀 Como Executar](#-como-executar)
8. [⚙️ Compilação do LLVM IR no Windows](#️-compilação-do-llvm-ir-no-windows)
9. [💾 Saídas Esperadas](#-saídas-esperadas)
10. [👩‍💻 Autoras](#-autoras)

---

## 🎯 Objetivo

O objetivo principal do projeto é:

- Processar um código-fonte `codigo.fimly`
- Gerar tokens e reconhecer lexemas (análise léxica)
- Relatar erros léxicos e sintáticos
- Gerar uma **imagem da AST (árvore sintática)** em `.png`
- Salvar a árvore também em `codigo.dot` para visualização com o Graphviz
- Realizar análise semântica (validação de tipos e escopos)
- Gerar **código intermediário** (Código de três endereços - TAC)
- Gerar **código LLVM IR (codigo.ll)** compilável com `clang`

---

## 🌐 Linguagem Fimly

A linguagem **Fimly** é uma linguagem didática, criada como exercício de projeto de compiladores. É uma fusão dos nomes **Filomena** e **Emmylly** e traz uma sintaxe intuitiva, parecida com Portugol.

Exemplo de código Fimly:

```fimly
valor: int;
a: int;
b: int;

inicio
    escreva("Digite um valor para a:");
    leia(a);
    escreva("Digite um valor para b:");
    leia(b);
    valor = a + b;
    escreva(valor);
fim
```
---

## 🧠 Gramática Fimly

```
grammar fimly;

// Tokens
INICIO     : 'inicio';
LEIA       : 'leia';
ESCREVA    : 'escreva';
FIM        : 'fim';
SE         : 'se' ;
ENTAO      : 'entao' ;
SENAO      : 'senao' ;
ENQUANTO   : 'enquanto' ;
FACA       : 'faca' ;

// Tipos de dados
TIPO_INTEIRO   : 'int' ;                      
TIPO_FLOAT     : 'float' ;
TIPO_STRING    : 'string' ;

// Símbolos
ADICAO     : '+' ;
SUBTRACAO  : '-' ;
DIVISAO    : '/' ;
MULTIPLICA : '*' ;
IGUAL      : '==';
DIFERENTE  : '!=';
MAIORIGUAL : '>=';
MENORIGUAL : '<=';
MAIOR      : '>';
MENOR      : '<';
ATRIBUICAO : '=';
NAO        : '!';
E          : '&&';
OU         : '||';
ABRE_PAR   : '(' ;
DOIS_PONTOS: ':' ;
FECHA_PAR  : ')' ;
ABRE_CHAVE : '{' ;
FECHA_CHAVE: '}' ;
PONTO_VIR  : ';' ;
VIRG       : ',' ;

// Literais e identificadores
ID        : [a-zA-Z_] [a-zA-Z_0-9]*;         
INTEIRO   : ('0'..'9')+;
FLOAT     : ('0'..'9')+ '.' ('0'..'9')*;
STRING    : '"' ~["\r\n]* '"' ;

// Reconhece espaço em branco
COMENTARIO : '//' ~[\r\n]* -> skip ;
WS         : [ \t\n\r\f]+ -> skip ;


// Regras de gramática
fimly
    : (comando_declaracao)* INICIO comandos* FIM
    ;

comando_declaracao
    : ID DOIS_PONTOS tipo PONTO_VIR
    ;

tipo
    : TIPO_INTEIRO
    | TIPO_FLOAT
    | TIPO_STRING
    ;

comandos
    : comando_ler
    | comando_escrever
    | comando_condicional
    | comando_repeticao
    | comando_atribuicao
    ;

comando_ler
    : LEIA ABRE_PAR ID FECHA_PAR PONTO_VIR
    ;

comando_escrever
    : ESCREVA ABRE_PAR lista_expressao? FECHA_PAR PONTO_VIR
    ;

lista_expressao
    : expressao (VIRG expressao)*
    ;

bloco_comandos: ABRE_CHAVE comandos* FECHA_CHAVE;

comando_condicional
    : SE ABRE_PAR expressao FECHA_PAR bloco_comandos (SENAO bloco_comandos)?
    ;

comando_repeticao
    : ENQUANTO ABRE_PAR expressao FECHA_PAR FACA bloco_comandos
    ;

comando_atribuicao
    : ID ATRIBUICAO expressao PONTO_VIR
    ;

expressao
    : expressao_logica
    ;

expressao_logica
    : expressao_comparacao ( (E | OU) expressao_comparacao )*
    ;

expressao_comparacao
    : expressao_aritmetica ( (IGUAL | DIFERENTE | MAIOR | MAIORIGUAL | MENOR | MENORIGUAL) expressao_aritmetica )?
    ;

expressao_aritmetica
    : termo ( (ADICAO | SUBTRACAO) termo )*
    ;

termo
    : fator ( (MULTIPLICA | DIVISAO) fator )*
    ;

fator
    : INTEIRO
    | FLOAT
    | STRING
    | ID
    | ABRE_PAR expressao FECHA_PAR
    ;
```

## 🎯 Tokens da Linguagem Fimly

A seguir, estão listados os tokens reconhecidos pela linguagem Fimly, divididos por categorias:

### 📌 Palavras-chave

| Token     | Lexema     |
|-----------|------------|
| `INICIO`  | `inicio`   |
| `LEIA`    | `leia`     |
| `ESCREVA` | `escreva`  |
| `FIM`     | `fim`      |
| `SE`      | `se`       |
| `ENTAO`   | `entao`    |
| `SENAO`   | `senao`    |
| `ENQUANTO`| `enquanto` |
| `FACA`    | `faca`     |

### 🧩 Tipos de dados

| Token          | Lexema  |
|----------------|---------|
| `TIPO_INTEIRO` | `int`   |
| `TIPO_FLOAT`   | `float` |
| `TIPO_STRING`  | `string`|

### ➕ Operadores e Símbolos

| Token        | Símbolo |
|--------------|---------|
| `ADICAO`     | `+`     |
| `SUBTRACAO`  | `-`     |
| `DIVISAO`    | `/`     |
| `MULTIPLICA` | `*`     |
| `IGUAL`      | `==`    |
| `DIFERENTE`  | `!=`    |
| `MAIORIGUAL` | `>=`    |
| `MENORIGUAL` | `<=`    |
| `MAIOR`      | `>`     |
| `MENOR`      | `<`     |
| `ATRIBUICAO` | `=`     |
| `NAO`        | `!`     |
| `E`          | `&&`    |
| `OU`         | `||`    |

### 🧱 Delimitadores

| Token         | Símbolo |
|---------------|---------|
| `ABRE_PAR`    | `(`     |
| `FECHA_PAR`   | `)`     |
| `ABRE_CHAVE`  | `{`     |
| `FECHA_CHAVE` | `}`     |
| `DOIS_PONTOS` | `:`     |
| `PONTO_VIR`   | `;`     |
| `VIRG`        | `,`     |

### 🆔 Literais e Identificadores

| Token     | Padrão (Regex)                |
|-----------|-------------------------------|
| `ID`      | `[a-zA-Z_] [a-zA-Z_0-9]*`     |
| `INTEIRO` | `('0'..'9')+`                 |
| `FLOAT`   | `('0'..'9')+ '.' ('0'..'9')*` |
| `STRING`  | `"` ~["\\r\\n]* `"`           |

### 🧹 Espaços em branco e Comentários

| Token       | Descrição                     |
|-------------|-------------------------------|
| `COMENTARIO`| Comentário de linha `// ...` |
| `WS`        | Espaços, tabs e quebras de linha |

---

## ✨ Funcionalidades

- **Leitura de código-fonte:** O compilador processa arquivo codigo.fimly e gera tokens organizados.
- **Log de erros:** Erros léxicos e sintáticos são exibidos em tempo real ou armazenados em log.
- **Análise sintática:** Utiliza a gramática fimly.g4 para verificar a estrutura do programa.
- **Geração de AST:** Salva a árvore sintática como .dot e .png.
- **Análise semântica:** Valida declarações de variáveis e tipos.
- **Geração de TAC:** Código intermediário otimizado e legível.
- **Geração de LLVM IR:** Código de baixo nível compilável via clang.

---

## 🛠 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/downloads/)
- [ANTLR4](https://www.antlr.org/)
- Biblioteca `antlr4-python3-runtime`
- [LLVM Clang](https://llvm.org/builds/)
- [Visual Studio 2022 Build Tools (para libs e linker MSVC)](https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/)

---

## 🚀 Como Executar
Com as ferramentas já instaladas:
1. **Instale as dependências:**
   ```bash
   pip install antlr4-python3-runtime
2. Gere o parser e lexer com ANTLR:
   ```bash
   antlr4 -Dlanguage=Python3 fimly.g4
3. Execute o compilador:
   ```bash
   python main.py codigo.fimly --gerar-tac --gerar-llvm --gerar-ast

---

### ⚙️ Compilação do LLVM IR no Windows
- Visual Studio 2022 Build Tools instalado (com C++ tools)
- LLVM Clang instalado (ex: https://llvm.org/builds/)
- Variáveis de ambiente do Visual Studio configuradas para x64 (executando vcvars64.bat)

Passo a passo:
1. Abra o Prompt de Comando do Windows
   - Pressione a tecla ```Windows + R```, digite ```cmd``` e pressione Enter.
   
2. Configure o ambiente Visual Studio x64
   - Execute o script que configura as variáveis de ambiente para compilação 64 bits:
   ```bash
   call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

3. Vá até a pasta onde está salvo seu projeto
- Meu Exemplo:
   ```bash
   cd C:\Users\memmy\OneDrive\Documentos\GitHub\Compiladores

4. Compile o código LLVM IR para executável
   - No prompt (mesmo ambiente onde rodou o passo anterior), execute:
   ```bash
   C:\Program Files\LLVM\bin\clang.exe" -target x86_64-pc-windows-msvc codigo.ll -o programa.exe -llegacy_stdio_definitions
    ```
   - Esse comando usa clang para gerar  ```programa.exe ``` a partir do  ```codigo.ll```.
   - A opção  ```-llegacy_stdio_definitions ``` é importante para resolver funções C padrão como  ```printf ``` e  ```scanf ```.

5. Execute o Programa
   ```bash
      programa.exe

---

## 💾 Saídas Esperadas
Ao executar o compilador com o comando acima, espere as seguintes saídas no terminal:

### Conteúdo do arquivo
```bash
=== Conteúdo do arquivo ===

valor: int;
a: int;
b: int;

inicio
    escreva("Digite um valor para a:");
    leia(a);
    escreva("Digite um valor para b:");
    leia(b);
    valor = a + b;
    escreva(valor);
fim
```

### Tokens Reconhecidos (Análise Léxica)
```bash
=== ANALÍSE LÉXICA ===
TOKENS RECONHECIDOS:
<ID, 'valor', Linha 2, Coluna 0>
<DOIS_PONTOS, ':', Linha 2, Coluna 5>
<TIPO_INTEIRO, 'int', Linha 2, Coluna 7>
<PONTO_VIR, ';', Linha 2, Coluna 10>
<ID, 'a', Linha 3, Coluna 0>
<DOIS_PONTOS, ':', Linha 3, Coluna 1>
<TIPO_INTEIRO, 'int', Linha 3, Coluna 3>
<PONTO_VIR, ';', Linha 3, Coluna 6>
<ID, 'b', Linha 4, Coluna 0>
<DOIS_PONTOS, ':', Linha 4, Coluna 1>
<TIPO_INTEIRO, 'int', Linha 4, Coluna 3>
<PONTO_VIR, ';', Linha 4, Coluna 6>
<INICIO, 'inicio', Linha 6, Coluna 0>
<ESCREVA, 'escreva', Linha 7, Coluna 4>
<ABRE_PAR, '(', Linha 7, Coluna 11>
<STRING, '"Digite um valor para a:"', Linha 7, Coluna 12>
<FECHA_PAR, ')', Linha 7, Coluna 37>
<PONTO_VIR, ';', Linha 7, Coluna 38>
<LEIA, 'leia', Linha 8, Coluna 4>
<ABRE_PAR, '(', Linha 8, Coluna 8>
<ID, 'a', Linha 8, Coluna 9>
<FECHA_PAR, ')', Linha 8, Coluna 10>
<PONTO_VIR, ';', Linha 8, Coluna 11>
<ESCREVA, 'escreva', Linha 9, Coluna 4>
<ABRE_PAR, '(', Linha 9, Coluna 11>
<STRING, '"Digite um valor para b:"', Linha 9, Coluna 12>
<FECHA_PAR, ')', Linha 9, Coluna 37>
<PONTO_VIR, ';', Linha 9, Coluna 38>
<LEIA, 'leia', Linha 10, Coluna 4>
<ABRE_PAR, '(', Linha 10, Coluna 8>
<ID, 'b', Linha 10, Coluna 9>
<FECHA_PAR, ')', Linha 10, Coluna 10>
<PONTO_VIR, ';', Linha 10, Coluna 11>
<ID, 'valor', Linha 11, Coluna 4>
<ATRIBUICAO, '=', Linha 11, Coluna 10>
<ID, 'a', Linha 11, Coluna 12>
<ADICAO, '+', Linha 11, Coluna 14>
<ID, 'b', Linha 11, Coluna 16>
<PONTO_VIR, ';', Linha 11, Coluna 17>
<ESCREVA, 'escreva', Linha 12, Coluna 4>
<ABRE_PAR, '(', Linha 12, Coluna 11>
<ID, 'valor', Linha 12, Coluna 12>
<FECHA_PAR, ')', Linha 12, Coluna 17>
<PONTO_VIR, ';', Linha 12, Coluna 18>
<FIM, 'fim', Linha 13, Coluna 0>
```

### Análise Sintática
```bash
=== ANALÍSE SINTATICA ===
[Log Semântico]: Variável 'valor' declarada como 'int'
[Log Semântico]: Variável 'a' declarada como 'int'
[Log Semântico]: Variável 'b' declarada como 'int'
```

### Imagem da AST
   - Será criada a imagem ```imagens/codigo.png``` e o arquivo  ```imagens/codigo.dot``` para visualização gráfica da árvore sintática.
```bash
=== IMAGEM GERADA (AST) ===
Arquivo imagens\codigo.dot criado.
Imagem imagens\codigo.png gerada.
```

### Código Intermediário (TAC)
```bash
=== CÓDIGO INTERMEDIÁRIO (TAC) ===
DECL valor, int
DECL a, int
DECL b, int
PRINT "Digite um valor para a:"
READ a
PRINT "Digite um valor para b:"
READ b
_t1 = a + b
valor = _t1
PRINT valor
```

### Arquivos Gerados
codigo.tac — arquivo contendo o código intermediário TAC.
```bash
=== ARQUIVO TAC ===

Arquivo TAC gerado: codigo.tac
```

codigo.ll — arquivo contendo o código LLVM IR compilável.
```bash
=== ARQUIVO DE LLVM IR ===

Arquivo LLVM IR gerado: codigo.ll
```
### Saída do Programa no Prompt

Ao executar o programa gerado (`programa.exe`), o usuário verá a seguinte interação no prompt de comando:

```bash
Digite um valor para a:
5
Digite um valor para b:
7
12
```

---

## 👩‍💻 Autoras
- [Emmylly](https://github.com/EmmyllyDev)
- [Filomena Soares](https://github.com/FilomenaSoares)



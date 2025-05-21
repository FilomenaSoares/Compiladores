# Criação de um Mini Compilador

Este repositório contém o desenvolvimento de um compilador para uma linguagem fictícia, com base em uma gramática que eu e Filomena Soares criamos e definimos no arquivo `fimly.g4`. O compilador é implementado utilizando a biblioteca **ANTLR**, e o objetivo é processar código-fonte, gerar tokens e relatar erros léxicos.

## 🧠 Minha Linguagem

O nome da linguagem é **Fimly**, uma junção dos nomes **Filomena** e **Emmylly**.

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



## ✨ Funcionalidades

- **Leitura de código-fonte:** O compilador processa arquivos `.fonte` e gera tokens no formato:
- **Log de erros:** Erros léxicos e outros problemas são registrados em arquivo de log ou exibidos no terminal.
- **Erros léxicos:** O compilador identifica e reporta erros no seguinte formato:

## 🛠 Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/downloads/)
- [ANTLR4](https://www.antlr.org/)
- Biblioteca `antlr4-python3-runtime`

## 🚀 Como Executar
Com as ferramentas já instaladas (Python e ANTLR4):
1. **Instale as dependências:**
   ```bash
   pip install antlr4-python3-runtime
2. Gere o parser e lexer com ANTLR:
   ```bash
   antlr4 -Dlanguage=Python3 fimly.g4
3. Execute o compilador:
   ```bash
    python testar_linguagem.py
## 👩‍💻 Autoras
- [Emmylly](https://github.com/EmmyllyDev)
- [Filomena Soares](https://github.com/FilomenaSoares)



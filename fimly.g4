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
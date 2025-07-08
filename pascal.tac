DECL n, int
DECL i, int
DECL j, int
DECL k, int
DECL valor, int
DECL s, int
PRINT "Digite um numero inteiro: \n"
READ n
_t1 = n < 1
IF_FALSE _t1 GOTO L1
PRINT "Erro: numero deve ser maior ou igual a 1."
GOTO L2
L1:
i = 0
L3:
_t2 = i < n
IF_FALSE _t2 GOTO L4
s = 0
L5:
_t3 = n - i
_t4 = _t3 - 1
_t5 = s < _t4
IF_FALSE _t5 GOTO L6
PRINT " "
_t6 = s + 1
s = _t6
GOTO L5
L6:
j = 0
L7:
_t7 = j <= i
IF_FALSE _t7 GOTO L8
valor = 1
_t8 = j > 0
IF_FALSE _t8 GOTO L9
k = 0
L10:
_t9 = k < j
IF_FALSE _t9 GOTO L11
_t10 = i - k
_t11 = valor * _t10
_t12 = k + 1
_t13 = _t11 / _t12
valor = _t13
_t14 = k + 1
k = _t14
GOTO L10
L11:
L9:
PRINT valor
_t15 = j + 1
j = _t15
GOTO L7
L8:
PRINT "\n"
_t16 = i + 1
i = _t16
GOTO L3
L4:
L2:

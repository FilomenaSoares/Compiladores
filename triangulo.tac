DECL a, float
DECL b, float
DECL c, float
PRINT "Digite um valor para o lado a:"
READ a
PRINT "Digite um valor para o lado b:"
READ b
PRINT "Digite um valor para o lado c:"
READ c
_t1 = a <= 0.0
_t2 = b <= 0.0
|| _t3, _t1, _t2
_t4 = c <= 0.0
|| _t5, _t3, _t4
_t6 = a + b
_t7 = _t6 <= c
|| _t8, _t5, _t7
_t9 = a + c
_t10 = _t9 <= b
|| _t11, _t8, _t10
_t12 = b + c
_t13 = _t12 <= a
|| _t14, _t11, _t13
IF_FALSE _t14 GOTO L1
PRINT "Medidas invalidas"
GOTO L2
L1:
_t15 = a == b
_t16 = b == c
&& _t17, _t15, _t16
IF_FALSE _t17 GOTO L3
PRINT "Triangulo equilatero valido"
GOTO L4
L3:
_t18 = a == b
_t19 = b == c
|| _t20, _t18, _t19
_t21 = a == c
|| _t22, _t20, _t21
IF_FALSE _t22 GOTO L5
PRINT "Triangulo isosceles valido"
GOTO L6
L5:
PRINT "Triangulo escaleno valido"
L6:
L4:
L2:

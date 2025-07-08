DECL a, int
DECL b, int
DECL c, int
PRINT "Digite um valor para o lado a: \n"
READ a
PRINT "Digite um valor para o lado b: \n"
READ b
PRINT "Digite um valor para o lado c: \n"
READ c
_t1 = a <= 0
IF_FALSE _t1 GOTO L1
PRINT "Medidas invalidas"
GOTO L2
L1:
_t2 = a == b
IF_FALSE _t2 GOTO L3
PRINT "Triangulo equilatero valido"
GOTO L4
L3:
_t3 = a == b
IF_FALSE _t3 GOTO L5
PRINT "Triangulo isosceles valido"
GOTO L6
L5:
PRINT "Triangulo escaleno valido"
L6:
L4:
L2:

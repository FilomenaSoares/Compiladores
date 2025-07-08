; LLVM IR Gerado pelo Compilador Fimly
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@print_int_fmt = private unnamed_addr constant [3 x i8] c"%d\00"
@print_float_fmt = private unnamed_addr constant [3 x i8] c"%f\00"
@scan_int_fmt = private unnamed_addr constant [3 x i8] c"%d\00"
@scan_float_fmt = private unnamed_addr constant [4 x i8] c"%lf\00"

@msg0 = private unnamed_addr constant [31 x i8] c"Digite um valor para o lado a:\00"
@msg1 = private unnamed_addr constant [31 x i8] c"Digite um valor para o lado b:\00"
@msg2 = private unnamed_addr constant [31 x i8] c"Digite um valor para o lado c:\00"
@msg3 = private unnamed_addr constant [18 x i8] c"Medidas invalidas\00"
@msg4 = private unnamed_addr constant [28 x i8] c"Triangulo equilatero valido\00"
@msg5 = private unnamed_addr constant [27 x i8] c"Triangulo isosceles valido\00"
@msg6 = private unnamed_addr constant [26 x i8] c"Triangulo escaleno valido\00"

define i32 @main() {
entry:
  %a = alloca double
  %b = alloca double
  %c = alloca double
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([31 x i8], [31 x i8]* @msg0, i32 0, i32 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @scan_float_fmt, i32 0, i32 0), double* %a)
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([31 x i8], [31 x i8]* @msg1, i32 0, i32 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @scan_float_fmt, i32 0, i32 0), double* %b)
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([31 x i8], [31 x i8]* @msg2, i32 0, i32 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @scan_float_fmt, i32 0, i32 0), double* %c)
  %r1 = load double, double* %a
  %r2 = fcmp ole double %r1, 0.0
  %r3 = zext i1 %r2 to i32
  %_t1 = alloca i32
  store i32 %r3, i32* %_t1
  %r4 = load double, double* %b
  %r5 = fcmp ole double %r4, 0.0
  %r6 = zext i1 %r5 to i32
  %_t2 = alloca i32
  store i32 %r6, i32* %_t2
  %r7 = load i32, i32* %_t1
  %r8 = load i32, i32* %_t2
  %r9 = or i32 %r7, %r8
  %_t3 = alloca i32
  store i32 %r9, i32* %_t3
  %r10 = load double, double* %c
  %r11 = fcmp ole double %r10, 0.0
  %r12 = zext i1 %r11 to i32
  %_t4 = alloca i32
  store i32 %r12, i32* %_t4
  %r13 = load i32, i32* %_t3
  %r14 = load i32, i32* %_t4
  %r15 = or i32 %r13, %r14
  %_t5 = alloca i32
  store i32 %r15, i32* %_t5
  %r16 = load double, double* %a
  %r17 = load double, double* %b
  %r18 = fadd double %r16, %r17
  %_t6 = alloca double
  store double %r18, double* %_t6
  %r19 = load double, double* %_t6
  %r20 = load double, double* %c
  %r21 = fcmp ole double %r19, %r20
  %r22 = zext i1 %r21 to i32
  %_t7 = alloca i32
  store i32 %r22, i32* %_t7
  %r23 = load i32, i32* %_t5
  %r24 = load i32, i32* %_t7
  %r25 = or i32 %r23, %r24
  %_t8 = alloca i32
  store i32 %r25, i32* %_t8
  %r26 = load double, double* %a
  %r27 = load double, double* %c
  %r28 = fadd double %r26, %r27
  %_t9 = alloca double
  store double %r28, double* %_t9
  %r29 = load double, double* %_t9
  %r30 = load double, double* %b
  %r31 = fcmp ole double %r29, %r30
  %r32 = zext i1 %r31 to i32
  %_t10 = alloca i32
  store i32 %r32, i32* %_t10
  %r33 = load i32, i32* %_t8
  %r34 = load i32, i32* %_t10
  %r35 = or i32 %r33, %r34
  %_t11 = alloca i32
  store i32 %r35, i32* %_t11
  %r36 = load double, double* %b
  %r37 = load double, double* %c
  %r38 = fadd double %r36, %r37
  %_t12 = alloca double
  store double %r38, double* %_t12
  %r39 = load double, double* %_t12
  %r40 = load double, double* %a
  %r41 = fcmp ole double %r39, %r40
  %r42 = zext i1 %r41 to i32
  %_t13 = alloca i32
  store i32 %r42, i32* %_t13
  %r43 = load i32, i32* %_t11
  %r44 = load i32, i32* %_t13
  %r45 = or i32 %r43, %r44
  %_t14 = alloca i32
  store i32 %r45, i32* %_t14
  %r46 = load i32, i32* %_t14
  %r47 = icmp eq i32 %r46, 0
  br i1 %r47, label %L1, label %L_auto_1
L_auto_1:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @msg3, i32 0, i32 0))
  br label %L2
L1:
  %r48 = load double, double* %a
  %r49 = load double, double* %b
  %r50 = fcmp oeq double %r48, %r49
  %r51 = zext i1 %r50 to i32
  %_t15 = alloca i32
  store i32 %r51, i32* %_t15
  %r52 = load double, double* %b
  %r53 = load double, double* %c
  %r54 = fcmp oeq double %r52, %r53
  %r55 = zext i1 %r54 to i32
  %_t16 = alloca i32
  store i32 %r55, i32* %_t16
  %r56 = load i32, i32* %_t15
  %r57 = load i32, i32* %_t16
  %r58 = and i32 %r56, %r57
  %_t17 = alloca i32
  store i32 %r58, i32* %_t17
  %r59 = load i32, i32* %_t17
  %r60 = icmp eq i32 %r59, 0
  br i1 %r60, label %L3, label %L_auto_2
L_auto_2:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @msg4, i32 0, i32 0))
  br label %L4
L3:
  %r61 = load double, double* %a
  %r62 = load double, double* %b
  %r63 = fcmp oeq double %r61, %r62
  %r64 = zext i1 %r63 to i32
  %_t18 = alloca i32
  store i32 %r64, i32* %_t18
  %r65 = load double, double* %b
  %r66 = load double, double* %c
  %r67 = fcmp oeq double %r65, %r66
  %r68 = zext i1 %r67 to i32
  %_t19 = alloca i32
  store i32 %r68, i32* %_t19
  %r69 = load i32, i32* %_t18
  %r70 = load i32, i32* %_t19
  %r71 = or i32 %r69, %r70
  %_t20 = alloca i32
  store i32 %r71, i32* %_t20
  %r72 = load double, double* %a
  %r73 = load double, double* %c
  %r74 = fcmp oeq double %r72, %r73
  %r75 = zext i1 %r74 to i32
  %_t21 = alloca i32
  store i32 %r75, i32* %_t21
  %r76 = load i32, i32* %_t20
  %r77 = load i32, i32* %_t21
  %r78 = or i32 %r76, %r77
  %_t22 = alloca i32
  store i32 %r78, i32* %_t22
  %r79 = load i32, i32* %_t22
  %r80 = icmp eq i32 %r79, 0
  br i1 %r80, label %L5, label %L_auto_3
L_auto_3:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([27 x i8], [27 x i8]* @msg5, i32 0, i32 0))
  br label %L6
L5:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([26 x i8], [26 x i8]* @msg6, i32 0, i32 0))
  br label %L6
L6:
  br label %L4
L4:
  br label %L2
L2:
  ret i32 0
}
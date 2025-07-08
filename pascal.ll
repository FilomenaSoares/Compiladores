; LLVM IR gerado pelo compilador Fimly
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@print_fmt = constant [4 x i8] c"%d \00"
@scan_fmt = constant [3 x i8] c"%d\00"

@msg0 = constant [28 x i8] c"Digite um numero inteiro: \0A\00"
@msg1 = constant [42 x i8] c"Erro: numero deve ser maior ou igual a 1.\00"
@msg2 = constant [2 x i8] c" \00"
@msg3 = constant [2 x i8] c"\0A\00"

define i32 @main() {
entry:
  %n = alloca i32
  %i = alloca i32
  %j = alloca i32
  %k = alloca i32
  %valor = alloca i32
  %s = alloca i32
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @msg0, i64 0, i64 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_fmt, i64 0, i64 0), i32* %n)
  %r1 = load i32, i32* %n
  %r2 = icmp slt i32 %r1, 1
  %r3 = zext i1 %r2 to i32
  %_t1 = alloca i32
  store i32 %r3, i32* %_t1
  %r4 = load i32, i32* %_t1
  %r5 = icmp eq i32 %r4, 0
  br i1 %r5, label %L1, label %label1
label1:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([42 x i8], [42 x i8]* @msg1, i64 0, i64 0))
  br label %L2
L1:
  store i32 0, i32* %i
  br label %L3
L3:
  %r6 = load i32, i32* %i
  %r7 = load i32, i32* %n
  %r8 = icmp slt i32 %r6, %r7
  %r9 = zext i1 %r8 to i32
  %_t2 = alloca i32
  store i32 %r9, i32* %_t2
  %r10 = load i32, i32* %_t2
  %r11 = icmp eq i32 %r10, 0
  br i1 %r11, label %L4, label %label2
label2:
  store i32 0, i32* %s
  br label %L5
L5:
  %r12 = load i32, i32* %n
  %r13 = load i32, i32* %i
  %r14 = sub i32 %r12, %r13
  %_t3 = alloca i32
  store i32 %r14, i32* %_t3
  %r15 = load i32, i32* %_t3
  %r16 = sub i32 %r15, 1
  %_t4 = alloca i32
  store i32 %r16, i32* %_t4
  %r17 = load i32, i32* %s
  %r18 = load i32, i32* %_t4
  %r19 = icmp slt i32 %r17, %r18
  %r20 = zext i1 %r19 to i32
  %_t5 = alloca i32
  store i32 %r20, i32* %_t5
  %r21 = load i32, i32* %_t5
  %r22 = icmp eq i32 %r21, 0
  br i1 %r22, label %L6, label %label3
label3:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @msg2, i64 0, i64 0))
  %r23 = load i32, i32* %s
  %r24 = add i32 %r23, 1
  %_t6 = alloca i32
  store i32 %r24, i32* %_t6
  %r25 = load i32, i32* %_t6
  store i32 %r25, i32* %s
  br label %L5
L6:
  store i32 0, i32* %j
  br label %L7
L7:
  %r26 = load i32, i32* %j
  %r27 = load i32, i32* %i
  %r28 = icmp sle i32 %r26, %r27
  %r29 = zext i1 %r28 to i32
  %_t7 = alloca i32
  store i32 %r29, i32* %_t7
  %r30 = load i32, i32* %_t7
  %r31 = icmp eq i32 %r30, 0
  br i1 %r31, label %L8, label %label4
label4:
  store i32 1, i32* %valor
  %r32 = load i32, i32* %j
  %r33 = icmp sgt i32 %r32, 0
  %r34 = zext i1 %r33 to i32
  %_t8 = alloca i32
  store i32 %r34, i32* %_t8
  %r35 = load i32, i32* %_t8
  %r36 = icmp eq i32 %r35, 0
  br i1 %r36, label %L9, label %label5
label5:
  store i32 0, i32* %k
  br label %L10
L10:
  %r37 = load i32, i32* %k
  %r38 = load i32, i32* %j
  %r39 = icmp slt i32 %r37, %r38
  %r40 = zext i1 %r39 to i32
  %_t9 = alloca i32
  store i32 %r40, i32* %_t9
  %r41 = load i32, i32* %_t9
  %r42 = icmp eq i32 %r41, 0
  br i1 %r42, label %L11, label %label6
label6:
  %r43 = load i32, i32* %i
  %r44 = load i32, i32* %k
  %r45 = sub i32 %r43, %r44
  %_t10 = alloca i32
  store i32 %r45, i32* %_t10
  %r46 = load i32, i32* %valor
  %r47 = load i32, i32* %_t10
  %r48 = mul i32 %r46, %r47
  %_t11 = alloca i32
  store i32 %r48, i32* %_t11
  %r49 = load i32, i32* %k
  %r50 = add i32 %r49, 1
  %_t12 = alloca i32
  store i32 %r50, i32* %_t12
  %r51 = load i32, i32* %_t11
  %r52 = load i32, i32* %_t12
  %r53 = sdiv i32 %r51, %r52
  %_t13 = alloca i32
  store i32 %r53, i32* %_t13
  %r54 = load i32, i32* %_t13
  store i32 %r54, i32* %valor
  %r55 = load i32, i32* %k
  %r56 = add i32 %r55, 1
  %_t14 = alloca i32
  store i32 %r56, i32* %_t14
  %r57 = load i32, i32* %_t14
  store i32 %r57, i32* %k
  br label %L10
L11:
  br label %L9
L9:
  %r58 = load i32, i32* %valor
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @print_fmt, i64 0, i64 0), i32 %r58)
  %r59 = load i32, i32* %j
  %r60 = add i32 %r59, 1
  %_t15 = alloca i32
  store i32 %r60, i32* %_t15
  %r61 = load i32, i32* %_t15
  store i32 %r61, i32* %j
  br label %L7
L8:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @msg3, i64 0, i64 0))
  %r62 = load i32, i32* %i
  %r63 = add i32 %r62, 1
  %_t16 = alloca i32
  store i32 %r63, i32* %_t16
  %r64 = load i32, i32* %_t16
  store i32 %r64, i32* %i
  br label %L3
L4:
  br label %L2
L2:
  br label %fim
fim:
  ret i32 0
}
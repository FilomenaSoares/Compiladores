; LLVM IR gerado pelo compilador Fimly
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@print_fmt = constant [4 x i8] c"%d \00"
@scan_fmt = constant [3 x i8] c"%d\00"

@msg0 = constant [33 x i8] c"Digite um valor para o lado a: \0A\00"
@msg1 = constant [33 x i8] c"Digite um valor para o lado b: \0A\00"
@msg2 = constant [33 x i8] c"Digite um valor para o lado c: \0A\00"
@msg3 = constant [18 x i8] c"Medidas invalidas\00"
@msg4 = constant [28 x i8] c"Triangulo equilatero valido\00"
@msg5 = constant [27 x i8] c"Triangulo isosceles valido\00"
@msg6 = constant [26 x i8] c"Triangulo escaleno valido\00"

define i32 @main() {
entry:
  %a = alloca i32
  %b = alloca i32
  %c = alloca i32
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([33 x i8], [33 x i8]* @msg0, i64 0, i64 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_fmt, i64 0, i64 0), i32* %a)
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([33 x i8], [33 x i8]* @msg1, i64 0, i64 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_fmt, i64 0, i64 0), i32* %b)
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([33 x i8], [33 x i8]* @msg2, i64 0, i64 0))
  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_fmt, i64 0, i64 0), i32* %c)
  %r1 = load i32, i32* %a
  %r2 = icmp sle i32 %r1, 0
  %r3 = zext i1 %r2 to i32
  %_t1 = alloca i32
  store i32 %r3, i32* %_t1
  %r4 = load i32, i32* %_t1
  %r5 = icmp eq i32 %r4, 0
  br i1 %r5, label %L1, label %label1
label1:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([18 x i8], [18 x i8]* @msg3, i64 0, i64 0))
  br label %L2
L1:
  %r6 = load i32, i32* %a
  %r7 = load i32, i32* %b
  %r8 = icmp eq i32 %r6, %r7
  %r9 = zext i1 %r8 to i32
  %_t2 = alloca i32
  store i32 %r9, i32* %_t2
  %r10 = load i32, i32* %_t2
  %r11 = icmp eq i32 %r10, 0
  br i1 %r11, label %L3, label %label2
label2:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([28 x i8], [28 x i8]* @msg4, i64 0, i64 0))
  br label %L4
L3:
  %r12 = load i32, i32* %a
  %r13 = load i32, i32* %b
  %r14 = icmp eq i32 %r12, %r13
  %r15 = zext i1 %r14 to i32
  %_t3 = alloca i32
  store i32 %r15, i32* %_t3
  %r16 = load i32, i32* %_t3
  %r17 = icmp eq i32 %r16, 0
  br i1 %r17, label %L5, label %label3
label3:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([27 x i8], [27 x i8]* @msg5, i64 0, i64 0))
  br label %L6
L5:
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([26 x i8], [26 x i8]* @msg6, i64 0, i64 0))
  br label %L6
L6:
  br label %L4
L4:
  br label %L2
L2:
  br label %fim
fim:
  ret i32 0
}
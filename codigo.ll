; LLVM IR gerado pelo compilador Fimly
declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)
@print_fmt = constant [4 x i8] c"%d\0A\00"
@scan_fmt = constant [3 x i8] c"%d\00"

define i32 @main() {
entry:
%valor = alloca i32
%a = alloca i32
%b = alloca i32
@msg0 = constant [24 x i8] c"Digite um para a valor:\00"
call i32 (i8*, ...) @printf(i8* getelementptr ([24 x i8], [24 x i8]* @msg0, i32 0, i32 0))
call i32 (i8*, ...) @scanf(i8* getelementptr ([3 x i8], [3 x i8]* @scan_fmt, i32 0, i32 0), i32* %a)
@msg0 = constant [24 x i8] c"Digite um para b valor:\00"
call i32 (i8*, ...) @printf(i8* getelementptr ([24 x i8], [24 x i8]* @msg0, i32 0, i32 0))
call i32 (i8*, ...) @scanf(i8* getelementptr ([3 x i8], [3 x i8]* @scan_fmt, i32 0, i32 0), i32* %b)
%r1 = load i32, i32* %a
%r2 = load i32, i32* %b
%r3 = add i32 %r1, %r2
store i32 %r3, i32* %valor
%r4 = load i32, i32* %valor
call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @print_fmt, i32 0, i32 0), i32 %r4)
ret i32 0
}
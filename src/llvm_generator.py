class LLVMGenerator:
    def __init__(self, tac_instructions):
        self.instructions = tac_instructions
        self.llvm_code = []
        self.reg_counter = 0
        self.var_map = {}
        self.labels_defined = set()
        self.block_count = 0
        self.string_constants = {}  # {literal_str: (label_name, size)}

    def new_reg(self):
        self.reg_counter += 1
        return f"%r{self.reg_counter}"

    def new_label(self):
        self.block_count += 1
        return f"label{self.block_count}"

    def emit(self, code_line):
        self.llvm_code.append(code_line)

    def generate(self):
        # 1) Coletar todas as strings constantes (strings usadas no PRINT)
        self.collect_string_constants()

        # 2) Emitir cabeçalho e declarações externas
        self.emit_header()

        # 3) Emitir as constantes globais (strings)
        self.emit_constants()

        # 4) Emitir a função main com as instruções
        self.emit_main()

        # 5) Retorna o código LLVM gerado como string
        return "\n".join(self.llvm_code)

    def collect_string_constants(self):
        # Percorre as instruções para coletar strings usadas no PRINT
        for instr in self.instructions:
            if instr.opcode == "PRINT":
                val = instr.args[0]
                if val.value.startswith('"') and val.value.endswith('"'):
                    if val.value not in self.string_constants:
                        label_name = f"@msg{len(self.string_constants)}"
                        tamanho = len(val.value.strip('"')) + 1
                        self.string_constants[val.value] = (label_name, tamanho)

    def emit_header(self):
        self.emit("; LLVM IR gerado pelo compilador Fimly")
        self.emit("declare i32 @printf(i8*, ...)")
        self.emit("declare i32 @scanf(i8*, ...)")
        self.emit('@print_fmt = constant [4 x i8] c"%d\\0A\\00"')  # "%d\n"
        self.emit('@scan_fmt = constant [3 x i8] c"%d\\00"')       # "%d"
        self.emit("")

    def emit_constants(self):
        # Emite todas as strings constantes no escopo global, antes do main
        for raw_str, (label_name, size) in self.string_constants.items():
            mensagem = raw_str.strip('"').replace('\\n', '\\0A').replace('%', '%%')
            self.emit(f'{label_name} = constant [{size} x i8] c"{mensagem}\\00"')
        self.emit("")

    def emit_main(self):
        self.emit("define i32 @main() {")
        self.emit("entry:")
        for instr in self.instructions:
            self.handle_instr(instr)
        self.emit("ret i32 0")
        self.emit("}")

    def handle_instr(self, instr):
        op = instr.opcode
        args = instr.args

        if op == "DECL":
            var_name = args[0].value
            if var_name not in self.var_map:
                self.emit(f"%{var_name} = alloca i32")
                self.var_map[var_name] = f"%{var_name}"

        elif op == "ASSIGN":
            dest = args[0].value
            src = args[1]
            if src.value.isdigit():
                self.emit(f"store i32 {src.value}, i32* {self.var_map[dest]}")
            else:
                src_reg = self.load_var(src.value)
                self.emit(f"store i32 {src_reg}, i32* {self.var_map[dest]}")

        elif op in ['+', '-', '*', '/']:
            dest = args[0].value
            left = args[1]
            right = args[2]
            left_reg = left.value if left.value.isdigit() else self.load_var(left.value)
            right_reg = right.value if right.value.isdigit() else self.load_var(right.value)
            res_reg = self.new_reg()
            if op == '+':
                self.emit(f"{res_reg} = add i32 {left_reg}, {right_reg}")
            elif op == '-':
                self.emit(f"{res_reg} = sub i32 {left_reg}, {right_reg}")
            elif op == '*':
                self.emit(f"{res_reg} = mul i32 {left_reg}, {right_reg}")
            elif op == '/':
                self.emit(f"{res_reg} = sdiv i32 {left_reg}, {right_reg}")
            if dest in self.var_map:
                self.emit(f"store i32 {res_reg}, i32* {self.var_map[dest]}")
            else:
                self.var_map[dest] = res_reg

        elif op in ['<', '<=', '>', '>=', '==', '!=']:
            dest = args[0].value
            left = args[1]
            right = args[2]
            left_reg = left.value if left.value.isdigit() else self.load_var(left.value)
            right_reg = right.value if right.value.isdigit() else self.load_var(right.value)
            cmp_reg = self.new_reg()
            llvm_op = {
                '<': 'slt', '<=': 'sle', '>': 'sgt',
                '>=': 'sge', '==': 'eq', '!=': 'ne'
            }[op]
            self.emit(f"{cmp_reg} = icmp {llvm_op} i32 {left_reg}, {right_reg}")
            bool_reg = self.new_reg()
            self.emit(f"{bool_reg} = zext i1 {cmp_reg} to i32")
            self.var_map[dest] = bool_reg

        elif op == "PRINT":
            val = args[0]
            if val.value.isdigit():
                self.emit(f"call i32 (i8*, ...) @printf(i8* getelementptr "
                          f"([4 x i8], [4 x i8]* @print_fmt, i32 0, i32 0), i32 {val.value})")

            elif val.value.startswith('"') and val.value.endswith('"'):
                label_name, tamanho = self.string_constants[val.value]
                self.emit(f"call i32 (i8*, ...) @printf(i8* getelementptr "
                          f"([{tamanho} x i8], [{tamanho} x i8]* {label_name}, i32 0, i32 0))")

            else:
                val_reg = self.load_var(val.value)
                self.emit(f"call i32 (i8*, ...) @printf(i8* getelementptr "
                          f"([4 x i8], [4 x i8]* @print_fmt, i32 0, i32 0), i32 {val_reg})")

        elif op == "READ":
            var = args[0].value
            self.emit(f"call i32 (i8*, ...) @scanf(i8* getelementptr "
                      f"([3 x i8], [3 x i8]* @scan_fmt, i32 0, i32 0), i32* {self.var_map[var]})")

        elif op == "LABEL":
            label = args[0]
            if label not in self.labels_defined:
                self.emit(f"{label}:")
                self.labels_defined.add(label)

        elif op == "GOTO":
            label = args[0]
            self.emit(f"br label %{label}")

        elif op == "IF_FALSE_GOTO":
            cond_var = args[0].value
            label = args[1]
            cond_reg = self.load_var(cond_var)
            cmp_reg = self.new_reg()
            self.emit(f"{cmp_reg} = icmp eq i32 {cond_reg}, 0")
            next_label = self.new_label()
            self.emit(f"br i1 {cmp_reg}, label %{label}, label %{next_label}")
            self.emit(f"{next_label}:")

        else:
            self.emit(f"; Instrução não implementada: {op}")

    def load_var(self, var_name):
        if var_name in self.var_map and self.var_map[var_name].startswith('%r'):
            return self.var_map[var_name]
        reg = self.new_reg()
        self.emit(f"{reg} = load i32, i32* {self.var_map[var_name]}")
        return reg

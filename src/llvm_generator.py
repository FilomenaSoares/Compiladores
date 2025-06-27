class LLVMGenerator:
    def __init__(self, tac_instructions):
        self.instructions = tac_instructions
        self.llvm_code = []
        self.reg_counter = 0
        self.var_map = {}        # Mapeia variáveis do TAC para endereços (alloca)
        self.labels_defined = set()
        self.block_stack = []
        self.block_count = 0

    def new_reg(self):
        self.reg_counter += 1
        return f"%r{self.reg_counter}"

    def new_label(self):
        self.block_count += 1
        return f"label{self.block_count}"

    def emit(self, code_line):
        self.llvm_code.append(code_line)

    def generate(self):
        self.emit_header()
        self.emit_main()
        return "\n".join(self.llvm_code)

    def emit_header(self):
        self.emit("; LLVM IR gerado pelo compilador Fimly")
        self.emit("declare i32 @printf(i8*, ...)")
        self.emit("declare i32 @scanf(i8*, ...)")
        self.emit('@print_fmt = constant [4 x i8] c"%d\\0A\\00"')  # "%d\n"
        self.emit('@scan_fmt = constant [3 x i8] c"%d\\00"')       # "%d"
        self.emit("")
        self.emit("define i32 @main() {")
        self.emit("entry:")

    def emit_main(self):
        # Aqui processamos todas as instruções TAC sequencialmente
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
                # Aloca variável local (stack)
                self.emit(f"%{var_name} = alloca i32")
                self.var_map[var_name] = f"%{var_name}"

        elif op == "ASSIGN":
            dest = args[0].value
            src = args[1]

            if src.value.isdigit():
                # Valor literal direto
                self.emit(f"store i32 {src.value}, i32* {self.var_map[dest]}")
            else:
                # Variável ou temporário
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

            # Se for variável declarada, faça store
            if dest in self.var_map:
                self.emit(f"store i32 {res_reg}, i32* {self.var_map[dest]}")
            else:
                # Se dest é temporário, mapeie para o registrador res_reg para uso futuro
                # Por exemplo, crie um mapa temporário de temporários para regs
                self.var_map[dest] = res_reg

        elif op == "PRINT":
            val = args[0]
            if val.value.isdigit():
                self.emit(f"call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @print_fmt, i32 0, i32 0), i32 {val.value})")
            elif val.value.startswith('"') and val.value.endswith('"'):
            # Trata string literal
                mensagem = val.value.strip('"').replace('\\n', '\\0A').replace('%', '%%')
                label_name = f"@msg{self.reg_counter}"
                tamanho = len(mensagem) + 1
                self.emit(f'{label_name} = constant [{tamanho} x i8] c"{mensagem}\\00"')
                self.emit(f'call i32 (i8*, ...) @printf(i8* getelementptr ([{tamanho} x i8], [{tamanho} x i8]* {label_name}, i32 0, i32 0))')
            else:
        # Variável
                val_reg = self.load_var(val.value)
                self.emit(f"call i32 (i8*, ...) @printf(i8* getelementptr ([4 x i8], [4 x i8]* @print_fmt, i32 0, i32 0), i32 {val_reg})")

        elif op == "READ":
            var = args[0].value
            self.emit(f"call i32 (i8*, ...) @scanf(i8* getelementptr ([3 x i8], [3 x i8]* @scan_fmt, i32 0, i32 0), i32* {self.var_map[var]})")

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

            # Compara cond == 0 (falso)
            self.emit(f"{cmp_reg} = icmp eq i32 {cond_reg}, 0")

            # Necessário criar label para o "else" (continuação) para o branch condicional
            else_label = self.new_label()

            self.emit(f"br i1 {cmp_reg}, label %{label}, label %{else_label}")
            self.emit(f"{else_label}:")  # Label para o fluxo se cond != 0

        else:
            self.emit(f"; Instrução não implementada: {op}")

    def load_var(self, var_name):
    # Se for temporário já armazenado em reg, retorna direto
        if var_name in self.var_map and self.var_map[var_name].startswith('%r'):
            return self.var_map[var_name]
        # Se for variável declarada, faça load da stack
        reg = self.new_reg()
        self.emit(f"{reg} = load i32, i32* {self.var_map[var_name]}")
        return reg

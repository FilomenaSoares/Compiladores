class LLVMGenerator:
    def __init__(self, tac_instructions):
        self.instructions = tac_instructions
        self.llvm_code = []
        self.reg_counter = 0
        self.var_map = {}
        self.labels_defined = set()
        self.block_count = 0
        self.string_constants = {}

    def new_reg(self):
        self.reg_counter += 1
        return f"%r{self.reg_counter}"

    def new_label(self):
        self.block_count += 1
        return f"label{self.block_count}"

    def emit(self, code_line):
        self.llvm_code.append(code_line)

    def generate(self):
        self.collect_string_constants()
        self.emit_header()
        self.emit_constants()
        self.emit_main()
        return "\n".join(self.llvm_code)

    def collect_string_constants(self):
        for instr in self.instructions:
            if instr.opcode == "PRINT":
                val = instr.args[0]
                if hasattr(val, 'value') and isinstance(val.value, str) and val.value.startswith('"'):
                    if val.value not in self.string_constants:
                        raw = val.value.strip('"')
                        mensagem = raw.replace('%', '%%')
                        mensagem_bytes = bytes(mensagem, "utf-8").decode("unicode_escape").encode("latin1")
                        tamanho = len(mensagem_bytes) + 1
                        label_name = f"@msg{len(self.string_constants)}"
                        self.string_constants[val.value] = (label_name, tamanho)

    def emit_header(self):
        self.emit("; LLVM IR gerado pelo compilador Fimly")
        self.emit("declare i32 @printf(i8*, ...)")
        self.emit("declare i32 @scanf(i8*, ...)")
        self.emit('@print_fmt = constant [4 x i8] c"%d \\00"')
        self.emit('@scan_fmt = constant [3 x i8] c"%d\\00"')
        self.emit("")

    def emit_constants(self):
        for raw_str, (label_name, size) in self.string_constants.items():
            mensagem = raw_str.strip('"').replace('\\n', '\\0A').replace('%', '%%')
            self.emit(f'{label_name} = constant [{size} x i8] c"{mensagem}\\00"')
        self.emit("")

    def emit_main(self):
        self.emit("define i32 @main() {")
        self.emit("entry:")
        
        for instr in self.instructions:
            self.handle_instr(instr)

        # Após o loop, se o último bloco não foi fechado, feche-o agora.
        if self.llvm_code and not self.llvm_code[-1].strip().startswith(('br ', 'ret ')):
            self.emit("  br label %fim")

        if "fim" not in self.labels_defined:
            self.emit("fim:")
        
        self.emit("  ret i32 0")
        self.emit("}")

    def handle_instr(self, instr):
        op = instr.opcode
        args = instr.args

        def get_value(arg):
            return arg.value if hasattr(arg, 'value') else arg

        # Lógica de terminação de bloco: se a instrução atual é um label e o bloco anterior
        # não foi fechado com 'br' ou 'ret', nós o fechamos agora com um salto para este label.
        if op == 'LABEL':
            if self.llvm_code and not self.llvm_code[-1].strip().startswith(('br ', 'ret ')):
                 self.emit(f"  br label %{get_value(args[0])}")
        
        if op == "DECL":
            var_name = get_value(args[0])
            if var_name not in self.var_map:
                self.emit(f"  %{var_name} = alloca i32")
                self.var_map[var_name] = f"%{var_name}"

        elif op == "ASSIGN":
            dest = get_value(args[0])
            src_val = get_value(args[1])
            if dest not in self.var_map:
                self.emit(f"  %{dest} = alloca i32")
                self.var_map[dest] = f"%{dest}"
            
            if str(src_val).isdigit() or (str(src_val).startswith('-') and str(src_val)[1:].isdigit()):
                self.emit(f"  store i32 {src_val}, i32* {self.var_map[dest]}")
            else:
                src_reg = self.load_var(src_val)
                self.emit(f"  store i32 {src_reg}, i32* {self.var_map[dest]}")

        elif op in ['+', '-', '*', '/']:
            dest = get_value(args[0])
            left_val = get_value(args[1])
            right_val = get_value(args[2])
            
            left_reg = str(left_val) if str(left_val).isdigit() else self.load_var(left_val)
            right_reg = str(right_val) if str(right_val).isdigit() else self.load_var(right_val)
            
            res_reg = self.new_reg()
            llvm_op = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'sdiv'}[op]
            self.emit(f"  {res_reg} = {llvm_op} i32 {left_reg}, {right_reg}")
            
            if dest not in self.var_map:
                self.emit(f"  %{dest} = alloca i32")
                self.var_map[dest] = f"%{dest}"
            self.emit(f"  store i32 {res_reg}, i32* {self.var_map[dest]}")

        elif op in ['<', '<=', '>', '>=', '==', '!=']:
            dest = get_value(args[0])
            left_val = get_value(args[1])
            right_val = get_value(args[2])
            
            left_reg = str(left_val) if str(left_val).isdigit() else self.load_var(left_val)
            right_reg = str(right_val) if str(right_val).isdigit() else self.load_var(right_val)

            cmp_reg = self.new_reg()
            llvm_op = {'<': 'slt', '<=': 'sle', '>': 'sgt', '>=': 'sge', '==': 'eq', '!=': 'ne'}[op]
            self.emit(f"  {cmp_reg} = icmp {llvm_op} i32 {left_reg}, {right_reg}")
            
            bool_reg = self.new_reg()
            self.emit(f"  {bool_reg} = zext i1 {cmp_reg} to i32")
            if dest not in self.var_map:
                self.emit(f"  %{dest} = alloca i32")
                self.var_map[dest] = f"%{dest}"
            self.emit(f"  store i32 {bool_reg}, i32* {self.var_map[dest]}")

        elif op == "PRINT":
            val = get_value(args[0])
            if str(val).isdigit():
                self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @print_fmt, i64 0, i64 0), i32 {val})')
            elif isinstance(val, str) and val.startswith('"'):
                label_name, tamanho = self.string_constants[val]
                self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([{tamanho} x i8], [{tamanho} x i8]* {label_name}, i64 0, i64 0))')
            else:
                val_reg = self.load_var(val)
                self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @print_fmt, i64 0, i64 0), i32 {val_reg})')

        elif op == "READ":
            var = get_value(args[0])
            if var not in self.var_map:
                self.emit(f"  %{var} = alloca i32")
                self.var_map[var] = f"%{var}"
            self.emit(f'  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_fmt, i64 0, i64 0), i32* {self.var_map[var]})')

        elif op == "LABEL":
            label = get_value(args[0])
            if label not in self.labels_defined:
                self.emit(f"{label}:")
                self.labels_defined.add(label)

        elif op == "GOTO":
            label = get_value(args[0])
            self.emit(f"  br label %{label}")

        elif op == "IF_FALSE_GOTO":
            cond_var = get_value(args[0])
            label_dest = get_value(args[1])
            
            cond_reg = self.load_var(cond_var)
            cmp_reg = self.new_reg()
            self.emit(f"  {cmp_reg} = icmp eq i32 {cond_reg}, 0")
            next_label = self.new_label()
            self.emit(f"  br i1 {cmp_reg}, label %{label_dest}, label %{next_label}")
            self.emit(f"{next_label}:")
            
        else:
            self.emit(f"; Instrução não implementada: {op}")

    def load_var(self, var_name):
        s_var_name = str(var_name)

            # Se for um registrador temporário, apenas retorne
        if s_var_name.startswith('%'):
            return s_var_name
        
        # --- INÍCIO DA CORREÇÃO ---
        # Se for um número (int ou float), não aloque memória,
        # retorne o próprio número como um valor literal.
        try:
            # Tenta converter para float. Se funcionar, é um número.
            float(s_var_name)
            return s_var_name 
        except ValueError:
            # Se falhar, não é um número, então é um nome de variável. Continue.
            pass
        # --- FIM DA CORREÇÃO ---
            
        # Se a variável ainda não foi alocada, aloque agora
        if s_var_name not in self.var_map:
            # ATENÇÃO: Ainda está alocando como i32. Isso será o próximo passo a mudar.
            self.emit(f"  %{s_var_name} = alloca i32") 
            self.var_map[s_var_name] = f"%{s_var_name}"
        
        # Carregue o valor da variável alocada para um registrador
        reg = self.new_reg()
        # ATENÇÃO: Ainda está carregando como i32.
        self.emit(f"  {reg} = load i32, i32* {self.var_map[s_var_name]}") 
        return reg
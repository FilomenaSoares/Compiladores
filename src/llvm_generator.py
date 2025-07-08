# src/llvm_generator.py - VERSÃO FINAL UNIFICADA

class LLVMGenerator:
    def __init__(self, tac_instructions):
        self.instructions = tac_instructions
        self.llvm_code = []
        self.reg_counter = 0
        self.label_count = 0
        
        # Arquitetura correta, consciente dos tipos
        self.var_map = {}
        self.labels_defined = set()
        self.block_terminated = False
        
        # Lógica de strings que funciona no seu ambiente
        self.string_constants = {}

    # --- Funções Auxiliares ---

    def new_reg(self):
        self.reg_counter += 1
        return f"%r{self.reg_counter}"

    def new_label(self):
        self.label_count += 1
        return f"L_auto_{self.label_count}"

    def emit(self, code_line):
        self.llvm_code.append(code_line)

    def get_value(self, arg):
        return arg.value if hasattr(arg, 'value') else arg

    def get_llvm_type(self, type_str):
        if type_str == 'float': return 'double'
        if type_str == 'int': return 'i32'
        return 'i32'

    # --- Lógica Principal de Geração ---

    def generate(self):
        self.collect_string_constants()
        self.emit_header()
        self.emit_constants()
        self.emit_main_function()
        return "\n".join(self.llvm_code)

    # --- Métodos para Strings "Transplantados" da sua versão do Pascal ---
    def collect_string_constants(self):
        for instr in self.instructions:
            for arg in instr.args:
                val = self.get_value(arg)
                if isinstance(val, str) and val.startswith('"'):
                    if val not in self.string_constants:
                        raw = val.strip('"')
                        # Sua lógica de replace e bytes
                        mensagem = raw.replace('%', '%%')
                        mensagem_bytes = bytes(mensagem, "utf-8").decode("unicode_escape").encode("latin1")
                        tamanho = len(mensagem_bytes) + 1
                        label_name = f"@msg{len(self.string_constants)}"
                        self.string_constants[val] = (label_name, tamanho, raw) # Armazenar raw para emit

    def emit_constants(self):
        for raw_str_val, (label_name, size, raw_content) in self.string_constants.items():
            # Sua lógica para formatar a mensagem para LLVM
            mensagem = raw_content.replace('\\n', '\\0A').replace('%', '%%')
            self.emit(f'{label_name} = private unnamed_addr constant [{size} x i8] c"{mensagem}\\00"')
        self.emit("")
    # --- Fim dos métodos transplantados ---

    def emit_header(self):
        self.emit("; LLVM IR Gerado pelo Compilador Fimly")
        self.emit("declare i32 @printf(i8*, ...)")
        self.emit("declare i32 @scanf(i8*, ...)")
        self.emit('@print_int_fmt = private unnamed_addr constant [3 x i8] c"%d\\00"')
        self.emit('@print_float_fmt = private unnamed_addr constant [3 x i8] c"%f\\00"')
        self.emit('@scan_int_fmt = private unnamed_addr constant [3 x i8] c"%d\\00"')
        self.emit('@scan_float_fmt = private unnamed_addr constant [4 x i8] c"%lf\\00"')
        self.emit("")

    def emit_main_function(self):
        self.emit("define i32 @main() {")
        self.emit("entry:")
        self.block_terminated = False
        for instr in self.instructions:
            self.handle_instr(instr)
        if not self.block_terminated:
            self.emit("  ret i32 0")
        self.emit("}")

    # --- Manipuladores de Instrução (Versão Moderna e Consciente de Tipos) ---

    def get_operand_type_and_val(self, operand):
        val = self.get_value(operand)
        if str(val) in self.var_map:
            var_info = self.var_map[str(val)]
            reg = self.new_reg()
            self.emit(f"  {reg} = load {var_info['type']}, {var_info['type']}* {var_info['ptr']}")
            return var_info['type'], reg
        try:
            float(val)
            return ("double" if "." in str(val) else "i32"), str(val)
        except (ValueError, TypeError):
            return "ptr", val

    def cast_if_needed(self, reg, from_type, to_type):
        if from_type == to_type: return reg
        cast_reg = self.new_reg()
        if from_type == 'i32' and to_type == 'double': self.emit(f"  {cast_reg} = sitofp i32 {reg} to double")
        elif from_type == 'double' and to_type == 'i32': self.emit(f"  {cast_reg} = fptosi double {reg} to i32")
        else: return reg
        return cast_reg

    def handle_instr(self, instr):
        op, args = instr.opcode, instr.args

        if op in ["GOTO", "LABEL", "IF_FALSE_GOTO"]:
            if op == "LABEL":
                label = self.get_value(args[0])
                if not self.block_terminated: self.emit(f"  br label %{label}")
                if label not in self.labels_defined:
                    self.emit(f"{label}:")
                    self.labels_defined.add(label)
                self.block_terminated = False
            elif op == "GOTO":
                if not self.block_terminated: self.emit(f"  br label %{self.get_value(args[0])}")
                self.block_terminated = True
            elif op == "IF_FALSE_GOTO":
                if not self.block_terminated:
                    cond_type, cond_val = self.get_operand_type_and_val(args[0])
                    label_dest = self.get_value(args[1])
                    cmp_reg, next_label = self.new_reg(), self.new_label()
                    self.emit(f"  {cmp_reg} = icmp eq {cond_type} {cond_val}, 0")
                    self.emit(f"  br i1 {cmp_reg}, label %{label_dest}, label %{next_label}")
                    self.emit(f"{next_label}:")
                self.block_terminated = False
            return
        
        if self.block_terminated: return

        if op == "DECL":
            var_name = self.get_value(args[0])
            llvm_type = self.get_llvm_type(self.get_value(args[1]))
            if var_name not in self.var_map:
                ptr = f"%{var_name}"
                self.emit(f"  {ptr} = alloca {llvm_type}")
                self.var_map[var_name] = {'ptr': ptr, 'type': llvm_type}

        elif op == "ASSIGN":
            dest_name, src_operand = self.get_value(args[0]), args[1]
            dest_info = self.var_map[dest_name]
            src_type, src_val = self.get_operand_type_and_val(src_operand)
            src_reg = self.cast_if_needed(src_val, src_type, dest_info['type'])
            self.emit(f"  store {dest_info['type']} {src_reg}, {dest_info['type']}* {dest_info['ptr']}")

        elif op in ['+', '-', '*', '/', '&&', '||', '<', '<=', '>', '>=', '==', '!=']:
            dest_name, left, right = (self.get_value(a) for a in args)
            left_type, left_val = self.get_operand_type_and_val(left)
            right_type, right_val = self.get_operand_type_and_val(right)
            
            is_float = 'double' in [left_type, right_type]
            op_type = 'double' if is_float else 'i32'
            left_reg, right_reg = self.cast_if_needed(left_val, left_type, op_type), self.cast_if_needed(right_val, right_type, op_type)
            res_reg = self.new_reg()

            if op in ['+', '-', '*', '/']:
                op_map = ({'+': 'fadd', '-': 'fsub', '*': 'fmul', '/': 'fdiv'} if is_float else
                          {'+': 'add', '-': 'sub', '*': 'mul', '/': 'sdiv'})
                self.emit(f"  {res_reg} = {op_map[op]} {op_type} {left_reg}, {right_reg}")
                if dest_name not in self.var_map:
                    self.var_map[dest_name] = {'ptr': f'%{dest_name}', 'type': op_type}
                    self.emit(f"  %{dest_name} = alloca {op_type}")
                self.emit(f"  store {op_type} {res_reg}, {op_type}* {self.var_map[dest_name]['ptr']}")
            else:
                is_logic = op in ['&&', '||']
                if is_logic:
                    op_map = {'&&': 'and', '||': 'or'}
                    self.emit(f"  {res_reg} = {op_map[op]} i32 {left_reg}, {right_reg}")
                else: # Comparações
                    op_map = ({'<': 'olt', '<=': 'ole', '>': 'ogt', '>=': 'oge', '==': 'oeq', '!=': 'one'} if is_float else
                              {'<': 'slt', '<=': 'sle', '>': 'sgt', '>=': 'sge', '==': 'eq', '!=': 'ne'})
                    self.emit(f"  {res_reg} = {'fcmp' if is_float else 'icmp'} {op_map[op]} {op_type} {left_reg}, {right_reg}")
                
                final_res = res_reg
                if not is_logic:
                    bool_reg = self.new_reg()
                    self.emit(f"  {bool_reg} = zext i1 {res_reg} to i32")
                    final_res = bool_reg
                
                if dest_name not in self.var_map:
                    self.var_map[dest_name] = {'ptr': f'%{dest_name}', 'type': 'i32'}
                    self.emit(f"  %{dest_name} = alloca i32")
                self.emit(f"  store i32 {final_res}, i32* {self.var_map[dest_name]['ptr']}")

        elif op == "PRINT":
            for arg in args:
                val_type, val_reg = self.get_operand_type_and_val(arg)
                if val_type == 'i32':
                    self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @print_int_fmt, i32 0, i32 0), i32 {val_reg})')
                elif val_type == 'double':
                    self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @print_float_fmt, i32 0, i32 0), double {val_reg})')
                elif val_type == 'ptr':
                    # Usando a lógica de string que funciona para você
                    label_name, tamanho, _ = self.string_constants[self.get_value(arg)]
                    self.emit(f'  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([{tamanho} x i8], [{tamanho} x i8]* {label_name}, i32 0, i32 0))')

        elif op == "READ":
            var_name = self.get_value(args[0])
            var_info = self.var_map[var_name]
            if var_info['type'] == 'i32':
                self.emit(f'  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @scan_int_fmt, i32 0, i32 0), i32* {var_info["ptr"]})')
            elif var_info['type'] == 'double':
                self.emit(f'  call i32 (i8*, ...) @scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @scan_float_fmt, i32 0, i32 0), double* {var_info["ptr"]})')
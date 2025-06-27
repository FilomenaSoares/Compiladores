from abc import ABC, abstractmethod

# Classe para representar os operandos das instruções TAC
class TACOperand:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

# Classe para representar uma instrução TAC
class TACInstruction:
    def __init__(self, opcode: str, *args):
        self.opcode = opcode
        self.args = args

    def __repr__(self):
        op = self.opcode
        args = self.args

        if op in ['+', '-', '*', '/', '<', '<=', '>', '>=', '==', '!=']:
            return f"{args[0]} = {args[1]} {op} {args[2]}"

        if op == 'ASSIGN':
            return f"{args[0]} = {args[1]}"

        if op == 'GOTO':
            return f"GOTO {args[0]}"

        if op == 'IF_FALSE_GOTO':
            return f"IF_FALSE {args[0]} GOTO {args[1]}"

        if op == 'LABEL':
            return f"{args[0]}:"

        # Padrão para outras instruções como 'CALL', 'PRINT', etc.
        return f"{op} " + ", ".join(map(str, args))

# Interface Visitor
class Visitor(ABC):
    @abstractmethod
    def visit(self, node):
        pass

# Gerador de código intermediário (Three Address Code)
class GeradorDeCodigoIntermediario(Visitor):
    def __init__(self):
        self.temp_counter = 0
        self.label_counter = 0
        self.instructions = []

    def new_temp(self):
        self.temp_counter += 1
        return TACOperand(f"_t{self.temp_counter}")
    
    def new_label(self):
        self.label_counter += 1
        return f"L{self.label_counter}"

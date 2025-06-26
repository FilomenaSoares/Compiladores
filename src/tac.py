# tac.py
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
        # Formatação inteligente baseada no opcode
        op = self.opcode
        args = self.args

        if op in ['+', '-', '*', '/']:
            # Ex: _t0 = _t1 + _t2
            return f"{args[0]} = {args[1]} {op} {args[2]}"
        
        if op == 'ASSIGN':
            # Ex: x = _t0
            return f"{args[0]} = {args[1]}"

        if op == 'GOTO':
            # Ex: GOTO L1
            return f"GOTO {args[0]}"

        if op == 'IF_FALSE_GOTO':
            # Ex: IF_FALSE _t0 GOTO L2
            return f"IF_FALSE {args[0]} GOTO {args[1]}"
        
        if op == 'LABEL':
            # Ex: L3:
            return f"{args[0]}:"
        
        # Caso padrão (pode ser usado para print, call, etc.)
        return f"{op} " + ", ".join(map(str, args))

# Interface Visitor
class Visitor(ABC):
    @abstractmethod
    def visit(self, node):
        pass

# Classe que implementa o Visitor para geração de código intermediário
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
        return TACOperand(f"L{self.label_counter}")
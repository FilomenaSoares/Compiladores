from abc import ABC, abstractmethod

# Classe para representar os operandos das instruções TAC
class TACOperand:
    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return self.value

# Classe para representar uma instrução TAC
class TACInstruction:
    def __init__(self, opcode: str, destino: TACOperand, *argumentos: TACOperand):
        self.opcode = opcode
        self.destino = destino
        self.argumentos = argumentos

    def __repr__(self):
        args = ', '.join(map(str, self.argumentos))
        return f"{self.destino} = {self.opcode} {args}"

# Interface Visitor
class Visitor(ABC):
    @abstractmethod
    def visit(self, node):
        pass

# Classe que implementa o Visitor para geração de código intermediário
class GeradorDeCodigoIntermediario(Visitor):
    def __init__(self):
        self.temp_counter = 0
        self.instructions = []

    def new_temp(self):
        self.temp_counter += 1
        return TACOperand(f"_t{self.temp_counter}")

class Expressao:
    pass

class ExpressaoBinaria(Expressao):
    def __init__(self, esquerda, operador, direita):
        self.esquerda = esquerda
        self.operador = operador
        self.direita = direita

class ExpressaoUnaria(Expressao):
    def __init__(self, operador, expressao):
        self.operador = operador
        self.expressao = expressao

class Identificador(Expressao):
    def __init__(self, nome):
        self.nome = nome

    def visit(self, node):
        if isinstance(node, ExpressaoBinaria):
            return self.visit_binaria(node)
        elif isinstance(node, ExpressaoUnaria):
            return self.visit_unaria(node)
        elif isinstance(node, Identificador):
            return self.visit_identificador(node)
        # Adicionar outros tipos conforme necessário

    def visit_binaria(self, node):
        left = self.visit(node.esquerda)
        right = self.visit(node.direita)
        temp = self.new_temp()
        self.instructions.append(TACInstruction(node.operador, temp, left, right))
        return temp

    def visit_unaria(self, node):
        expr = self.visit(node.expressao)
        temp = self.new_temp()
        self.instructions.append(TACInstruction(node.operador, temp, expr))
        return temp

    def visit_identificador(self, node):
        return TACOperand(node.nome)

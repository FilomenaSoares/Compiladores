from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from graphviz import Source

class ASTNode(Node):
    pass

class ASTVisualizer:
    def __init__(self, start_node=0):
        self.node_count = start_node

    def create_node(self, label, parent=None):
        node = ASTNode(label, parent=parent)
        self.node_count += 1
        return node

    def render(self, root):
        for pre, fill, node in RenderTree(root):
            print(f"{pre}{node.name}")

    def export_to_dot(self, root, output_path="ast.dot"):
        try:
            DotExporter(root).to_dotfile(output_path)
            print(f"AST exportada para {output_path}.")
        except Exception as e:
            print(f"Erro ao exportar AST para DOT: {e}")

    def generate_png(self, dot_file, output_image="ast.png"):
        try:
            source = Source.from_file(dot_file)
            source.render(output_image, format='png', cleanup=False)
            print(f"Imagem gerada: {output_image}")
        except Exception as e:
            print(f"Erro ao gerar a imagem PNG: {e}")

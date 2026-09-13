from antlr4 import *

from gen.NNGraphLexer import NNGraphLexer
from gen.NNGraphParser import NNGraphParser
from compiler.visitor import ModelVisitor
from compiler.semantic import SemanticAnalyzer
from compiler.codegen import CodeGenerator
from graphviz_export import GraphvizExporter

def main():
    input_stream = FileStream("example1.nng", encoding="utf-8")

    lexer = NNGraphLexer(input_stream)

    tokens = CommonTokenStream(lexer)

    parser = NNGraphParser(tokens)

    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax Error!")
        return
    print("Parse Successful!")
    # print(tree.toStringTree(recog=parser))

    visitor = ModelVisitor()
    visitor.visit(tree)
    model = visitor.getModel()

    semantic = SemanticAnalyzer(model)

    errors = semantic.analyze()

    print(model)

    if errors:

        print("\nSemantic Errors:")

        for e in errors:
            print("-", e)
        return

    else:

        print("\nSemantic Analysis Successful!")

        generator = CodeGenerator(model)

        generator.save("generated_model.py")
        exporter = GraphvizExporter(model)
        exporter.export("graph.dot")
        import subprocess

        subprocess.run([
            "dot",
            "-Tpng",
            "graph.dot",
            "-o",
            "graph.png"
        ])

        print("GraphViz file generated successfully.")

        print("PyTorch code generated successfully.")

if __name__ == "__main__":
    main()
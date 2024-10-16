import sys
from antlr4 import *
from MapGrammarLexer import MapGrammarLexer
from MapGrammarParser import MapGrammarParser

class MyVisitor(ParseTreeVisitor):
    def visitMapFunction(self, ctx):
        function_name = ctx.function().getText()
        iterable = ctx.iterable().getText()
        print(f"Applying function '{function_name}' to iterable '{iterable}'")
        # Aquí puedes implementar la lógica para ejecutar la función sobre el iterable

    # Implementa otros métodos de visita según lo necesites

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = MapGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MapGrammarParser(stream)
    tree = parser.program()  # Inicia el análisis a partir de la regla 'program'
    
    visitor = MyVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()


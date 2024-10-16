import sys
from antlr4 import *
from ComplexNumberLexer import ComplexNumberLexer
from ComplexNumberParser import ComplexNumberParser

def main():
    input_stream = InputStream(input("Ingresa una expresión de números complejos: "))
    lexer = ComplexNumberLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ComplexNumberParser(stream)
    
    # Parsear la expresión
    tree = parser.expr()

    # Aquí podrías implementar un método para evaluar el árbol de parseo
    # Evaluar(tree)

if __name__ == '__main__':
    main()


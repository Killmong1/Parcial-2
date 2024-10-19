import sys
from antlr4 import *
from ComplexLexer import ComplexLexer
from ComplexParser import ComplexParser
from ComplexVisitor import ComplexVisitor  # Importar el visitor generado por ANTLR

# Clase para recorrer el árbol generado por el parser
class MyComplexVisitor(ComplexVisitor):  # Extiende del visitor generado
    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expr(0))  # Visitamos la subexpresión izquierda
        right = self.visit(ctx.expr(1))  # Visitamos la subexpresión derecha
        print(f"Add: {left} + {right}")  # Depuración
        return left + right

    def visitSubtractExpr(self, ctx):
        left = self.visit(ctx.expr(0))  # Visitamos la subexpresión izquierda
        right = self.visit(ctx.expr(1))  # Visitamos la subexpresión derecha
        print(f"Subtract: {left} - {right}")  # Depuración
        return left - right

    def visitMultiplyExpr(self, ctx):
        left = self.visit(ctx.expr(0))  # Visitamos la subexpresión izquierda
        right = self.visit(ctx.expr(1))  # Visitamos la subexpresión derecha
        print(f"Multiply: {left} * {right}")  # Depuración
        return left * right

    def visitParenExpr(self, ctx):
        result = self.visit(ctx.expr())  # Evaluamos la expresión entre paréntesis
        print(f"Paren: ({result})")  # Depuración
        return result

    def visitComplexExpr(self, ctx):
        real = int(ctx.complexNumber().REAL().getText())  # Parte real
        imaginary = 0
        if ctx.complexNumber().IMAGINARY():
            imaginary = int(ctx.complexNumber().IMAGINARY().getText()[:-1])  # Quitamos la 'i'
        complex_value = complex(real, imaginary)
        print(f"Complex: {complex_value}")  # Depuración
        return complex_value  # Retornamos el número complejo

# Función principal para procesar una expresión
def main(input_text):
    input_stream = InputStream(input_text)
    lexer = ComplexLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ComplexParser(token_stream)
    tree = parser.expr()

    visitor = MyComplexVisitor()
    result = visitor.visit(tree)  # Visita el árbol para evaluar la expresión
    print("Resultado:", result)  # Resultado final

if __name__ == '__main__':
    # Prueba con una expresión de números complejos
    input_text = '(8 + 9i) + (6 - 5i)'  # Puedes cambiar esta expresión
    main(input_text)

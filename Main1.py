import sys
from antlr4 import *
from punto1Lexer import punto1Lexer
from punto1Parser import punto1Parser
from punto1Visitor import punto1Visitor

class MyComplexVisitor(punto1Visitor):
    def __init__(self):
        self.variables = {'j': complex(0, 1)}  # Definimos 'j' como 0 + 1j
        self.operations = []  # Para guardar las operaciones realizadas

    def visitAddExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left + right
        operation = f"({self.format_output(left)}) + ({self.format_output(right)})"
        self.operations.append(operation)
        print(f"Operación: {operation} = {self.format_output(result)}")
        return result

    def visitSubtractExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        result = left - right
        operation = f"({self.format_output(left)}) - ({self.format_output(right)})"
        self.operations.append(operation)
        print(f"Operación: {operation} = {self.format_output(result)}")
        return result

    def visitMultiplyExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))

        # Si ambos lados son variables o complejos, mostrar como j^2 o similar
        if isinstance(left, str) and left == 'j' and isinstance(right, str) and right == 'j':
            result = 'j^2'
            operation = f"({left}) * ({right})"
        elif isinstance(left, str) and isinstance(right, str):
            result = f"({left}) * ({right})"  # Mostrar como expresión
            operation = result
        else:
            result = left * right
            operation = f"({self.format_output(left)}) * ({self.format_output(right)})"
        
        self.operations.append(operation)
        print(f"Operación: {operation} = {self.format_output(result)}")
        return result

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitComplexExpr(self, ctx):
        real = int(ctx.complexNumber().REAL().getText())
        imaginary = 0
        if ctx.complexNumber().IMAGINARY():
            imaginary = int(ctx.complexNumber().IMAGINARY().getText()[:-1])  # Quitamos la 'j'
        complex_value = complex(real, imaginary)
        print(f"Complejo: {complex_value}")
        return complex_value

    def visitIntegerExpr(self, ctx):
        value = int(ctx.INTEGER().getText())
        print(f"Entero: {value}")
        return value

    def visitVariableExpr(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = self.variables.get(var_name, complex(0, 0))  # Valor por defecto 0 + 0j si no existe
        print(f"Variable: {var_name} = {self.format_output(value)}")
        return var_name  # Retornar el nombre de la variable

    def format_output(self, value):
        """Función que formatea la salida dependiendo del tipo."""
        if isinstance(value, complex):
            return str(value)  # Mostrar como número complejo
        elif isinstance(value, str):
            return value  # Retornar la variable como string
        else:
            return str(value)  # Para enteros y demás

    def get_final_result(self):
        """Genera el resultado final a partir de las operaciones realizadas."""
        if self.operations:
            final_operation = " , ".join(self.operations)
            return f"Resultado total: {final_operation}"
        return "No se realizaron operaciones."

def main(input_text):
    input_stream = InputStream(input_text)
    lexer = punto1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = punto1Parser(token_stream)
    tree = parser.expr()

    visitor = MyComplexVisitor()
    result = visitor.visit(tree)

    # Mostrar el resultado final correctamente
    print("Resultado final:", visitor.format_output(result))

if __name__ == '__main__':
    # Cambia esta expresión para probar diferentes casos
    input_text = '((2+0j) + (3+0j)) * ((5+0j) + (8+0j))'  # Puedes probar con diferentes expresiones
    main(input_text)

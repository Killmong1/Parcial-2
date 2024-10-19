import sys
from antlr4 import *  # Importamos las clases necesarias de ANTLR
from punto2Lexer import punto2Lexer  # Lexer generado por ANTLR que reconoce los tokens del lenguaje
from punto2Parser import punto2Parser  # Parser generado por ANTLR que analiza las reglas de la gramática
from punto2Visitor import punto2Visitor  # Visitor generado por ANTLR que permite recorrer el árbol sintáctico

# Definimos algunas funciones que el lenguaje soporta
def square(x):
    """Función que calcula el cuadrado de un número."""
    return x * x

def is_even(x):
    """Función que determina si un número es par."""
    return x % 2 == 0

# Clase visitante que implementa la lógica para ejecutar las expresiones del lenguaje
class MyMapFilterVisitor(punto2Visitor):  
    """
    Clase que extiende el visitor generado por ANTLR para interpretar el árbol sintáctico
    y ejecutar las operaciones de map y filter sobre las listas o tuplas.
    """
    
    def visitMapFunction(self, ctx):
        """
        Método que se ejecuta cuando se encuentra una función `MAP`.
        Aplica una función sobre una lista o tupla utilizando `map`.
        """
        function_name = ctx.ID().getText()  # Obtiene el nombre de la función a aplicar
        function = globals()[function_name]  # Busca la función en el entorno global (por ejemplo, 'square')
        iterable = self.visit(ctx.iterable())  # Evalúa el iterable (lista o tupla)
        result = list(map(function, iterable))  # Aplica la función usando map y convierte el resultado a lista
        print(f"MAP result: {result}")  # Imprime el resultado para depuración
        return result  # Retorna el resultado de la operación map
    
    def visitFilterFunction(self, ctx):
        """
        Método que se ejecuta cuando se encuentra una función `FILTER`.
        Aplica una función de filtro sobre una lista o tupla utilizando `filter`.
        """
        function_name = ctx.ID().getText()  # Obtiene el nombre de la función de filtro
        function = globals()[function_name]  # Busca la función en el entorno global (por ejemplo, 'is_even')
        iterable = self.visit(ctx.iterable())  # Evalúa el iterable (lista o tupla)
        result = list(filter(function, iterable))  # Aplica el filtro usando filter y convierte el resultado a lista
        print(f"FILTER result: {result}")  # Imprime el resultado para depuración
        return result  # Retorna el resultado de la operación filter

    def visitListIterable(self, ctx):
        """
        Método que se ejecuta cuando el iterable es una lista.
        Visita cada elemento de la lista y lo evalúa.
        """
        elements = self.visit(ctx.exprList())  # Evalúa los elementos de la lista
        return elements  # Retorna la lista de elementos evaluados
    
    def visitTupleIterable(self, ctx):
        """
        Método que se ejecuta cuando el iterable es una tupla.
        Visita cada elemento de la tupla y lo evalúa.
        """
        elements = self.visit(ctx.exprList())  # Evalúa los elementos de la tupla
        return elements  # Retorna la tupla de elementos evaluados
    
    def visitExprList(self, ctx):
        """
        Método que se ejecuta cuando se encuentra una lista de expresiones.
        Convierte los valores de las expresiones en enteros.
        """
        return [int(expr.getText()) for expr in ctx.expr()]  # Retorna una lista de enteros

# Función principal para ejecutar el programa
def main(input_text):
    """
    Función principal que inicializa el lexer, el parser, y recorre el árbol de análisis sintáctico.
    """
    input_stream = InputStream(input_text)  # Crea un flujo de entrada a partir del texto proporcionado
    lexer = punto2Lexer(input_stream)  # Inicializa el lexer para dividir el texto en tokens
    token_stream = CommonTokenStream(lexer)  # Almacena los tokens generados por el lexer
    parser = punto2Parser(token_stream)  # Inicializa el parser para construir el árbol sintáctico a partir de los tokens
    tree = parser.program()  # Inicia el análisis sintáctico en el nodo 'program' de la gramática

    visitor = MyMapFilterVisitor()  # Crea una instancia del visitor personalizado
    visitor.visit(tree)  # Recorre el árbol sintáctico con el visitor para ejecutar el programa

if __name__ == '__main__':
    """
    Punto de entrada principal del programa.
    """
    # Ejemplo de entrada con dos operaciones: una de map y otra de filter
    input_text = 'MAP(square, [1, 2, 3, 4])\nFILTER(is_even, [1, 2, 3, 4])'  # Puedes modificar la entrada
    main(input_text)  # Llama a la función principal con la entrada proporcionada

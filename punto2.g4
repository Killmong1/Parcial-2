grammar MapGrammar;

// Reglas de entrada
program         : statement* EOF ;
statement       : mapFunction
                | functionDefinition
                ;

// Definición de la función map
mapFunction     : 'MAP' '(' function ',' iterable ')' ;

// Definición de la función (puede ser una función predefinida o una definida por el usuario)
function        : IDENTIFIER '(' (expression (',' expression)*)? ')' 
                | IDENTIFIER  // Funciones predefinidas sin parámetros
                ;

// Definición de un iterable
iterable        : list
                | tuple
                ;

// Definición de una lista
list            : '[' (expression (',' expression)*)? ']' ;

// Definición de una tupla
tuple           : '(' (expression (',' expression)*)? ')' ;

// Expresiones válidas
expression      : IDENTIFIER
                | NUMBER
                | STRING
                | '(' expression ')'  // Soporte para paréntesis
                ;

// Definiciones de terminales
IDENTIFIER      : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores (nombres de funciones y variables)
NUMBER          : [0-9]+ ;                      // Números enteros
STRING          : '"' (ESC | ~["\\])* '"' ;   // Cadenas entre comillas
fragment ESC    : '\\' [btnfr"'\\] ;           // Escape de caracteres

WS              : [ \t\r\n]+ -> skip ;          // Espacios en blanco


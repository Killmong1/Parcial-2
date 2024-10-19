grammar punto2;

// Reglas del parser
program : statement+ EOF;

statement
    : mapFunc
    | filterFunc
    ;

mapFunc
    : 'MAP' '(' ID ',' iterable ')' # MapFunction
    ;

filterFunc
    : 'FILTER' '(' ID ',' iterable ')' # FilterFunction
    ;

// Definición de un iterable: lista o tupla
iterable
    : list
    | tuple
    ;

list
    : '[' exprList ']' # ListIterable
    ;

tuple
    : '(' exprList ')' # TupleIterable
    ;

exprList
    : expr (',' expr)*  // Lista de expresiones separadas por comas
    ;

expr
    : INT  // Por simplicidad, consideramos solo enteros en esta gramática
    ;

// Tokens
ID  : [a-zA-Z_][a-zA-Z_0-9]*;  // Identificadores de funciones
INT : [0-9]+;  // Números enteros
WS  : [ \t\r\n]+ -> skip;  // Ignorar espacios en blanco

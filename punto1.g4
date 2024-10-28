grammar punto1;

// Reglas de parser
expr:   expr '+' expr               # AddExpr
    |   expr '-' expr               # SubtractExpr
    |   expr '*' expr               # MultiplyExpr
    |   '(' expr ')'                # ParenExpr
    |   complexNumber               # ComplexExpr
    |   INTEGER                     # IntegerExpr
    |   VARIABLE                    # VariableExpr
    ;

// Definición de un número complejo
complexNumber: REAL ( ('+'|'-') (IMAGINARY | VARIABLE))?;

// Tokens
REAL: [0-9]+;  // Parte real
IMAGINARY: [0-9]+ 'j';  // Parte imaginaria con 'j'
INTEGER: [0-9]+;  // Enteros
VARIABLE: [a-zA-Z_]+;  // Variables (como x, y, z)

// Ignoramos los espacios en blanco
WS: [ \t\r\n]+ -> skip;

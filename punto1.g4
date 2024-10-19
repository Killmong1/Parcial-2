grammar punto1;

// Reglas de parser
expr:   expr '+' expr               # AddExpr
    |   expr '-' expr               # SubtractExpr
    |   expr '*' expr               # MultiplyExpr
    |   '(' expr ')'                # ParenExpr
    |   complexNumber               # ComplexExpr
    ;

// Definición de un número complejo
complexNumber: REAL ( ('+'|'-') IMAGINARY )?;

// Tokens
REAL: [0-9]+;  // Parte real
IMAGINARY: [0-9]+ 'i';  // Parte imaginaria

// Ignoramos los espacios en blanco
WS: [ \t\r\n]+ -> skip;

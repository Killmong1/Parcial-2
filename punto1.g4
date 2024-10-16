grammar punto1;

// Regla de entrada principal
expr: term (('+' | '-') term)*;

// Regla para un término que puede ser un número complejo
term: '(' complexNumber ')' 
    | complexNumber;

// Regla para un número complejo
complexNumber: REAL ('+' | '-') IMAGINARY;

// Tokens
REAL: [0-9]+; // Para representar la parte real
IMAGINARY: [0-9]+ 'i'; // Para representar la parte imaginaria

// Espacios en blanco
WS: [ \t\r\n]+ -> skip; // Ignora los espacios en blanco


grammar PSeInt;

// ============================================
// Estructura básica, declaraciones y E/S
// ============================================

prog: encabezado bloque fin EOF;

encabezado: ('Proceso' | 'Algoritmo') IDENTIFICADOR;
bloque: sentencia*;
fin: ('FinProceso' | 'FinAlgoritmo');

sentencia
    : declaracion
    | asignacion
    | lectura
    | escritura
    // Pendiente: agregar Si/FinSi (condicional)
    // | condicional
    // Pendiente: agregar Mientras, Para, Repetir (bucles)
    // | mientras
    // | para
    // | repetir
    // Pendiente: agregar procedimientos y funciones
    // | subproceso
    // | funcion
    ;

// Declaraciones
declaracion: 'Definir' IDENTIFICADOR (',' IDENTIFICADOR)* 'Como' tipo;
tipo: 'Entero' | 'Real' | 'Logico' | 'Caracter' | 'Cadena';

// Asignaciones
asignacion: IDENTIFICADOR '<-' expr ';';

// Entrada/Salida
lectura: 'Leer' IDENTIFICADOR (',' IDENTIFICADOR)* ';';
escritura: 'Escribir' listaEscritura ';';
listaEscritura: expr (',' expr)*;

// Expresiones (aritmética básica)
expr
    : expr ('*' | '/' | 'MOD') expr      # MulDiv
    | expr ('+' | '-') expr              # AddSub
    | expr '^' expr                      # Potencia
    | '(' expr ')'                       # Parens
    | NUMERO                             # Numero
    | IDENTIFICADOR                      # Variable
    | CADENA                             # String
    ;

// ============================================
// TOKENS
// ============================================

NUMERO: [0-9]+ ('.' [0-9]+)?;
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;
CADENA: '"' (~["\\\r\n])* '"';

WS: [ \t\r\n]+ -> skip;
COMENTARIO: '//' ~[\r\n]* -> skip;

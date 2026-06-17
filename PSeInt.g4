grammar PSeInt;

// ============================================
// Estructura básica
// ============================================
// Un programa puede incluir funciones y subprocesos (antes o después
// del algoritmo principal), seguidos del algoritmo/proceso principal.
prog: subprograma* principal subprograma* EOF;

principal: encabezado bloque fin;

encabezado: ('Proceso' | 'Algoritmo') IDENTIFICADOR;
bloque: sentencia*;
fin: ('FinProceso' | 'FinAlgoritmo');

// ============================================
// Funciones y subprocesos
// ============================================

subprograma: funcion | subproceso;

// Funcion: retorna un valor (declarado como variable de retorno)
funcion
    : 'Funcion' IDENTIFICADOR '<-' IDENTIFICADOR '(' parametros? ')'
        bloque
      'FinFuncion'
    ;

// SubProceso / SubAlgoritmo: no retorna valor
subproceso
    : ('SubProceso' | 'SubAlgoritmo') IDENTIFICADOR '(' parametros? ')'
        bloque
      ('FinSubProceso' | 'FinSubAlgoritmo')
    ;

parametros: IDENTIFICADOR (',' IDENTIFICADOR)*;
argumentos: expr (',' expr)*;

// ============================================
// Sentencias
// ============================================

sentencia
    : declaracion
    | asignacion
    | lectura
    | escritura
    | condicional   // Si / Sino / FinSi
    | mientras      // Mientras / FinMientras
    | para          // Para / FinPara
    | repetir       // Repetir / Hasta Que
    | llamada       // invocación de un subproceso
    ;

// Declaraciones
declaracion: 'Definir' IDENTIFICADOR (',' IDENTIFICADOR)* 'Como' tipo ';'?;
tipo: 'Entero' | 'Real' | 'Logico' | 'Caracter' | 'Cadena';

// Asignaciones (el ';' final es opcional para mayor tolerancia)
asignacion: IDENTIFICADOR '<-' expr ';'?;

// Entrada/Salida
lectura: 'Leer' IDENTIFICADOR (',' IDENTIFICADOR)* ';'?;
escritura: ('Escribir' | 'Mostrar') listaEscritura ';'?;
listaEscritura: expr (',' expr)*;

// Llamada a un subproceso como sentencia
llamada: IDENTIFICADOR '(' argumentos? ')' ';'?;

// ============================================
// Estructuras de control
// ============================================

condicional
    : 'Si' expr 'Entonces'
        bloque
      ('Sino' bloque)?
      'FinSi'
    ;

mientras
    : 'Mientras' expr 'Hacer'
        bloque
      'FinMientras'
    ;

para
    : 'Para' IDENTIFICADOR '<-' expr 'Hasta' expr ('Con' 'Paso' expr)? 'Hacer'
        bloque
      'FinPara'
    ;

repetir
    : 'Repetir'
        bloque
      'Hasta' 'Que' expr ';'?
    ;

// ============================================
// Expresiones (con jerarquía de precedencia)
// ============================================
// De MAYOR a MENOR precedencia:
//   1. Paréntesis y llamadas a función
//   2. Potencia (^)               -> asociativa por la derecha
//   3. Multiplicación, división, módulo (*, /, MOD)
//   4. Suma, resta (+, -)
//   5. Relacionales (>, <, >=, <=, =, <>)
//   6. NO / ~  (negación lógica)
//   7. Y / &   (conjunción)
//   8. O / |   (disyunción)
expr
    : '(' expr ')'                                          # Parens
    | IDENTIFICADOR '(' argumentos? ')'                    # LlamadaFuncion
    | <assoc=right> expr '^' expr                          # Potencia
    | expr ('*' | '/' | 'MOD') expr                        # MulDiv
    | expr ('+' | '-') expr                                # AddSub
    | expr ('>' | '<' | '>=' | '<=' | '=' | '<>') expr     # Relacional
    | ('NO' | '~') expr                                    # NoLogico
    | expr ('Y' | '&') expr                                # YLogico
    | expr ('O' | '|') expr                                # OLogico
    | NUMERO                                                # Numero
    | BOOLEANO                                              # Booleano
    | IDENTIFICADOR                                         # Variable
    | CADENA                                                # String
    ;

// ============================================
// TOKENS
// ============================================

// Booleanos en pseudocódigo: Verdadero / Falso
// (debe ir ANTES de IDENTIFICADOR para que ANTLR los reconozca como literales)
BOOLEANO: 'Verdadero' | 'Falso';

NUMERO: [0-9]+ ('.' [0-9]+)?;
IDENTIFICADOR: [a-zA-Z_][a-zA-Z0-9_]*;
CADENA: '"' (~["\\\r\n])* '"';

WS: [ \t\r\n]+ -> skip;
COMENTARIO: '//' ~[\r\n]* -> skip;

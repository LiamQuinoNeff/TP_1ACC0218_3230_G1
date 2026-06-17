````markdown
# TP_1ACC0218_3230_G1

Proyecto desarrollado para el curso de **Teoria de Compiladores (NRC: 3230)** de la **Universidad Peruana de Ciencias Aplicadas (UPC)**, a cargo del docente **Peter Jonathan Montalvo Garcia**.

El objetivo del trabajo es desarrollar un traductor de codigo inspirado en **PSeInt** hacia **Python**, utilizando **ANTLR4** para el analisis lexico y sintactico. Para el **Hito 2**, se permite trabajar con un backend temporal en Python, con el fin de validar el flujo principal del compilador. En el siguiente hito, el backend sera evolucionado hacia **LLVM**, de acuerdo con el alcance final del curso.

## Integrantes

| Codigo | Integrante |
| --- | --- |
| U202315585 | Alexander Miranda Vivanco |
| U202421876 | Gustavo Antonio Perez Rojas |
| U20221E167 | Liam Mikael Quino Neff |
| U202310543 | Johan Sebastian Quispe Quintana |
| U20181H114 | Mauricio Eduardo Vera Castellon |

## Resumen del proyecto

En este repositorio se desarrolla un traductor de codigo de **PSeInt a Python**, orientado a facilitar la transicion desde el pseudocodigo educativo hacia un lenguaje de programacion real.

El proyecto utiliza **ANTLR4** para definir la gramatica, generar el lexer, parser y visitor, y construir el flujo principal de analisis del codigo fuente. En el **Hito 2**, el avance se centra en ampliar la gramatica e implementar una primera version funcional del backend en Python. Esta implementacion permite traducir instrucciones basicas y estructuras de control de PSeInt a codigo Python equivalente.

El alcance actual corresponde al **Hito 2** del curso, por lo que el repositorio incluye un avance aproximado del 50% de la implementacion final. La integracion con **LLVM** queda planificada para el siguiente hito.

## Alcance actual

El estado actual del repositorio corresponde al avance solicitado para el **Hito 2**:

- Informe con la problematica, motivacion y objetivos del proyecto.
- Gramatica actualizada en ANTLR4.
- Arquitectura general del compilador.
- Plan de validacion.
- Implementacion parcial del compilador.
- Backend temporal en Python.
- Pruebas preliminares en Google Colab.
- Repositorio con el codigo fuente del avance.

## Funcionalidades reconocidas por la gramatica

La gramatica actualizada permite reconocer:

- Encabezado de programa con `Proceso` o `Algoritmo`.
- Cierre de programa con `FinProceso` o `FinAlgoritmo`.
- Declaraciones de variables con `Definir`.
- Tipos de datos basicos: `Entero`, `Real`, `Logico`, `Caracter` y `Cadena`.
- Asignaciones con el operador `<-`.
- Lectura de datos con `Leer`.
- Escritura de datos con `Escribir` o `Mostrar`.
- Expresiones aritmeticas con operadores `+`, `-`, `*`, `/`, `MOD` y `^`.
- Expresiones relacionales con `>`, `<`, `>=`, `<=`, `=` y `<>`.
- Expresiones logicas con `Y`, `O` y `NO`.
- Condicionales con `Si`, `Entonces`, `Sino` y `FinSi`.
- Bucles con `Mientras` y `FinMientras`.
- Bucles con `Para`, `Hasta`, `Con Paso` y `FinPara`.
- Repeticiones con `Repetir` y `Hasta Que`.
- Funciones con `Funcion` y `FinFuncion`.
- Subprocesos con `SubProceso` y `FinSubProceso`.

## Arquitectura del compilador

La arquitectura del compilador se organiza en etapas simples y progresivas. Para el Hito 2, el flujo implementado utiliza ANTLR4 como frontend y Python como backend temporal.

```text
Codigo fuente PSeInt
        ↓
Analizador lexico - Lexer ANTLR4
        ↓
Analizador sintactico - Parser ANTLR4
        ↓
Arbol de analisis sintactico - Parse Tree
        ↓
Visitor TraductorPython
        ↓
Backend temporal en Python
        ↓
Codigo Python generado
        ↓
Ejecucion y pruebas preliminares
````

Para el siguiente hito, se proyecta reemplazar o complementar el backend temporal con **LLVM**, siguiendo el flujo final del compilador:

```text
Codigo fuente PSeInt
        ↓
ANTLR4 Lexer y Parser
        ↓
Parse Tree
        ↓
Visitor / Generador intermedio
        ↓
Backend LLVM
        ↓
LLVM IR
        ↓
Optimizacion y generacion de codigo
```

## Sistema multiagente

El proyecto se organiza como un sistema multiagente simple, donde cada agente cumple una responsabilidad dentro del proceso de traduccion.

| Agente                  | Responsabilidad                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------ |
| Agente lexico           | Reconoce tokens como palabras clave, identificadores, numeros, cadenas y operadores. |
| Agente sintactico       | Verifica que el codigo cumpla con la gramatica definida en ANTLR4.                   |
| Agente traductor Python | Recorre el arbol sintactico y genera codigo Python como backend temporal.            |
| Agente de validacion    | Ejecuta casos de prueba y revisa que la traduccion mantenga la logica original.      |
| Agente de backend LLVM  | Sera desarrollado en el siguiente hito para generar codigo intermedio con LLVM.      |

## Traducciones principales del Hito 2

| PSeInt                            | Python generado                       |
| --------------------------------- | ------------------------------------- |
| `Definir x Como Entero`           | `x = 0`                               |
| `Definir nombre Como Cadena`      | `nombre = ""`                         |
| `x <- 10`                         | `x = 10`                              |
| `Leer x`                          | `x = input()` o conversion segun tipo |
| `Escribir "Hola"`                 | `print("Hola")`                       |
| `Si condicion Entonces`           | `if condicion:`                       |
| `Sino`                            | `else:`                               |
| `Mientras condicion Hacer`        | `while condicion:`                    |
| `Para i <- 1 Hasta n Hacer`       | `for i in range(1, n + 1):`           |
| `Repetir ... Hasta Que condicion` | `while True:` con condicion de salida |
| `Verdadero` / `Falso`             | `True` / `False`                      |
| `Y` / `O` / `NO`                  | `and` / `or` / `not`                  |
| `MOD`                             | `%`                                   |
| `^`                               | `**`                                  |

## Plan de validacion

Para el Hito 2 se plantea un plan de validacion orientado a comprobar que el flujo principal del traductor funcione correctamente.

Los criterios considerados son:

* Reconocer programas validos escritos en PSeInt.
* Detectar errores de sintaxis en programas invalidos.
* Generar codigo Python equivalente.
* Mantener la logica original del programa.
* Ejecutar el codigo Python generado sin errores en casos basicos.

Casos de prueba propuestos:

| Codigo | Caso de prueba                        | Elemento validado                 |
| ------ | ------------------------------------- | --------------------------------- |
| CP-01  | Declaracion y asignacion de variables | `Definir`, `<-`                   |
| CP-02  | Entrada y salida basica               | `Leer`, `Escribir`                |
| CP-03  | Expresiones aritmeticas               | `+`, `-`, `*`, `/`, `MOD`, `^`    |
| CP-04  | Condicional simple                    | `Si`, `Sino`, `FinSi`             |
| CP-05  | Bucle Mientras                        | `Mientras`, `FinMientras`         |
| CP-06  | Bucle Para                            | `Para`, `Hasta`, `Con Paso`       |
| CP-07  | Repeticion                            | `Repetir`, `Hasta Que`            |
| CP-08  | Operadores logicos                    | `Y`, `O`, `NO`                    |
| CP-09  | Funciones                             | `Funcion`, `FinFuncion`           |
| CP-10  | Subprocesos                           | `SubProceso`, `FinSubProceso`     |
| CP-11  | Caso integrado                        | Programa con varias estructuras   |
| CP-12  | Codigo con error                      | Validacion de errores sintacticos |

## Entregables del Hito 2

De acuerdo con el avance solicitado para el segundo hito, este repositorio contempla:

* Informe actualizado.
* Problematica, motivacion y objetivos del proyecto.
* Gramatica actualizada en ANTLR4.
* Arquitectura del compilador.
* Plan de validacion.
* Codigo fuente con avance de la implementacion.
* Notebook de Colab con pruebas preliminares.
* Backend temporal en Python.

## Estructura del repositorio

```text
.
├── .gitignore
├── PSeint.g4
├── README.md
├── TP_1ACC0218_3230_G1.ipynb
├── lib/
└── source/
    ├── PSeIntLexer.py
    ├── PSeIntListener.py
    ├── PSeIntParser.py
    └── PSeIntVisitor.py
```

## Gramatica

La gramatica principal se encuentra en [PSeint.g4](PSeint.g4). Esta version actualizada amplia la gramatica inicial del Hito 1 e incorpora nuevas reglas para estructuras condicionales, bucles, repeticiones, funciones y subprocesos.

El objetivo de esta gramatica es reconocer programas escritos con una sintaxis similar a PSeInt y permitir su posterior traduccion a Python mediante un Visitor personalizado.

## Estado de desarrollo

El proyecto se encuentra en el **Hito 2**, con un avance parcial de la implementacion final. Actualmente ya se cuenta con una gramatica ampliada, archivos generados por ANTLR4 y una primera estrategia de traduccion hacia Python.

Python se utiliza como backend temporal para este hito, ya que permite comprobar la traduccion de manera rapida y clara. La implementacion con **LLVM** queda pendiente para el siguiente hito.

## Proximo paso

El siguiente hito del proyecto consistira en completar la implementacion del compilador, integrar el backend con **LLVM**, ejecutar el plan de validacion de forma completa, documentar los resultados obtenidos y preparar la presentacion final del proyecto.

```
```

# TP_1ACC0218_3230_G1

Proyecto desarrollado para el curso de **Teoria de Compiladores (NCR: 3230)** de la **Universidad Peruana de Ciencias Aplicadas (UPC)**, a cargo del docente **Peter Jonathan Montalvo Garcia**.

El objetivo del trabajo es construir un lenguaje de programacion orientado a la solucion de una problematica definida por el grupo, utilizando **ANTLR4** en la etapa inicial y, mas adelante, una implementacion completa del compilador con **LLVM**.

## Integrantes

| Codigo | Integrante |
| --- | --- |
| U202315585 | Alexander Miranda Vivanco |
| U202421876 | Gustavo Antonio Perez Rojas |
| U20221E167 | Liam Mikael Quino Neff |
| U202310543 | Johan Sebastian Quispe Quintana |
| U20181H114 | Mauricio Eduardo Vera Castellon |

## Resumen del proyecto

En este repositorio se desarrolla una version inicial de un lenguaje inspirado en **PSeInt**, con una gramatica formalizada en **ANTLR4**. El alcance actual corresponde al **Hito 1** del curso, por lo que el proyecto se enfoca en la definicion del lenguaje, su estructura sintactica y una demostracion basica de funcionamiento.

La gramatica actualmente permite reconocer:

- Encabezado de programa con `Proceso` o `Algoritmo`.
- Declaraciones de variables con tipo.
- Asignaciones.
- Lectura de datos con `Leer`.
- Escritura de datos con `Escribir`.
- Expresiones aritmeticas basicas con operadores, parentesis y potencia.

## Alcance actual

El estado actual del repositorio corresponde exclusivamente al avance solicitado para el **Hito 1**:

- Informe preliminar con planteamiento del problema y motivacion.
- Gramática en ANTLR4.
- Repositorio con los archivos base del proyecto.
- Driver simple para demostracion inicial.

## Entregables del Hito 1

De acuerdo con el enunciado del curso, esta primera etapa contempla:

- Problematica y motivacion.
- Objetivos del lenguaje.
- Gramática en ANTLR4.
- Repositorio con el codigo fuente y un driver simple.
- Demo en video de la gramática.

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

## Gramática

La gramática principal se encuentra en [PSeint.g4](PSeint.g4) y define la estructura base del lenguaje. En esta primera version se prioriza la sintaxis esencial para describir programas simples y sentar las bases para futuras extensiones como:

- Condicionales.
- Bucles.
- Procedimientos y funciones.
- Analisis semantico.
- Generacion de codigo intermedio y back end con LLVM.

## Estado de desarrollo

Este avance cubre solamente la etapa inicial del proyecto. Las fases posteriores incluiran la ampliacion de la gramatica, la arquitectura del compilador y la implementacion completa del front end y back end.

## Proximo paso

El siguiente hito del proyecto consistira en ampliar la gramatica y avanzar con la implementacion del compilador, incluyendo validacion y arquitectura general de la solucion.
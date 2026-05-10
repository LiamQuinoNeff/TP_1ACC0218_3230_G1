# Generated from PSeInt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PSeIntParser import PSeIntParser
else:
    from source.PSeIntParser import PSeIntParser

# This class defines a complete listener for a parse tree produced by PSeIntParser.
class PSeIntListener(ParseTreeListener):

    # Enter a parse tree produced by PSeIntParser#prog.
    def enterProg(self, ctx:PSeIntParser.ProgContext):
        pass

    # Exit a parse tree produced by PSeIntParser#prog.
    def exitProg(self, ctx:PSeIntParser.ProgContext):
        pass


    # Enter a parse tree produced by PSeIntParser#encabezado.
    def enterEncabezado(self, ctx:PSeIntParser.EncabezadoContext):
        pass

    # Exit a parse tree produced by PSeIntParser#encabezado.
    def exitEncabezado(self, ctx:PSeIntParser.EncabezadoContext):
        pass


    # Enter a parse tree produced by PSeIntParser#bloque.
    def enterBloque(self, ctx:PSeIntParser.BloqueContext):
        pass

    # Exit a parse tree produced by PSeIntParser#bloque.
    def exitBloque(self, ctx:PSeIntParser.BloqueContext):
        pass


    # Enter a parse tree produced by PSeIntParser#fin.
    def enterFin(self, ctx:PSeIntParser.FinContext):
        pass

    # Exit a parse tree produced by PSeIntParser#fin.
    def exitFin(self, ctx:PSeIntParser.FinContext):
        pass


    # Enter a parse tree produced by PSeIntParser#sentencia.
    def enterSentencia(self, ctx:PSeIntParser.SentenciaContext):
        pass

    # Exit a parse tree produced by PSeIntParser#sentencia.
    def exitSentencia(self, ctx:PSeIntParser.SentenciaContext):
        pass


    # Enter a parse tree produced by PSeIntParser#declaracion.
    def enterDeclaracion(self, ctx:PSeIntParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by PSeIntParser#declaracion.
    def exitDeclaracion(self, ctx:PSeIntParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by PSeIntParser#tipo.
    def enterTipo(self, ctx:PSeIntParser.TipoContext):
        pass

    # Exit a parse tree produced by PSeIntParser#tipo.
    def exitTipo(self, ctx:PSeIntParser.TipoContext):
        pass


    # Enter a parse tree produced by PSeIntParser#asignacion.
    def enterAsignacion(self, ctx:PSeIntParser.AsignacionContext):
        pass

    # Exit a parse tree produced by PSeIntParser#asignacion.
    def exitAsignacion(self, ctx:PSeIntParser.AsignacionContext):
        pass


    # Enter a parse tree produced by PSeIntParser#lectura.
    def enterLectura(self, ctx:PSeIntParser.LecturaContext):
        pass

    # Exit a parse tree produced by PSeIntParser#lectura.
    def exitLectura(self, ctx:PSeIntParser.LecturaContext):
        pass


    # Enter a parse tree produced by PSeIntParser#escritura.
    def enterEscritura(self, ctx:PSeIntParser.EscrituraContext):
        pass

    # Exit a parse tree produced by PSeIntParser#escritura.
    def exitEscritura(self, ctx:PSeIntParser.EscrituraContext):
        pass


    # Enter a parse tree produced by PSeIntParser#listaEscritura.
    def enterListaEscritura(self, ctx:PSeIntParser.ListaEscrituraContext):
        pass

    # Exit a parse tree produced by PSeIntParser#listaEscritura.
    def exitListaEscritura(self, ctx:PSeIntParser.ListaEscrituraContext):
        pass


    # Enter a parse tree produced by PSeIntParser#Numero.
    def enterNumero(self, ctx:PSeIntParser.NumeroContext):
        pass

    # Exit a parse tree produced by PSeIntParser#Numero.
    def exitNumero(self, ctx:PSeIntParser.NumeroContext):
        pass


    # Enter a parse tree produced by PSeIntParser#Variable.
    def enterVariable(self, ctx:PSeIntParser.VariableContext):
        pass

    # Exit a parse tree produced by PSeIntParser#Variable.
    def exitVariable(self, ctx:PSeIntParser.VariableContext):
        pass


    # Enter a parse tree produced by PSeIntParser#MulDiv.
    def enterMulDiv(self, ctx:PSeIntParser.MulDivContext):
        pass

    # Exit a parse tree produced by PSeIntParser#MulDiv.
    def exitMulDiv(self, ctx:PSeIntParser.MulDivContext):
        pass


    # Enter a parse tree produced by PSeIntParser#AddSub.
    def enterAddSub(self, ctx:PSeIntParser.AddSubContext):
        pass

    # Exit a parse tree produced by PSeIntParser#AddSub.
    def exitAddSub(self, ctx:PSeIntParser.AddSubContext):
        pass


    # Enter a parse tree produced by PSeIntParser#Parens.
    def enterParens(self, ctx:PSeIntParser.ParensContext):
        pass

    # Exit a parse tree produced by PSeIntParser#Parens.
    def exitParens(self, ctx:PSeIntParser.ParensContext):
        pass


    # Enter a parse tree produced by PSeIntParser#String.
    def enterString(self, ctx:PSeIntParser.StringContext):
        pass

    # Exit a parse tree produced by PSeIntParser#String.
    def exitString(self, ctx:PSeIntParser.StringContext):
        pass


    # Enter a parse tree produced by PSeIntParser#Potencia.
    def enterPotencia(self, ctx:PSeIntParser.PotenciaContext):
        pass

    # Exit a parse tree produced by PSeIntParser#Potencia.
    def exitPotencia(self, ctx:PSeIntParser.PotenciaContext):
        pass



del PSeIntParser
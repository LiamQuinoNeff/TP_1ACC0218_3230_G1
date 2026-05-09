# Generated from PSeint.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PSeintParser import PSeintParser
else:
    from PSeintParser import PSeintParser

# This class defines a complete listener for a parse tree produced by PSeintParser.
class PSeintListener(ParseTreeListener):

    # Enter a parse tree produced by PSeintParser#prog.
    def enterProg(self, ctx:PSeintParser.ProgContext):
        pass

    # Exit a parse tree produced by PSeintParser#prog.
    def exitProg(self, ctx:PSeintParser.ProgContext):
        pass


    # Enter a parse tree produced by PSeintParser#encabezado.
    def enterEncabezado(self, ctx:PSeintParser.EncabezadoContext):
        pass

    # Exit a parse tree produced by PSeintParser#encabezado.
    def exitEncabezado(self, ctx:PSeintParser.EncabezadoContext):
        pass


    # Enter a parse tree produced by PSeintParser#bloque.
    def enterBloque(self, ctx:PSeintParser.BloqueContext):
        pass

    # Exit a parse tree produced by PSeintParser#bloque.
    def exitBloque(self, ctx:PSeintParser.BloqueContext):
        pass


    # Enter a parse tree produced by PSeintParser#fin.
    def enterFin(self, ctx:PSeintParser.FinContext):
        pass

    # Exit a parse tree produced by PSeintParser#fin.
    def exitFin(self, ctx:PSeintParser.FinContext):
        pass


    # Enter a parse tree produced by PSeintParser#sentencia.
    def enterSentencia(self, ctx:PSeintParser.SentenciaContext):
        pass

    # Exit a parse tree produced by PSeintParser#sentencia.
    def exitSentencia(self, ctx:PSeintParser.SentenciaContext):
        pass


    # Enter a parse tree produced by PSeintParser#declaracion.
    def enterDeclaracion(self, ctx:PSeintParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by PSeintParser#declaracion.
    def exitDeclaracion(self, ctx:PSeintParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by PSeintParser#tipo.
    def enterTipo(self, ctx:PSeintParser.TipoContext):
        pass

    # Exit a parse tree produced by PSeintParser#tipo.
    def exitTipo(self, ctx:PSeintParser.TipoContext):
        pass


    # Enter a parse tree produced by PSeintParser#asignacion.
    def enterAsignacion(self, ctx:PSeintParser.AsignacionContext):
        pass

    # Exit a parse tree produced by PSeintParser#asignacion.
    def exitAsignacion(self, ctx:PSeintParser.AsignacionContext):
        pass


    # Enter a parse tree produced by PSeintParser#lectura.
    def enterLectura(self, ctx:PSeintParser.LecturaContext):
        pass

    # Exit a parse tree produced by PSeintParser#lectura.
    def exitLectura(self, ctx:PSeintParser.LecturaContext):
        pass


    # Enter a parse tree produced by PSeintParser#escritura.
    def enterEscritura(self, ctx:PSeintParser.EscrituraContext):
        pass

    # Exit a parse tree produced by PSeintParser#escritura.
    def exitEscritura(self, ctx:PSeintParser.EscrituraContext):
        pass


    # Enter a parse tree produced by PSeintParser#listaEscritura.
    def enterListaEscritura(self, ctx:PSeintParser.ListaEscrituraContext):
        pass

    # Exit a parse tree produced by PSeintParser#listaEscritura.
    def exitListaEscritura(self, ctx:PSeintParser.ListaEscrituraContext):
        pass


    # Enter a parse tree produced by PSeintParser#Numero.
    def enterNumero(self, ctx:PSeintParser.NumeroContext):
        pass

    # Exit a parse tree produced by PSeintParser#Numero.
    def exitNumero(self, ctx:PSeintParser.NumeroContext):
        pass


    # Enter a parse tree produced by PSeintParser#Variable.
    def enterVariable(self, ctx:PSeintParser.VariableContext):
        pass

    # Exit a parse tree produced by PSeintParser#Variable.
    def exitVariable(self, ctx:PSeintParser.VariableContext):
        pass


    # Enter a parse tree produced by PSeintParser#MulDiv.
    def enterMulDiv(self, ctx:PSeintParser.MulDivContext):
        pass

    # Exit a parse tree produced by PSeintParser#MulDiv.
    def exitMulDiv(self, ctx:PSeintParser.MulDivContext):
        pass


    # Enter a parse tree produced by PSeintParser#AddSub.
    def enterAddSub(self, ctx:PSeintParser.AddSubContext):
        pass

    # Exit a parse tree produced by PSeintParser#AddSub.
    def exitAddSub(self, ctx:PSeintParser.AddSubContext):
        pass


    # Enter a parse tree produced by PSeintParser#Parens.
    def enterParens(self, ctx:PSeintParser.ParensContext):
        pass

    # Exit a parse tree produced by PSeintParser#Parens.
    def exitParens(self, ctx:PSeintParser.ParensContext):
        pass


    # Enter a parse tree produced by PSeintParser#String.
    def enterString(self, ctx:PSeintParser.StringContext):
        pass

    # Exit a parse tree produced by PSeintParser#String.
    def exitString(self, ctx:PSeintParser.StringContext):
        pass


    # Enter a parse tree produced by PSeintParser#Potencia.
    def enterPotencia(self, ctx:PSeintParser.PotenciaContext):
        pass

    # Exit a parse tree produced by PSeintParser#Potencia.
    def exitPotencia(self, ctx:PSeintParser.PotenciaContext):
        pass



del PSeintParser
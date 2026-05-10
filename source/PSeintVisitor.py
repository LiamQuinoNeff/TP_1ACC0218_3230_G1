# Generated from PSeInt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PSeIntParser import PSeIntParser
else:
    from source.PSeIntParser import PSeIntParser

# This class defines a complete generic visitor for a parse tree produced by PSeIntParser.

class PSeIntVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PSeIntParser#prog.
    def visitProg(self, ctx:PSeIntParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#encabezado.
    def visitEncabezado(self, ctx:PSeIntParser.EncabezadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#bloque.
    def visitBloque(self, ctx:PSeIntParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#fin.
    def visitFin(self, ctx:PSeIntParser.FinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#sentencia.
    def visitSentencia(self, ctx:PSeIntParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#declaracion.
    def visitDeclaracion(self, ctx:PSeIntParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#tipo.
    def visitTipo(self, ctx:PSeIntParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#asignacion.
    def visitAsignacion(self, ctx:PSeIntParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#lectura.
    def visitLectura(self, ctx:PSeIntParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#escritura.
    def visitEscritura(self, ctx:PSeIntParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#listaEscritura.
    def visitListaEscritura(self, ctx:PSeIntParser.ListaEscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Numero.
    def visitNumero(self, ctx:PSeIntParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Variable.
    def visitVariable(self, ctx:PSeIntParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#MulDiv.
    def visitMulDiv(self, ctx:PSeIntParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#AddSub.
    def visitAddSub(self, ctx:PSeIntParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Parens.
    def visitParens(self, ctx:PSeIntParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#String.
    def visitString(self, ctx:PSeIntParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Potencia.
    def visitPotencia(self, ctx:PSeIntParser.PotenciaContext):
        return self.visitChildren(ctx)



del PSeIntParser
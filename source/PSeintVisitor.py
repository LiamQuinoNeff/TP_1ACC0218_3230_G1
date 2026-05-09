# Generated from PSeint.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PSeintParser import PSeintParser
else:
    from PSeintParser import PSeintParser

# This class defines a complete generic visitor for a parse tree produced by PSeintParser.

class PSeintVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PSeintParser#prog.
    def visitProg(self, ctx:PSeintParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#encabezado.
    def visitEncabezado(self, ctx:PSeintParser.EncabezadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#bloque.
    def visitBloque(self, ctx:PSeintParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#fin.
    def visitFin(self, ctx:PSeintParser.FinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#sentencia.
    def visitSentencia(self, ctx:PSeintParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#declaracion.
    def visitDeclaracion(self, ctx:PSeintParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#tipo.
    def visitTipo(self, ctx:PSeintParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#asignacion.
    def visitAsignacion(self, ctx:PSeintParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#lectura.
    def visitLectura(self, ctx:PSeintParser.LecturaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#escritura.
    def visitEscritura(self, ctx:PSeintParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#listaEscritura.
    def visitListaEscritura(self, ctx:PSeintParser.ListaEscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#Numero.
    def visitNumero(self, ctx:PSeintParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#Variable.
    def visitVariable(self, ctx:PSeintParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#MulDiv.
    def visitMulDiv(self, ctx:PSeintParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#AddSub.
    def visitAddSub(self, ctx:PSeintParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#Parens.
    def visitParens(self, ctx:PSeintParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#String.
    def visitString(self, ctx:PSeintParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeintParser#Potencia.
    def visitPotencia(self, ctx:PSeintParser.PotenciaContext):
        return self.visitChildren(ctx)



del PSeintParser
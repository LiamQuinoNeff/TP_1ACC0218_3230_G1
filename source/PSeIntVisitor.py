# Generated from PSeInt.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PSeIntParser import PSeIntParser
else:
    from PSeIntParser import PSeIntParser

# This class defines a complete generic visitor for a parse tree produced by PSeIntParser.

class PSeIntVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PSeIntParser#prog.
    def visitProg(self, ctx:PSeIntParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#principal.
    def visitPrincipal(self, ctx:PSeIntParser.PrincipalContext):
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


    # Visit a parse tree produced by PSeIntParser#subprograma.
    def visitSubprograma(self, ctx:PSeIntParser.SubprogramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#funcion.
    def visitFuncion(self, ctx:PSeIntParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#subproceso.
    def visitSubproceso(self, ctx:PSeIntParser.SubprocesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#parametros.
    def visitParametros(self, ctx:PSeIntParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#argumentos.
    def visitArgumentos(self, ctx:PSeIntParser.ArgumentosContext):
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


    # Visit a parse tree produced by PSeIntParser#llamada.
    def visitLlamada(self, ctx:PSeIntParser.LlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#condicional.
    def visitCondicional(self, ctx:PSeIntParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#mientras.
    def visitMientras(self, ctx:PSeIntParser.MientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#para.
    def visitPara(self, ctx:PSeIntParser.ParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#repetir.
    def visitRepetir(self, ctx:PSeIntParser.RepetirContext):
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


    # Visit a parse tree produced by PSeIntParser#OLogico.
    def visitOLogico(self, ctx:PSeIntParser.OLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Booleano.
    def visitBooleano(self, ctx:PSeIntParser.BooleanoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#String.
    def visitString(self, ctx:PSeIntParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#YLogico.
    def visitYLogico(self, ctx:PSeIntParser.YLogicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Relacional.
    def visitRelacional(self, ctx:PSeIntParser.RelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#LlamadaFuncion.
    def visitLlamadaFuncion(self, ctx:PSeIntParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#Potencia.
    def visitPotencia(self, ctx:PSeIntParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PSeIntParser#NoLogico.
    def visitNoLogico(self, ctx:PSeIntParser.NoLogicoContext):
        return self.visitChildren(ctx)



del PSeIntParser
# Generated from BooleanExpr.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BooleanExprParser import BooleanExprParser
else:
    from BooleanExprParser import BooleanExprParser

# This class defines a complete listener for a parse tree produced by BooleanExprParser.
class BooleanExprListener(ParseTreeListener):

    # Enter a parse tree produced by BooleanExprParser#compileUnit.
    def enterCompileUnit(self, ctx:BooleanExprParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#compileUnit.
    def exitCompileUnit(self, ctx:BooleanExprParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#conjunctionExpr.
    def enterConjunctionExpr(self, ctx:BooleanExprParser.ConjunctionExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#conjunctionExpr.
    def exitConjunctionExpr(self, ctx:BooleanExprParser.ConjunctionExprContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#negationExpr.
    def enterNegationExpr(self, ctx:BooleanExprParser.NegationExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#negationExpr.
    def exitNegationExpr(self, ctx:BooleanExprParser.NegationExprContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#impExr.
    def enterImpExr(self, ctx:BooleanExprParser.ImpExrContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#impExr.
    def exitImpExr(self, ctx:BooleanExprParser.ImpExrContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#disjunctionExpr.
    def enterDisjunctionExpr(self, ctx:BooleanExprParser.DisjunctionExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#disjunctionExpr.
    def exitDisjunctionExpr(self, ctx:BooleanExprParser.DisjunctionExprContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#numberExpr.
    def enterNumberExpr(self, ctx:BooleanExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#numberExpr.
    def exitNumberExpr(self, ctx:BooleanExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#parensExpr.
    def enterParensExpr(self, ctx:BooleanExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#parensExpr.
    def exitParensExpr(self, ctx:BooleanExprParser.ParensExprContext):
        pass


    # Enter a parse tree produced by BooleanExprParser#biimpExpr.
    def enterBiimpExpr(self, ctx:BooleanExprParser.BiimpExprContext):
        pass

    # Exit a parse tree produced by BooleanExprParser#biimpExpr.
    def exitBiimpExpr(self, ctx:BooleanExprParser.BiimpExprContext):
        pass



del BooleanExprParser
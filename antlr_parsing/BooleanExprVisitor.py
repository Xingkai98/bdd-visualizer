# Generated from BooleanExpr.g4 by ANTLR 4.8
from EvaluationVisitor import *
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BooleanExprParser import BooleanExprParser
else:
    from BooleanExprParser import BooleanExprParser

# This class defines a complete generic visitor for a parse tree produced by BooleanExprParser.

class BooleanExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BooleanExprParser#compileUnit.
    def visitCompileUnit(self, ctx:BooleanExprParser.CompileUnitContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by BooleanExprParser#variableExpr.
    def visitVariableExpr(self, ctx:BooleanExprParser.VariableExprContext):
        return BooleanVariableNode(value=str(ctx.VARIABLE()))

    # Visit a parse tree produced by BooleanExprParser#conjunctionExpr.
    def visitConjunctionExpr(self, ctx: BooleanExprParser.ConjunctionExprContext):
        node = ExprNode(value='∧')
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by BooleanExprParser#negationExpr.
    def visitNegationExpr(self, ctx: BooleanExprParser.NegationExprContext):
        node = ExprNode(value='¬')
        node.child = self.visit(ctx.child)
        return node

    # Visit a parse tree produced by BooleanExprParser#impExr.
    def visitImpExr(self, ctx: BooleanExprParser.ImpExrContext):
        node = ExprNode(value='=>')
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by BooleanExprParser#disjunctionExpr.
    def visitDisjunctionExpr(self, ctx: BooleanExprParser.DisjunctionExprContext):
        node = ExprNode(value='∨')
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by BooleanExprParser#parensExpr.
    def visitParensExpr(self, ctx: BooleanExprParser.ParensExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by BooleanExprParser#biimpExpr.
    def visitBiimpExpr(self, ctx: BooleanExprParser.BiimpExprContext):
        node = ExprNode(value='<=>')
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node



del BooleanExprParser
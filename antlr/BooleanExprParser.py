# Generated from BooleanExpr.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("%\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\22\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3 \n\3\f\3\16\3#\13\3\3\3\2\3\4\4\2\4")
        buf.write("\2\2\2(\2\6\3\2\2\2\4\21\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2")
        buf.write("\3\b\3\3\2\2\2\t\n\b\3\1\2\n\13\7\3\2\2\13\f\5\4\3\2\f")
        buf.write("\r\7\4\2\2\r\22\3\2\2\2\16\17\7\5\2\2\17\22\5\4\3\b\20")
        buf.write("\22\7\n\2\2\21\t\3\2\2\2\21\16\3\2\2\2\21\20\3\2\2\2\22")
        buf.write("!\3\2\2\2\23\24\f\7\2\2\24\25\7\6\2\2\25 \5\4\3\b\26\27")
        buf.write("\f\6\2\2\27\30\7\7\2\2\30 \5\4\3\7\31\32\f\5\2\2\32\33")
        buf.write("\7\b\2\2\33 \5\4\3\6\34\35\f\4\2\2\35\36\7\t\2\2\36 \5")
        buf.write("\4\3\5\37\23\3\2\2\2\37\26\3\2\2\2\37\31\3\2\2\2\37\34")
        buf.write("\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\5\3\2\2\2")
        buf.write("#!\3\2\2\2\5\21\37!")
        return buf.getvalue()


class BooleanExprParser ( Parser ):

    grammarFileName = "BooleanExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\u00AC'", "'\u2227'", 
                     "'\u2228'", "'<=>'", "'=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VARIABLE", "WS" ]

    RULE_compileUnit = 0
    RULE_expr = 1

    ruleNames =  [ "compileUnit", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    VARIABLE=8
    WS=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompileUnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BooleanExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(BooleanExprParser.EOF, 0)

        def getRuleIndex(self):
            return BooleanExprParser.RULE_compileUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompileUnit" ):
                listener.enterCompileUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompileUnit" ):
                listener.exitCompileUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompileUnit" ):
                return visitor.visitCompileUnit(self)
            else:
                return visitor.visitChildren(self)




    def compileUnit(self):

        localctx = BooleanExprParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(BooleanExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BooleanExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(BooleanExprParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConjunctionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConjunctionExpr" ):
                listener.enterConjunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConjunctionExpr" ):
                listener.exitConjunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjunctionExpr" ):
                return visitor.visitConjunctionExpr(self)
            else:
                return visitor.visitChildren(self)


    class NegationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.child = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BooleanExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegationExpr" ):
                listener.enterNegationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegationExpr" ):
                listener.exitNegationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegationExpr" ):
                return visitor.visitNegationExpr(self)
            else:
                return visitor.visitChildren(self)


    class ImpExrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpExr" ):
                listener.enterImpExr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpExr" ):
                listener.exitImpExr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImpExr" ):
                return visitor.visitImpExr(self)
            else:
                return visitor.visitChildren(self)


    class DisjunctionExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDisjunctionExpr" ):
                listener.enterDisjunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDisjunctionExpr" ):
                listener.exitDisjunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDisjunctionExpr" ):
                return visitor.visitDisjunctionExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(BooleanExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class BiimpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BooleanExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BooleanExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(BooleanExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBiimpExpr" ):
                listener.enterBiimpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBiimpExpr" ):
                listener.exitBiimpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBiimpExpr" ):
                return visitor.visitBiimpExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BooleanExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BooleanExprParser.T__0]:
                localctx = BooleanExprParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(BooleanExprParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(BooleanExprParser.T__1)
                pass
            elif token in [BooleanExprParser.T__2]:
                localctx = BooleanExprParser.NegationExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(BooleanExprParser.T__2)
                self.state = 13
                localctx.child = self.expr(6)
                pass
            elif token in [BooleanExprParser.VARIABLE]:
                localctx = BooleanExprParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                self.match(BooleanExprParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = BooleanExprParser.ConjunctionExprContext(self, BooleanExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 18
                        self.match(BooleanExprParser.T__3)
                        self.state = 19
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = BooleanExprParser.DisjunctionExprContext(self, BooleanExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 21
                        self.match(BooleanExprParser.T__4)
                        self.state = 22
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = BooleanExprParser.BiimpExprContext(self, BooleanExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 23
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 24
                        self.match(BooleanExprParser.T__5)
                        self.state = 25
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = BooleanExprParser.ImpExrContext(self, BooleanExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 27
                        self.match(BooleanExprParser.T__6)
                        self.state = 28
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





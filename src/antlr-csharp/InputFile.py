# Generated from Calculator.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,28,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,15,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,1,
        1,0,1,2,2,0,2,0,2,1,0,6,7,1,0,3,4,29,0,4,1,0,0,0,2,14,1,0,0,0,4,
        5,3,2,1,0,5,1,1,0,0,0,6,7,6,1,-1,0,7,15,5,5,0,0,8,9,7,0,0,0,9,15,
        3,2,1,4,10,11,5,1,0,0,11,12,3,2,1,0,12,13,5,2,0,0,13,15,1,0,0,0,
        14,6,1,0,0,0,14,8,1,0,0,0,14,10,1,0,0,0,15,24,1,0,0,0,16,17,10,2,
        0,0,17,18,7,1,0,0,18,23,3,2,1,3,19,20,10,1,0,0,20,21,7,0,0,0,21,
        23,3,2,1,2,22,16,1,0,0,0,22,19,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,
        0,24,25,1,0,0,0,25,3,1,0,0,0,26,24,1,0,0,0,3,14,22,24
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "<INVALID>", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "PLUS", "MINUS", "WS" ]

    RULE_calc = 0
    RULE_expr = 1

    ruleNames =  [ "calc", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    PLUS=6
    MINUS=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CalcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def getRuleIndex(self):
            return CalculatorParser.RULE_calc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCalc" ):
                listener.enterCalc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCalc" ):
                listener.exitCalc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalc" ):
                return visitor.visitCalc(self)
            else:
                return visitor.visitChildren(self)




    def calc(self):

        localctx = CalculatorParser.CalcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_calc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(CalculatorParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class PlusOrMinusExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusOrMinusExpr" ):
                listener.enterPlusOrMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusOrMinusExpr" ):
                listener.exitPlusOrMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlusOrMinusExpr" ):
                return visitor.visitPlusOrMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = CalculatorParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(CalculatorParser.NUM)
                pass
            elif token in [6, 7]:
                localctx = CalculatorParser.PlusOrMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 9
                self.expr(4)
                pass
            elif token in [1]:
                localctx = CalculatorParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                self.match(CalculatorParser.T__0)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(CalculatorParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.InfixExprContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 17
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 18
                        localctx.right = self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.InfixExprContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 20
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 21
                        localctx.right = self.expr(2)
                        pass

             
                self.state = 26
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
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)

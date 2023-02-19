# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\r\4\2\t\2\3\2\7\2\6\n\2\f\2\16\2\t\13\2\3\2\3\2\3\2\2")
        buf.write("\2\3\2\2\3\6\2\3\5\34\37\'(**\2\f\2\7\3\2\2\2\4\6\t\2")
        buf.write("\2\2\5\4\3\2\2\2\6\t\3\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b")
        buf.write("\n\3\2\2\2\t\7\3\2\2\2\n\13\7\2\2\3\13\3\3\2\2\2\3\7")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'boolean'", "'do'", "'else'", 
                     "'float'", "'for'", "'function'", "'if'", "'integer'", 
                     "'return'", "'string'", "'while'", "'void'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'false'", 
                     "'true'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "','", "':'", "';'", "'.'", "'['", "']'", "'('", "')'", 
                     "'{'", "'}'", "'='", "<INVALID>", "'\"'", "'0'", "'_'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", 
                      "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                      "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                      "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "FALSE", "TRUE", "BOOL", "FLO", "INT", "ID", "COMA", 
                      "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", 
                      "RCB", "EQU", "ARR", "DB", "ZERO", "UNDE", "PLUS", 
                      "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", 
                      "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPP=2
    STR=3
    AUTO=4
    BREAK=5
    BOOLEAN=6
    DO=7
    ELSE=8
    FLOAT=9
    FOR=10
    FUNCTION=11
    IF=12
    INTEGER=13
    RETURN=14
    STRING=15
    WHILE=16
    VOID=17
    OUT=18
    CONTINUE=19
    OF=20
    INHERIT=21
    ARRAY=22
    FALSE=23
    TRUE=24
    BOOL=25
    FLO=26
    INT=27
    ID=28
    COMA=29
    COL=30
    SEM=31
    DOT=32
    LSB=33
    RSB=34
    LB=35
    RB=36
    LCB=37
    RCB=38
    EQU=39
    ARR=40
    DB=41
    ZERO=42
    UNDE=43
    PLUS=44
    MINU=45
    MUTI=46
    DIVI=47
    MODU=48
    NOT=49
    AND=50
    OR=51
    EQUL=52
    NEQ=53
    LESS=54
    LOEQ=55
    GREA=56
    GOEQ=57
    SCOPE=58
    WS=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def COMMENT_C(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMENT_C)
            else:
                return self.getToken(MT22Parser.COMMENT_C, i)

        def COMMENT_CPP(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMENT_CPP)
            else:
                return self.getToken(MT22Parser.COMMENT_CPP, i)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.STR)
            else:
                return self.getToken(MT22Parser.STR, i)

        def FLO(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.FLO)
            else:
                return self.getToken(MT22Parser.FLO, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INT)
            else:
                return self.getToken(MT22Parser.INT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.LCB)
            else:
                return self.getToken(MT22Parser.LCB, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def RCB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.RCB)
            else:
                return self.getToken(MT22Parser.RCB, i)

        def ARR(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ARR)
            else:
                return self.getToken(MT22Parser.ARR, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.COMMENT_C) | (1 << MT22Parser.COMMENT_CPP) | (1 << MT22Parser.STR) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.COMA) | (1 << MT22Parser.LCB) | (1 << MT22Parser.RCB) | (1 << MT22Parser.ARR))) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.COMMENT_C) | (1 << MT22Parser.COMMENT_CPP) | (1 << MT22Parser.STR) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.COMA) | (1 << MT22Parser.LCB) | (1 << MT22Parser.RCB) | (1 << MT22Parser.ARR))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 8
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("!\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\2\2\4\2\4\2\2\2*\2\24\3\2\2")
        buf.write("\2\4\31\3\2\2\2\6\23\5\4\3\2\7\23\7\3\2\2\b\23\7\4\2\2")
        buf.write("\t\23\7\5\2\2\n\23\7\36\2\2\13\23\7!\2\2\f\23\7 \2\2\r")
        buf.write("\23\7#\2\2\16\23\7,\2\2\17\23\7$\2\2\20\23\7-\2\2\21\23")
        buf.write("\7/\2\2\22\6\3\2\2\2\22\7\3\2\2\2\22\b\3\2\2\2\22\t\3")
        buf.write("\2\2\2\22\n\3\2\2\2\22\13\3\2\2\2\22\f\3\2\2\2\22\r\3")
        buf.write("\2\2\2\22\16\3\2\2\2\22\17\3\2\2\2\22\20\3\2\2\2\22\21")
        buf.write("\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25")
        buf.write("\27\3\2\2\2\26\24\3\2\2\2\27\30\7\2\2\3\30\3\3\2\2\2\31")
        buf.write("\32\7\31\2\2\32\33\7(\2\2\33\34\7!\2\2\34\35\7)\2\2\35")
        buf.write("\36\7\27\2\2\36\37\7\20\2\2\37\5\3\2\2\2\4\22\24")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'auto'", "'break'", "'boolean'", "'do'", 
                     "'else'", "'float'", "'for'", "'function'", "'if'", 
                     "'integer'", "'return'", "'string'", "'while'", "'void'", 
                     "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
                     "'false'", "'true'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "':'", "';'", "'.'", "'['", "']'", 
                     "'('", "')'", "'{'", "'}'", "'='", "<INVALID>", "'\"'", 
                     "'0'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "STRTYP", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                      "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                      "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                      "ARRAY", "FALSE", "TRUE", "BOOL", "BOOLTYP", "FLO", 
                      "FLOTYP", "INT", "DEMENTION", "INTTYP", "ID", "COMA", 
                      "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", 
                      "RCB", "EQU", "ARR", "DB", "ZERO", "UNDE", "PLUS", 
                      "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", 
                      "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_arraytype = 1

    ruleNames =  [ "program", "arraytype" ]

    EOF = Token.EOF
    COMMENT_C=1
    COMMENT_CPP=2
    STR=3
    STRTYP=4
    AUTO=5
    BREAK=6
    BOOLEAN=7
    DO=8
    ELSE=9
    FLOAT=10
    FOR=11
    FUNCTION=12
    IF=13
    INTEGER=14
    RETURN=15
    STRING=16
    WHILE=17
    VOID=18
    OUT=19
    CONTINUE=20
    OF=21
    INHERIT=22
    ARRAY=23
    FALSE=24
    TRUE=25
    BOOL=26
    BOOLTYP=27
    FLO=28
    FLOTYP=29
    INT=30
    DEMENTION=31
    INTTYP=32
    ID=33
    COMA=34
    COL=35
    SEM=36
    DOT=37
    LSB=38
    RSB=39
    LB=40
    RB=41
    LCB=42
    RCB=43
    EQU=44
    ARR=45
    DB=46
    ZERO=47
    UNDE=48
    PLUS=49
    MINU=50
    MUTI=51
    DIVI=52
    MODU=53
    NOT=54
    AND=55
    OR=56
    EQUL=57
    NEQ=58
    LESS=59
    LOEQ=60
    GREA=61
    GOEQ=62
    SCOPE=63
    WS=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67

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

        def arraytype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ArraytypeContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ArraytypeContext,i)


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

        def DEMENTION(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.DEMENTION)
            else:
                return self.getToken(MT22Parser.DEMENTION, i)

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
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.COMMENT_C) | (1 << MT22Parser.COMMENT_CPP) | (1 << MT22Parser.STR) | (1 << MT22Parser.ARRAY) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.DEMENTION) | (1 << MT22Parser.ID) | (1 << MT22Parser.COMA) | (1 << MT22Parser.LCB) | (1 << MT22Parser.RCB) | (1 << MT22Parser.ARR))) != 0):
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MT22Parser.ARRAY]:
                    self.state = 4
                    self.arraytype()
                    pass
                elif token in [MT22Parser.COMMENT_C]:
                    self.state = 5
                    self.match(MT22Parser.COMMENT_C)
                    pass
                elif token in [MT22Parser.COMMENT_CPP]:
                    self.state = 6
                    self.match(MT22Parser.COMMENT_CPP)
                    pass
                elif token in [MT22Parser.STR]:
                    self.state = 7
                    self.match(MT22Parser.STR)
                    pass
                elif token in [MT22Parser.FLO]:
                    self.state = 8
                    self.match(MT22Parser.FLO)
                    pass
                elif token in [MT22Parser.DEMENTION]:
                    self.state = 9
                    self.match(MT22Parser.DEMENTION)
                    pass
                elif token in [MT22Parser.INT]:
                    self.state = 10
                    self.match(MT22Parser.INT)
                    pass
                elif token in [MT22Parser.ID]:
                    self.state = 11
                    self.match(MT22Parser.ID)
                    pass
                elif token in [MT22Parser.LCB]:
                    self.state = 12
                    self.match(MT22Parser.LCB)
                    pass
                elif token in [MT22Parser.COMA]:
                    self.state = 13
                    self.match(MT22Parser.COMA)
                    pass
                elif token in [MT22Parser.RCB]:
                    self.state = 14
                    self.match(MT22Parser.RCB)
                    pass
                elif token in [MT22Parser.ARR]:
                    self.state = 15
                    self.match(MT22Parser.ARR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def DEMENTION(self):
            return self.getToken(MT22Parser.DEMENTION, 0)

        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(MT22Parser.ARRAY)
            self.state = 24
            self.match(MT22Parser.LSB)
            self.state = 25
            self.match(MT22Parser.DEMENTION)
            self.state = 26
            self.match(MT22Parser.RSB)
            self.state = 27
            self.match(MT22Parser.OF)
            self.state = 28
            self.match(MT22Parser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






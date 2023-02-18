# Generated from f:\Univercity\S2 Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment1\old.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class oldParser ( Parser ):

    grammarFileName = "old.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "':'", 
                     "'='", "';'", "'.'", "'['", "']'", "'('", "')'", "'{'", 
                     "'}'", "'\"'", "'0'", "'_'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "COMMENT_C", "COMMENT_CPP", 
                      "OPERATOR", "FLOAT", "INT", "BOOLEAN", "IDENTIFIER", 
                      "STRING", "SEPERATOR", "ESCAPE", "COM", "COL", "EQU", 
                      "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", "RCB", 
                      "DB", "ZERO", "UNDERLINE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    NEWLINE=1
    COMMENT_C=2
    COMMENT_CPP=3
    OPERATOR=4
    FLOAT=5
    INT=6
    BOOLEAN=7
    IDENTIFIER=8
    STRING=9
    SEPERATOR=10
    ESCAPE=11
    COM=12
    COL=13
    EQU=14
    SEM=15
    DOT=16
    LSB=17
    RSB=18
    LB=19
    RB=20
    LCB=21
    RCB=22
    DB=23
    ZERO=24
    UNDERLINE=25
    WS=26
    ERROR_CHAR=27
    UNCLOSE_STRING=28
    ILLEGAL_ESCAPE=29

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
            return self.getToken(oldParser.EOF, 0)

        def getRuleIndex(self):
            return oldParser.RULE_program




    def program(self):

        localctx = oldParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(oldParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






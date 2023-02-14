# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\u0124\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\3\3\3\7\3")
        buf.write("\62\n\3\f\3\16\3\65\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\7\4@\n\4\f\4\16\4C\13\4\3\4\3\4\3\5\3\5\5\5I\n")
        buf.write("\5\3\5\3\5\3\5\7\5N\n\5\f\5\16\5Q\13\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6d\n\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\bm\n\b\f\b\16\b")
        buf.write("p\13\b\3\b\3\b\3\b\5\bu\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5")
        buf.write("\t}\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0089")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0094\n\n")
        buf.write("\3\13\6\13\u0097\n\13\r\13\16\13\u0098\3\f\3\f\5\f\u009d")
        buf.write("\n\f\3\f\6\f\u00a0\n\f\r\f\16\f\u00a1\3\r\5\r\u00a5\n")
        buf.write("\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u010f\n\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\6\22\u0116\n\22\r\22\16\22\u0117\3")
        buf.write("\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\63\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\2\27\2\31\2\33\2\35\2\37\2!\2#\f%\r\'\16)\17\3\2\13\4")
        buf.write("\2\f\f\17\17\7\2##\'\',-//\61\61\13\2*+..\60\60<=??]]")
        buf.write("__}}\177\177\3\2\63;\4\2GGgg\4\2--//\4\2C\\c|\3\2\62;")
        buf.write("\5\2\n\f\16\17\"\"\2\u014a\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2\7;\3\2\2\2")
        buf.write("\tH\3\2\2\2\13c\3\2\2\2\re\3\2\2\2\17t\3\2\2\2\21\u0088")
        buf.write("\3\2\2\2\23\u0093\3\2\2\2\25\u0096\3\2\2\2\27\u009a\3")
        buf.write("\2\2\2\31\u00a4\3\2\2\2\33\u00a6\3\2\2\2\35\u010e\3\2")
        buf.write("\2\2\37\u0110\3\2\2\2!\u0112\3\2\2\2#\u0115\3\2\2\2%\u011b")
        buf.write("\3\2\2\2\'\u011e\3\2\2\2)\u0121\3\2\2\2+,\7\f\2\2,\4\3")
        buf.write("\2\2\2-.\7\61\2\2./\7,\2\2/\63\3\2\2\2\60\62\13\2\2\2")
        buf.write("\61\60\3\2\2\2\62\65\3\2\2\2\63\64\3\2\2\2\63\61\3\2\2")
        buf.write("\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\7,\2\2\678\7\61\2")
        buf.write("\289\3\2\2\29:\b\3\2\2:\6\3\2\2\2;<\7\61\2\2<=\7\61\2")
        buf.write("\2=A\3\2\2\2>@\n\2\2\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2\2A")
        buf.write("B\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\b\4\2\2E\b\3\2\2\2FI\5")
        buf.write("\31\r\2GI\7a\2\2HF\3\2\2\2HG\3\2\2\2IO\3\2\2\2JN\5\31")
        buf.write("\r\2KN\7a\2\2LN\5\33\16\2MJ\3\2\2\2MK\3\2\2\2ML\3\2\2")
        buf.write("\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\n\3\2\2\2QO\3\2\2\2")
        buf.write("Rd\t\3\2\2ST\7(\2\2Td\7(\2\2UV\7~\2\2Vd\7~\2\2WX\7?\2")
        buf.write("\2Xd\7?\2\2YZ\7#\2\2Zd\7?\2\2[d\7>\2\2\\]\7>\2\2]d\7?")
        buf.write("\2\2^d\7@\2\2_`\7@\2\2`d\7?\2\2ab\7<\2\2bd\7<\2\2cR\3")
        buf.write("\2\2\2cS\3\2\2\2cU\3\2\2\2cW\3\2\2\2cY\3\2\2\2c[\3\2\2")
        buf.write("\2c\\\3\2\2\2c^\3\2\2\2c_\3\2\2\2ca\3\2\2\2d\f\3\2\2\2")
        buf.write("ef\t\4\2\2f\16\3\2\2\2gn\t\5\2\2hi\5!\21\2ij\5\33\16\2")
        buf.write("jm\3\2\2\2km\5\33\16\2lh\3\2\2\2lk\3\2\2\2mp\3\2\2\2n")
        buf.write("l\3\2\2\2no\3\2\2\2ou\3\2\2\2pn\3\2\2\2qr\5\37\20\2rs")
        buf.write("\7\"\2\2su\3\2\2\2tg\3\2\2\2tq\3\2\2\2uv\3\2\2\2vw\b\b")
        buf.write("\3\2w\20\3\2\2\2xy\5\17\b\2yz\7\60\2\2z|\5\25\13\2{}\5")
        buf.write("\27\f\2|{\3\2\2\2|}\3\2\2\2}\u0089\3\2\2\2~\177\5\17\b")
        buf.write("\2\177\u0080\5\27\f\2\u0080\u0081\7\60\2\2\u0081\u0082")
        buf.write("\5\25\13\2\u0082\u0089\3\2\2\2\u0083\u0084\5\17\b\2\u0084")
        buf.write("\u0085\7\60\2\2\u0085\u0086\5\25\13\2\u0086\u0087\5\27")
        buf.write("\f\2\u0087\u0089\3\2\2\2\u0088x\3\2\2\2\u0088~\3\2\2\2")
        buf.write("\u0088\u0083\3\2\2\2\u0089\22\3\2\2\2\u008a\u008b\7v\2")
        buf.write("\2\u008b\u008c\7t\2\2\u008c\u008d\7w\2\2\u008d\u0094\7")
        buf.write("g\2\2\u008e\u008f\7h\2\2\u008f\u0090\7c\2\2\u0090\u0091")
        buf.write("\7n\2\2\u0091\u0092\7u\2\2\u0092\u0094\7g\2\2\u0093\u008a")
        buf.write("\3\2\2\2\u0093\u008e\3\2\2\2\u0094\24\3\2\2\2\u0095\u0097")
        buf.write("\5\33\16\2\u0096\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\26\3\2\2\2\u009a")
        buf.write("\u009c\t\6\2\2\u009b\u009d\t\7\2\2\u009c\u009b\3\2\2\2")
        buf.write("\u009c\u009d\3\2\2\2\u009d\u009f\3\2\2\2\u009e\u00a0\5")
        buf.write("\33\16\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\30\3\2\2\2\u00a3")
        buf.write("\u00a5\t\b\2\2\u00a4\u00a3\3\2\2\2\u00a5\32\3\2\2\2\u00a6")
        buf.write("\u00a7\t\t\2\2\u00a7\34\3\2\2\2\u00a8\u00a9\7c\2\2\u00a9")
        buf.write("\u00aa\7w\2\2\u00aa\u00ab\7v\2\2\u00ab\u010f\7q\2\2\u00ac")
        buf.write("\u00ad\7d\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\u00b0\7c\2\2\u00b0\u010f\7m\2\2\u00b1\u00b2\7d\2\2\u00b2")
        buf.write("\u00b3\7q\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5\7n\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7c\2\2\u00b7\u010f\7p\2\2\u00b8")
        buf.write("\u00b9\7f\2\2\u00b9\u010f\7q\2\2\u00ba\u00bb\7g\2\2\u00bb")
        buf.write("\u00bc\7n\2\2\u00bc\u00bd\7u\2\2\u00bd\u010f\7g\2\2\u00be")
        buf.write("\u00bf\7h\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1\7n\2\2\u00c1")
        buf.write("\u00c2\7u\2\2\u00c2\u010f\7g\2\2\u00c3\u00c4\7h\2\2\u00c4")
        buf.write("\u00c5\7n\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7c\2\2\u00c7")
        buf.write("\u010f\7v\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca\7q\2\2\u00ca")
        buf.write("\u010f\7t\2\2\u00cb\u00cc\7h\2\2\u00cc\u00cd\7w\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0\7v\2\2\u00d0")
        buf.write("\u00d1\7k\2\2\u00d1\u00d2\7q\2\2\u00d2\u010f\7p\2\2\u00d3")
        buf.write("\u00d4\7k\2\2\u00d4\u010f\7h\2\2\u00d5\u00d6\7k\2\2\u00d6")
        buf.write("\u00d7\7p\2\2\u00d7\u00d8\7v\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\u00da\7i\2\2\u00da\u00db\7g\2\2\u00db\u010f\7t\2\2\u00dc")
        buf.write("\u00dd\7t\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7v\2\2\u00df")
        buf.write("\u00e0\7w\2\2\u00e0\u00e1\7t\2\2\u00e1\u010f\7p\2\2\u00e2")
        buf.write("\u00e3\7u\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7t\2\2\u00e5")
        buf.write("\u00e6\7k\2\2\u00e6\u00e7\7p\2\2\u00e7\u010f\7i\2\2\u00e8")
        buf.write("\u00e9\7v\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7w\2\2\u00eb")
        buf.write("\u010f\7g\2\2\u00ec\u00ed\7y\2\2\u00ed\u00ee\7j\2\2\u00ee")
        buf.write("\u00ef\7k\2\2\u00ef\u00f0\7n\2\2\u00f0\u010f\7g\2\2\u00f1")
        buf.write("\u00f2\7x\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7k\2\2\u00f4")
        buf.write("\u010f\7f\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7w\2\2\u00f7")
        buf.write("\u010f\7v\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7q\2\2\u00fa")
        buf.write("\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7k\2\2\u00fd")
        buf.write("\u00fe\7p\2\2\u00fe\u00ff\7w\2\2\u00ff\u010f\7g\2\2\u0100")
        buf.write("\u0101\7q\2\2\u0101\u010f\7h\2\2\u0102\u0103\7k\2\2\u0103")
        buf.write("\u0104\7p\2\2\u0104\u0105\7j\2\2\u0105\u0106\7g\2\2\u0106")
        buf.write("\u0107\7t\2\2\u0107\u0108\7k\2\2\u0108\u010f\7v\2\2\u0109")
        buf.write("\u010a\7c\2\2\u010a\u010b\7t\2\2\u010b\u010c\7t\2\2\u010c")
        buf.write("\u010d\7c\2\2\u010d\u010f\7{\2\2\u010e\u00a8\3\2\2\2\u010e")
        buf.write("\u00ac\3\2\2\2\u010e\u00b1\3\2\2\2\u010e\u00b8\3\2\2\2")
        buf.write("\u010e\u00ba\3\2\2\2\u010e\u00be\3\2\2\2\u010e\u00c3\3")
        buf.write("\2\2\2\u010e\u00c8\3\2\2\2\u010e\u00cb\3\2\2\2\u010e\u00d3")
        buf.write("\3\2\2\2\u010e\u00d5\3\2\2\2\u010e\u00dc\3\2\2\2\u010e")
        buf.write("\u00e2\3\2\2\2\u010e\u00e8\3\2\2\2\u010e\u00ec\3\2\2\2")
        buf.write("\u010e\u00f1\3\2\2\2\u010e\u00f5\3\2\2\2\u010e\u00f8\3")
        buf.write("\2\2\2\u010e\u0100\3\2\2\2\u010e\u0102\3\2\2\2\u010e\u0109")
        buf.write("\3\2\2\2\u010f\36\3\2\2\2\u0110\u0111\7\62\2\2\u0111 ")
        buf.write("\3\2\2\2\u0112\u0113\7a\2\2\u0113\"\3\2\2\2\u0114\u0116")
        buf.write("\t\n\2\2\u0115\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\3\2\2\2")
        buf.write("\u0119\u011a\b\22\2\2\u011a$\3\2\2\2\u011b\u011c\13\2")
        buf.write("\2\2\u011c\u011d\b\23\4\2\u011d&\3\2\2\2\u011e\u011f\13")
        buf.write("\2\2\2\u011f\u0120\b\24\5\2\u0120(\3\2\2\2\u0121\u0122")
        buf.write("\13\2\2\2\u0122\u0123\b\25\6\2\u0123*\3\2\2\2\25\2\63")
        buf.write("AHMOclnt|\u0088\u0093\u0098\u009c\u00a1\u00a4\u010e\u0117")
        buf.write("\7\b\2\2\3\b\2\3\23\3\3\24\4\3\25\5")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NEWLINE = 1
    COMMENT_C = 2
    COMMENT_CPP = 3
    IDENTIFIER = 4
    OPERATOR = 5
    SEPERATOR = 6
    INT = 7
    FLOAT = 8
    BOOLEAN = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COMMENT_C", "COMMENT_CPP", "IDENTIFIER", "OPERATOR", 
            "SEPERATOR", "INT", "FLOAT", "BOOLEAN", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NEWLINE", "COMMENT_C", "COMMENT_CPP", "IDENTIFIER", "OPERATOR", 
                  "SEPERATOR", "INT", "FLOAT", "BOOLEAN", "DECIMAL", "EXPONENT", 
                  "LETTER", "DIGIT", "KEYWORD", "ZERO", "UNDERLINE", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.INT_action 
            actions[17] = self.ERROR_CHAR_action 
            actions[18] = self.UNCLOSE_STRING_action 
            actions[19] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

             	self.text = self.text.replace('_','').replace(' ','')

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     



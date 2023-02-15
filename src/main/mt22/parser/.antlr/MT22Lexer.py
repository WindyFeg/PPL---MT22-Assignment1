# Generated from f:\Univercity\S2 Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("\u0140\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\7\38\n\3\f\3\16\3;\13\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4F\n\4\f\4\16\4I\13\4")
        buf.write("\3\4\3\4\3\5\3\5\5\5O\n\5\3\5\3\5\3\5\7\5T\n\5\f\5\16")
        buf.write("\5W\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6j\n\6\3\7\3\7\3\b\3\b\6\bp\n")
        buf.write("\b\r\b\16\bq\3\b\3\b\3\b\5\bw\n\b\3\b\3\b\6\b{\n\b\r\b")
        buf.write("\16\b|\3\b\3\b\3\b\5\b\u0082\n\b\5\b\u0084\n\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u008c\n\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u0099\n\n\3\13\3\13\3\13\7\13")
        buf.write("\u009e\n\13\f\13\16\13\u00a1\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\7\f\u00ab\n\f\f\f\16\f\u00ae\13\f\3\r")
        buf.write("\6\r\u00b1\n\r\r\r\16\r\u00b2\3\16\3\16\5\16\u00b7\n\16")
        buf.write("\3\16\6\16\u00ba\n\16\r\16\16\16\u00bb\3\17\5\17\u00bf")
        buf.write("\n\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u0129\n\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\6\25\u0132\n\25\r\25\16\25")
        buf.write("\u0133\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\39\2\31\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\r+\16")
        buf.write("-\17/\20\3\2\13\4\2\f\f\17\17\7\2##\'\',-//\61\61\13\2")
        buf.write("*+..\60\60<=??]]__}}\177\177\3\2\63;\4\2GGgg\4\2--//\4")
        buf.write("\2C\\c|\3\2\62;\5\2\n\f\16\17\"\"\2\u016a\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61")
        buf.write("\3\2\2\2\5\63\3\2\2\2\7A\3\2\2\2\tN\3\2\2\2\13i\3\2\2")
        buf.write("\2\rk\3\2\2\2\17\u0083\3\2\2\2\21\u008b\3\2\2\2\23\u0098")
        buf.write("\3\2\2\2\25\u009a\3\2\2\2\27\u00a5\3\2\2\2\31\u00b0\3")
        buf.write("\2\2\2\33\u00b4\3\2\2\2\35\u00be\3\2\2\2\37\u00c0\3\2")
        buf.write("\2\2!\u0128\3\2\2\2#\u012a\3\2\2\2%\u012c\3\2\2\2\'\u012e")
        buf.write("\3\2\2\2)\u0131\3\2\2\2+\u0137\3\2\2\2-\u013a\3\2\2\2")
        buf.write("/\u013d\3\2\2\2\61\62\7\f\2\2\62\4\3\2\2\2\63\64\7\61")
        buf.write("\2\2\64\65\7,\2\2\659\3\2\2\2\668\13\2\2\2\67\66\3\2\2")
        buf.write("\28;\3\2\2\29:\3\2\2\29\67\3\2\2\2:<\3\2\2\2;9\3\2\2\2")
        buf.write("<=\7,\2\2=>\7\61\2\2>?\3\2\2\2?@\b\3\2\2@\6\3\2\2\2AB")
        buf.write("\7\61\2\2BC\7\61\2\2CG\3\2\2\2DF\n\2\2\2ED\3\2\2\2FI\3")
        buf.write("\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JK\b\4\2")
        buf.write("\2K\b\3\2\2\2LO\5\35\17\2MO\7a\2\2NL\3\2\2\2NM\3\2\2\2")
        buf.write("OU\3\2\2\2PT\5\35\17\2QT\7a\2\2RT\5\37\20\2SP\3\2\2\2")
        buf.write("SQ\3\2\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\n")
        buf.write("\3\2\2\2WU\3\2\2\2Xj\t\3\2\2YZ\7(\2\2Zj\7(\2\2[\\\7~\2")
        buf.write("\2\\j\7~\2\2]^\7?\2\2^j\7?\2\2_`\7#\2\2`j\7?\2\2aj\7>")
        buf.write("\2\2bc\7>\2\2cj\7?\2\2dj\7@\2\2ef\7@\2\2fj\7?\2\2gh\7")
        buf.write("<\2\2hj\7<\2\2iX\3\2\2\2iY\3\2\2\2i[\3\2\2\2i]\3\2\2\2")
        buf.write("i_\3\2\2\2ia\3\2\2\2ib\3\2\2\2id\3\2\2\2ie\3\2\2\2ig\3")
        buf.write("\2\2\2j\f\3\2\2\2kl\t\4\2\2l\16\3\2\2\2mp\5\27\f\2np\5")
        buf.write("#\22\2om\3\2\2\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2")
        buf.write("\2rs\3\2\2\2st\7\60\2\2tv\5\31\r\2uw\5\33\16\2vu\3\2\2")
        buf.write("\2vw\3\2\2\2w\u0084\3\2\2\2x{\5\27\f\2y{\5#\22\2zx\3\2")
        buf.write("\2\2zy\3\2\2\2{|\3\2\2\2|z\3\2\2\2|}\3\2\2\2}~\3\2\2\2")
        buf.write("~\u0081\5\33\16\2\177\u0080\7\60\2\2\u0080\u0082\5\31")
        buf.write("\r\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083o\3\2\2\2\u0083z\3\2\2\2\u0084\u0085\3\2")
        buf.write("\2\2\u0085\u0086\b\b\3\2\u0086\20\3\2\2\2\u0087\u008c")
        buf.write("\5\27\f\2\u0088\u0089\5#\22\2\u0089\u008a\7\"\2\2\u008a")
        buf.write("\u008c\3\2\2\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\b\t\4\2\u008e\22\3\2")
        buf.write("\2\2\u008f\u0090\7v\2\2\u0090\u0091\7t\2\2\u0091\u0092")
        buf.write("\7w\2\2\u0092\u0099\7g\2\2\u0093\u0094\7h\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7n\2\2\u0096\u0097\7u\2\2\u0097\u0099")
        buf.write("\7g\2\2\u0098\u008f\3\2\2\2\u0098\u0093\3\2\2\2\u0099")
        buf.write("\24\3\2\2\2\u009a\u009f\5\'\24\2\u009b\u009e\5\35\17\2")
        buf.write("\u009c\u009e\7\"\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3")
        buf.write("\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2")
        buf.write("\u00a3\5\'\24\2\u00a3\u00a4\b\13\5\2\u00a4\26\3\2\2\2")
        buf.write("\u00a5\u00ac\t\5\2\2\u00a6\u00a7\5%\23\2\u00a7\u00a8\5")
        buf.write("\37\20\2\u00a8\u00ab\3\2\2\2\u00a9\u00ab\5\37\20\2\u00aa")
        buf.write("\u00a6\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\30\3\2")
        buf.write("\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b1\5\37\20\2\u00b0\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b3\3\2\2\2\u00b3\32\3\2\2\2\u00b4\u00b6\t\6\2\2\u00b5")
        buf.write("\u00b7\t\7\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00b9\3\2\2\2\u00b8\u00ba\5\37\20\2\u00b9\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\34\3\2\2\2\u00bd\u00bf\t\b\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\36\3\2\2\2\u00c0\u00c1\t\t\2\2\u00c1")
        buf.write(" \3\2\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7w\2\2\u00c4")
        buf.write("\u00c5\7v\2\2\u00c5\u0129\7q\2\2\u00c6\u00c7\7d\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca")
        buf.write("\u0129\7m\2\2\u00cb\u00cc\7d\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7q\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7g\2\2\u00d0")
        buf.write("\u00d1\7c\2\2\u00d1\u0129\7p\2\2\u00d2\u00d3\7f\2\2\u00d3")
        buf.write("\u0129\7q\2\2\u00d4\u00d5\7g\2\2\u00d5\u00d6\7n\2\2\u00d6")
        buf.write("\u00d7\7u\2\2\u00d7\u0129\7g\2\2\u00d8\u00d9\7h\2\2\u00d9")
        buf.write("\u00da\7c\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7u\2\2\u00dc")
        buf.write("\u0129\7g\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7n\2\2\u00df")
        buf.write("\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u0129\7v\2\2\u00e2")
        buf.write("\u00e3\7h\2\2\u00e3\u00e4\7q\2\2\u00e4\u0129\7t\2\2\u00e5")
        buf.write("\u00e6\7h\2\2\u00e6\u00e7\7w\2\2\u00e7\u00e8\7p\2\2\u00e8")
        buf.write("\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb")
        buf.write("\u00ec\7q\2\2\u00ec\u0129\7p\2\2\u00ed\u00ee\7k\2\2\u00ee")
        buf.write("\u0129\7h\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1")
        buf.write("\u00f2\7v\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7i\2\2\u00f4")
        buf.write("\u00f5\7g\2\2\u00f5\u0129\7t\2\2\u00f6\u00f7\7t\2\2\u00f7")
        buf.write("\u00f8\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7w\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u0129\7p\2\2\u00fc\u00fd\7u\2\2\u00fd")
        buf.write("\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100\7k\2\2\u0100")
        buf.write("\u0101\7p\2\2\u0101\u0129\7i\2\2\u0102\u0103\7v\2\2\u0103")
        buf.write("\u0104\7t\2\2\u0104\u0105\7w\2\2\u0105\u0129\7g\2\2\u0106")
        buf.write("\u0107\7y\2\2\u0107\u0108\7j\2\2\u0108\u0109\7k\2\2\u0109")
        buf.write("\u010a\7n\2\2\u010a\u0129\7g\2\2\u010b\u010c\7x\2\2\u010c")
        buf.write("\u010d\7q\2\2\u010d\u010e\7k\2\2\u010e\u0129\7f\2\2\u010f")
        buf.write("\u0110\7q\2\2\u0110\u0111\7w\2\2\u0111\u0129\7v\2\2\u0112")
        buf.write("\u0113\7e\2\2\u0113\u0114\7q\2\2\u0114\u0115\7p\2\2\u0115")
        buf.write("\u0116\7v\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118")
        buf.write("\u0119\7w\2\2\u0119\u0129\7g\2\2\u011a\u011b\7q\2\2\u011b")
        buf.write("\u0129\7h\2\2\u011c\u011d\7k\2\2\u011d\u011e\7p\2\2\u011e")
        buf.write("\u011f\7j\2\2\u011f\u0120\7g\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7k\2\2\u0122\u0129\7v\2\2\u0123\u0124\7c\2\2\u0124")
        buf.write("\u0125\7t\2\2\u0125\u0126\7t\2\2\u0126\u0127\7c\2\2\u0127")
        buf.write("\u0129\7{\2\2\u0128\u00c2\3\2\2\2\u0128\u00c6\3\2\2\2")
        buf.write("\u0128\u00cb\3\2\2\2\u0128\u00d2\3\2\2\2\u0128\u00d4\3")
        buf.write("\2\2\2\u0128\u00d8\3\2\2\2\u0128\u00dd\3\2\2\2\u0128\u00e2")
        buf.write("\3\2\2\2\u0128\u00e5\3\2\2\2\u0128\u00ed\3\2\2\2\u0128")
        buf.write("\u00ef\3\2\2\2\u0128\u00f6\3\2\2\2\u0128\u00fc\3\2\2\2")
        buf.write("\u0128\u0102\3\2\2\2\u0128\u0106\3\2\2\2\u0128\u010b\3")
        buf.write("\2\2\2\u0128\u010f\3\2\2\2\u0128\u0112\3\2\2\2\u0128\u011a")
        buf.write("\3\2\2\2\u0128\u011c\3\2\2\2\u0128\u0123\3\2\2\2\u0129")
        buf.write("\"\3\2\2\2\u012a\u012b\7\62\2\2\u012b$\3\2\2\2\u012c\u012d")
        buf.write("\7a\2\2\u012d&\3\2\2\2\u012e\u012f\7$\2\2\u012f(\3\2\2")
        buf.write("\2\u0130\u0132\t\n\2\2\u0131\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134")
        buf.write("\u0135\3\2\2\2\u0135\u0136\b\25\2\2\u0136*\3\2\2\2\u0137")
        buf.write("\u0138\13\2\2\2\u0138\u0139\b\26\6\2\u0139,\3\2\2\2\u013a")
        buf.write("\u013b\13\2\2\2\u013b\u013c\b\27\7\2\u013c.\3\2\2\2\u013d")
        buf.write("\u013e\13\2\2\2\u013e\u013f\b\30\b\2\u013f\60\3\2\2\2")
        buf.write("\34\29GNSUioqvz|\u0081\u0083\u008b\u0098\u009d\u009f\u00aa")
        buf.write("\u00ac\u00b2\u00b6\u00bb\u00be\u0128\u0133\t\b\2\2\3\b")
        buf.write("\2\3\t\3\3\13\4\3\26\5\3\27\6\3\30\7")
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
    FLOAT = 7
    INT = 8
    BOOLEAN = 9
    STRING = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NEWLINE", "COMMENT_C", "COMMENT_CPP", "IDENTIFIER", "OPERATOR", 
            "SEPERATOR", "FLOAT", "INT", "BOOLEAN", "STRING", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "NEWLINE", "COMMENT_C", "COMMENT_CPP", "IDENTIFIER", "OPERATOR", 
                  "SEPERATOR", "FLOAT", "INT", "BOOLEAN", "STRING", "POSINT", 
                  "DECIMAL", "EXPONENT", "LETTER", "DIGIT", "KEYWORD", "ZERO", 
                  "UNDERLINE", "DB", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

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
            actions[6] = self.FLOAT_action 
            actions[7] = self.INT_action 
            actions[9] = self.STRING_action 
            actions[20] = self.ERROR_CHAR_action 
            actions[21] = self.UNCLOSE_STRING_action 
            actions[22] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

             	self.text = self.text.replace('_','').replace(' ','')

     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

             	self.text = self.text.replace('_','').replace(' ','')

     

    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     



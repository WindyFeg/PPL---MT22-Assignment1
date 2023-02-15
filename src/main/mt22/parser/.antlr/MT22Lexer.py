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
        buf.write("\u014e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\3\3\3\3\3\3\3\7\3:\n\3\f\3\16\3=")
        buf.write("\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4H\n\4\f\4")
        buf.write("\16\4K\13\4\3\4\3\4\3\5\3\5\5\5Q\n\5\3\5\3\5\3\5\7\5V")
        buf.write("\n\5\f\5\16\5Y\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6l\n\6\3\7\3\7\3")
        buf.write("\b\3\b\6\br\n\b\r\b\16\bs\3\b\3\b\3\b\5\by\n\b\3\b\3\b")
        buf.write("\6\b}\n\b\r\b\16\b~\3\b\3\b\3\b\5\b\u0084\n\b\5\b\u0086")
        buf.write("\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u008e\n\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u009b\n\n\3\13\3")
        buf.write("\13\3\13\7\13\u00a0\n\13\f\13\16\13\u00a3\13\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00ad\n\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20\7\20\u00ba")
        buf.write("\n\20\f\20\16\20\u00bd\13\20\3\21\6\21\u00c0\n\21\r\21")
        buf.write("\16\21\u00c1\3\22\3\22\5\22\u00c6\n\22\3\22\6\22\u00c9")
        buf.write("\n\22\r\22\16\22\u00ca\3\23\5\23\u00ce\n\23\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\5\25\u0138\n\25\3\26\6\26\u013b\n\26\r")
        buf.write("\26\16\26\u013c\3\26\3\26\3\27\3\27\3\27\3\30\3\30\7\30")
        buf.write("\u0146\n\30\f\30\16\30\u0149\13\30\3\30\3\30\3\31\3\31")
        buf.write("\3;\2\32\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\r-\16/\17\61")
        buf.write("\20\3\2\f\4\2\f\f\17\17\7\2##\'\',-//\61\61\13\2*+..\60")
        buf.write("\60<=??]]__}}\177\177\b\2))ddhhppttvv\3\2\63;\4\2GGgg")
        buf.write("\4\2--//\4\2C\\c|\3\2\62;\5\2\n\f\16\17\"\"\2\u017a\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\3\63\3\2\2\2\5\65\3\2\2\2\7C\3\2\2\2\tP\3\2\2")
        buf.write("\2\13k\3\2\2\2\rm\3\2\2\2\17\u0085\3\2\2\2\21\u008d\3")
        buf.write("\2\2\2\23\u009a\3\2\2\2\25\u009c\3\2\2\2\27\u00a8\3\2")
        buf.write("\2\2\31\u00ae\3\2\2\2\33\u00b0\3\2\2\2\35\u00b2\3\2\2")
        buf.write("\2\37\u00b4\3\2\2\2!\u00bf\3\2\2\2#\u00c3\3\2\2\2%\u00cd")
        buf.write("\3\2\2\2\'\u00cf\3\2\2\2)\u0137\3\2\2\2+\u013a\3\2\2\2")
        buf.write("-\u0140\3\2\2\2/\u0143\3\2\2\2\61\u014c\3\2\2\2\63\64")
        buf.write("\7\f\2\2\64\4\3\2\2\2\65\66\7\61\2\2\66\67\7,\2\2\67;")
        buf.write("\3\2\2\28:\13\2\2\298\3\2\2\2:=\3\2\2\2;<\3\2\2\2;9\3")
        buf.write("\2\2\2<>\3\2\2\2=;\3\2\2\2>?\7,\2\2?@\7\61\2\2@A\3\2\2")
        buf.write("\2AB\b\3\2\2B\6\3\2\2\2CD\7\61\2\2DE\7\61\2\2EI\3\2\2")
        buf.write("\2FH\n\2\2\2GF\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2\2J")
        buf.write("L\3\2\2\2KI\3\2\2\2LM\b\4\2\2M\b\3\2\2\2NQ\5%\23\2OQ\7")
        buf.write("a\2\2PN\3\2\2\2PO\3\2\2\2QW\3\2\2\2RV\5%\23\2SV\7a\2\2")
        buf.write("TV\5\'\24\2UR\3\2\2\2US\3\2\2\2UT\3\2\2\2VY\3\2\2\2WU")
        buf.write("\3\2\2\2WX\3\2\2\2X\n\3\2\2\2YW\3\2\2\2Zl\t\3\2\2[\\\7")
        buf.write("(\2\2\\l\7(\2\2]^\7~\2\2^l\7~\2\2_`\7?\2\2`l\7?\2\2ab")
        buf.write("\7#\2\2bl\7?\2\2cl\7>\2\2de\7>\2\2el\7?\2\2fl\7@\2\2g")
        buf.write("h\7@\2\2hl\7?\2\2ij\7<\2\2jl\7<\2\2kZ\3\2\2\2k[\3\2\2")
        buf.write("\2k]\3\2\2\2k_\3\2\2\2ka\3\2\2\2kc\3\2\2\2kd\3\2\2\2k")
        buf.write("f\3\2\2\2kg\3\2\2\2ki\3\2\2\2l\f\3\2\2\2mn\t\4\2\2n\16")
        buf.write("\3\2\2\2or\5\37\20\2pr\5\33\16\2qo\3\2\2\2qp\3\2\2\2r")
        buf.write("s\3\2\2\2sq\3\2\2\2st\3\2\2\2tu\3\2\2\2uv\7\60\2\2vx\5")
        buf.write("!\21\2wy\5#\22\2xw\3\2\2\2xy\3\2\2\2y\u0086\3\2\2\2z}")
        buf.write("\5\37\20\2{}\5\33\16\2|z\3\2\2\2|{\3\2\2\2}~\3\2\2\2~")
        buf.write("|\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0083\5")
        buf.write("#\22\2\u0081\u0082\7\60\2\2\u0082\u0084\5!\21\2\u0083")
        buf.write("\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0086\3\2\2\2")
        buf.write("\u0085q\3\2\2\2\u0085|\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0088\b\b\3\2\u0088\20\3\2\2\2\u0089\u008e\5\37\20\2")
        buf.write("\u008a\u008b\5\33\16\2\u008b\u008c\7\"\2\2\u008c\u008e")
        buf.write("\3\2\2\2\u008d\u0089\3\2\2\2\u008d\u008a\3\2\2\2\u008e")
        buf.write("\u008f\3\2\2\2\u008f\u0090\b\t\4\2\u0090\22\3\2\2\2\u0091")
        buf.write("\u0092\7v\2\2\u0092\u0093\7t\2\2\u0093\u0094\7w\2\2\u0094")
        buf.write("\u009b\7g\2\2\u0095\u0096\7h\2\2\u0096\u0097\7c\2\2\u0097")
        buf.write("\u0098\7n\2\2\u0098\u0099\7u\2\2\u0099\u009b\7g\2\2\u009a")
        buf.write("\u0091\3\2\2\2\u009a\u0095\3\2\2\2\u009b\24\3\2\2\2\u009c")
        buf.write("\u00a1\5\31\r\2\u009d\u00a0\5\27\f\2\u009e\u00a0\n\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5\31\r")
        buf.write("\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\13\5\2\u00a7\26\3")
        buf.write("\2\2\2\u00a8\u00ac\7^\2\2\u00a9\u00ad\t\5\2\2\u00aa\u00ad")
        buf.write("\3\2\2\2\u00ab\u00ad\7^\2\2\u00ac\u00a9\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\30\3\2\2\2\u00ae")
        buf.write("\u00af\7$\2\2\u00af\32\3\2\2\2\u00b0\u00b1\7\62\2\2\u00b1")
        buf.write("\34\3\2\2\2\u00b2\u00b3\7a\2\2\u00b3\36\3\2\2\2\u00b4")
        buf.write("\u00bb\t\6\2\2\u00b5\u00b6\5\35\17\2\u00b6\u00b7\5\'\24")
        buf.write("\2\u00b7\u00ba\3\2\2\2\u00b8\u00ba\5\'\24\2\u00b9\u00b5")
        buf.write("\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc \3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00be\u00c0\5\'\24\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\"\3\2\2\2\u00c3\u00c5\t\7\2\2\u00c4\u00c6")
        buf.write("\t\b\2\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c8\3\2\2\2\u00c7\u00c9\5\'\24\2\u00c8\u00c7\3\2\2")
        buf.write("\2\u00c9\u00ca\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00cb")
        buf.write("\3\2\2\2\u00cb$\3\2\2\2\u00cc\u00ce\t\t\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce&\3\2\2\2\u00cf\u00d0\t\n\2\2\u00d0(\3\2")
        buf.write("\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4")
        buf.write("\7v\2\2\u00d4\u0138\7q\2\2\u00d5\u00d6\7d\2\2\u00d6\u00d7")
        buf.write("\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7c\2\2\u00d9\u0138")
        buf.write("\7m\2\2\u00da\u00db\7d\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7q\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7g\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u0138\7p\2\2\u00e1\u00e2\7f\2\2\u00e2\u0138")
        buf.write("\7q\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7n\2\2\u00e5\u00e6")
        buf.write("\7u\2\2\u00e6\u0138\7g\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9")
        buf.write("\7c\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7u\2\2\u00eb\u0138")
        buf.write("\7g\2\2\u00ec\u00ed\7h\2\2\u00ed\u00ee\7n\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7c\2\2\u00f0\u0138\7v\2\2\u00f1\u00f2")
        buf.write("\7h\2\2\u00f2\u00f3\7q\2\2\u00f3\u0138\7t\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7w\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7e\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u0138\7p\2\2\u00fc\u00fd\7k\2\2\u00fd\u0138")
        buf.write("\7h\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7g\2\2\u0102\u0103\7i\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0138\7t\2\2\u0105\u0106\7t\2\2\u0106\u0107")
        buf.write("\7g\2\2\u0107\u0108\7v\2\2\u0108\u0109\7w\2\2\u0109\u010a")
        buf.write("\7t\2\2\u010a\u0138\7p\2\2\u010b\u010c\7u\2\2\u010c\u010d")
        buf.write("\7v\2\2\u010d\u010e\7t\2\2\u010e\u010f\7k\2\2\u010f\u0110")
        buf.write("\7p\2\2\u0110\u0138\7i\2\2\u0111\u0112\7v\2\2\u0112\u0113")
        buf.write("\7t\2\2\u0113\u0114\7w\2\2\u0114\u0138\7g\2\2\u0115\u0116")
        buf.write("\7y\2\2\u0116\u0117\7j\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7n\2\2\u0119\u0138\7g\2\2\u011a\u011b\7x\2\2\u011b\u011c")
        buf.write("\7q\2\2\u011c\u011d\7k\2\2\u011d\u0138\7f\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7w\2\2\u0120\u0138\7v\2\2\u0121\u0122")
        buf.write("\7e\2\2\u0122\u0123\7q\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7k\2\2\u0126\u0127\7p\2\2\u0127\u0128")
        buf.write("\7w\2\2\u0128\u0138\7g\2\2\u0129\u012a\7q\2\2\u012a\u0138")
        buf.write("\7h\2\2\u012b\u012c\7k\2\2\u012c\u012d\7p\2\2\u012d\u012e")
        buf.write("\7j\2\2\u012e\u012f\7g\2\2\u012f\u0130\7t\2\2\u0130\u0131")
        buf.write("\7k\2\2\u0131\u0138\7v\2\2\u0132\u0133\7c\2\2\u0133\u0134")
        buf.write("\7t\2\2\u0134\u0135\7t\2\2\u0135\u0136\7c\2\2\u0136\u0138")
        buf.write("\7{\2\2\u0137\u00d1\3\2\2\2\u0137\u00d5\3\2\2\2\u0137")
        buf.write("\u00da\3\2\2\2\u0137\u00e1\3\2\2\2\u0137\u00e3\3\2\2\2")
        buf.write("\u0137\u00e7\3\2\2\2\u0137\u00ec\3\2\2\2\u0137\u00f1\3")
        buf.write("\2\2\2\u0137\u00f4\3\2\2\2\u0137\u00fc\3\2\2\2\u0137\u00fe")
        buf.write("\3\2\2\2\u0137\u0105\3\2\2\2\u0137\u010b\3\2\2\2\u0137")
        buf.write("\u0111\3\2\2\2\u0137\u0115\3\2\2\2\u0137\u011a\3\2\2\2")
        buf.write("\u0137\u011e\3\2\2\2\u0137\u0121\3\2\2\2\u0137\u0129\3")
        buf.write("\2\2\2\u0137\u012b\3\2\2\2\u0137\u0132\3\2\2\2\u0138*")
        buf.write("\3\2\2\2\u0139\u013b\t\13\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013a\3\2\2\2\u013c\u013d\3\2\2\2")
        buf.write("\u013d\u013e\3\2\2\2\u013e\u013f\b\26\2\2\u013f,\3\2\2")
        buf.write("\2\u0140\u0141\13\2\2\2\u0141\u0142\b\27\6\2\u0142.\3")
        buf.write("\2\2\2\u0143\u0147\5\31\r\2\u0144\u0146\n\2\2\2\u0145")
        buf.write("\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148\u014a\3\2\2\2\u0149\u0147\3")
        buf.write("\2\2\2\u014a\u014b\b\30\7\2\u014b\60\3\2\2\2\u014c\u014d")
        buf.write("\13\2\2\2\u014d\62\3\2\2\2\36\2;IPUWkqsx|~\u0083\u0085")
        buf.write("\u008d\u009a\u009f\u00a1\u00ac\u00b9\u00bb\u00c1\u00c5")
        buf.write("\u00ca\u00cd\u0137\u013c\u0147\b\b\2\2\3\b\2\3\t\3\3\13")
        buf.write("\4\3\27\5\3\30\6")
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
                  "SEPERATOR", "FLOAT", "INT", "BOOLEAN", "STRING", "ESCAPE", 
                  "DB", "ZERO", "UNDERLINE", "POSINT", "DECIMAL", "EXPONENT", 
                  "LETTER", "DIGIT", "KEYWORD", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[21] = self.ERROR_CHAR_action 
            actions[22] = self.UNCLOSE_STRING_action 
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

                self.text = self.text[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise UncloseString(self.text[1:])
     



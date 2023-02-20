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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0200\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3")
        buf.write("\2\3\2\7\2\u009a\n\2\f\2\16\2\u009d\13\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b3\n\4\3\5\3\5\3\5\7")
        buf.write("\5\u00b8\n\5\f\5\16\5\u00bb\13\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\5\35\u0145\n\35\3\36\6\36\u0148\n")
        buf.write("\36\r\36\16\36\u0149\3\37\3\37\5\37\u014e\n\37\3\37\6")
        buf.write("\37\u0151\n\37\r\37\16\37\u0152\3 \3 \6 \u0157\n \r \16")
        buf.write(" \u0158\3 \3 \3 \5 \u015e\n \3 \3 \6 \u0162\n \r \16 ")
        buf.write("\u0163\3 \3 \3 \3 \5 \u016a\n \5 \u016c\n \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\7!\u0175\n!\f!\16!\u0178\13!\3\"\3\"\5\"\u017c")
        buf.write("\n\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0185\n#\3$\3$\3%\5%\u018a")
        buf.write("\n%\3&\3&\5&\u018e\n&\3&\3&\3&\7&\u0193\n&\f&\16&\u0196")
        buf.write("\13&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u01b2")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01b9\n\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3")
        buf.write("@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3")
        buf.write("G\6G\u01ec\nG\rG\16G\u01ed\3G\3G\3H\3H\3H\3I\3I\3I\7I")
        buf.write("\u01f8\nI\fI\16I\u01fb\13I\3I\3I\3J\3J\3\u009b\2K\3\3")
        buf.write("\5\4\7\2\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33")
        buf.write("\16\35\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31")
        buf.write("\63\32\65\33\67\349\35;\2=\2?\36A\2C\37E G\2I\2K!M\"O")
        buf.write("#Q$S%U&W\'Y([)]*_+a,c\2e\2g-i.k/m\60o\61q\62s\63u\64w")
        buf.write("\65y\66{\67}8\1779\u0081:\u0083;\u0085<\u0087=\u0089>")
        buf.write("\u008b?\u008d@\u008fA\u0091B\u0093C\3\2\r\4\2\f\f\17\17")
        buf.write("\b\2))ddhhppttvv\4\2$$^^\6\2\f\f\17\17$$^^\4\2GGgg\4\2")
        buf.write("--//\3\2\63;\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\5\2\f")
        buf.write("\f\17\17$$\2\u0217\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2?\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\3\u0095\3\2\2\2\5\u00a3\3\2\2\2\7\u00ae\3\2\2")
        buf.write("\2\t\u00b4\3\2\2\2\13\u00c0\3\2\2\2\r\u00c2\3\2\2\2\17")
        buf.write("\u00c7\3\2\2\2\21\u00cd\3\2\2\2\23\u00d5\3\2\2\2\25\u00d8")
        buf.write("\3\2\2\2\27\u00dd\3\2\2\2\31\u00e3\3\2\2\2\33\u00e7\3")
        buf.write("\2\2\2\35\u00f0\3\2\2\2\37\u00f3\3\2\2\2!\u00fb\3\2\2")
        buf.write("\2#\u0102\3\2\2\2%\u0109\3\2\2\2\'\u010f\3\2\2\2)\u0114")
        buf.write("\3\2\2\2+\u0118\3\2\2\2-\u0121\3\2\2\2/\u0124\3\2\2\2")
        buf.write("\61\u012c\3\2\2\2\63\u0132\3\2\2\2\65\u0137\3\2\2\2\67")
        buf.write("\u013d\3\2\2\29\u0144\3\2\2\2;\u0147\3\2\2\2=\u014b\3")
        buf.write("\2\2\2?\u016b\3\2\2\2A\u016f\3\2\2\2C\u017b\3\2\2\2E\u0184")
        buf.write("\3\2\2\2G\u0186\3\2\2\2I\u0189\3\2\2\2K\u018d\3\2\2\2")
        buf.write("M\u0197\3\2\2\2O\u0199\3\2\2\2Q\u019b\3\2\2\2S\u019d\3")
        buf.write("\2\2\2U\u019f\3\2\2\2W\u01a1\3\2\2\2Y\u01a3\3\2\2\2[\u01a5")
        buf.write("\3\2\2\2]\u01a7\3\2\2\2_\u01a9\3\2\2\2a\u01ab\3\2\2\2")
        buf.write("c\u01b1\3\2\2\2e\u01b8\3\2\2\2g\u01ba\3\2\2\2i\u01bf\3")
        buf.write("\2\2\2k\u01c1\3\2\2\2m\u01c3\3\2\2\2o\u01c5\3\2\2\2q\u01c7")
        buf.write("\3\2\2\2s\u01c9\3\2\2\2u\u01cb\3\2\2\2w\u01cd\3\2\2\2")
        buf.write("y\u01cf\3\2\2\2{\u01d1\3\2\2\2}\u01d4\3\2\2\2\177\u01d7")
        buf.write("\3\2\2\2\u0081\u01da\3\2\2\2\u0083\u01dd\3\2\2\2\u0085")
        buf.write("\u01df\3\2\2\2\u0087\u01e2\3\2\2\2\u0089\u01e4\3\2\2\2")
        buf.write("\u008b\u01e7\3\2\2\2\u008d\u01eb\3\2\2\2\u008f\u01f1\3")
        buf.write("\2\2\2\u0091\u01f4\3\2\2\2\u0093\u01fe\3\2\2\2\u0095\u0096")
        buf.write("\7\61\2\2\u0096\u0097\7,\2\2\u0097\u009b\3\2\2\2\u0098")
        buf.write("\u009a\13\2\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2")
        buf.write("\2\u009b\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e")
        buf.write("\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7,\2\2\u009f")
        buf.write("\u00a0\7\61\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\b\2\2")
        buf.write("\2\u00a2\4\3\2\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\7")
        buf.write("\61\2\2\u00a5\u00a9\3\2\2\2\u00a6\u00a8\n\2\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3")
        buf.write("\2\2\2\u00ac\u00ad\b\3\2\2\u00ad\6\3\2\2\2\u00ae\u00b2")
        buf.write("\7^\2\2\u00af\u00b3\t\3\2\2\u00b0\u00b3\5i\65\2\u00b1")
        buf.write("\u00b3\t\4\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b1\3\2\2\2\u00b3\b\3\2\2\2\u00b4\u00b9\5i\65")
        buf.write("\2\u00b5\u00b8\5\7\4\2\u00b6\u00b8\n\5\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bc\u00bd\5i\65\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00bf\b\5\3\2\u00bf\n\3\2\2\2\u00c0\u00c1")
        buf.write("\5\u008bF\2\u00c1\f\3\2\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7w\2\2\u00c4\u00c5\7v\2\2\u00c5\u00c6\7q\2\2\u00c6\16")
        buf.write("\3\2\2\2\u00c7\u00c8\7d\2\2\u00c8\u00c9\7t\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7m\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7d\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7c\2\2\u00d3\u00d4\7p\2\2\u00d4\22\3\2\2\2\u00d5\u00d6")
        buf.write("\7f\2\2\u00d6\u00d7\7q\2\2\u00d7\24\3\2\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc")
        buf.write("\7g\2\2\u00dc\26\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df")
        buf.write("\7n\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7v\2\2\u00e2\30\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5")
        buf.write("\7q\2\2\u00e5\u00e6\7t\2\2\u00e6\32\3\2\2\2\u00e7\u00e8")
        buf.write("\7h\2\2\u00e8\u00e9\7w\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb")
        buf.write("\7e\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7q\2\2\u00ee\u00ef\7p\2\2\u00ef\34\3\2\2\2\u00f0\u00f1")
        buf.write("\7k\2\2\u00f1\u00f2\7h\2\2\u00f2\36\3\2\2\2\u00f3\u00f4")
        buf.write("\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7\u00f8\7i\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa \3\2\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd")
        buf.write("\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7p\2\2\u0101\"\3\2\2\2\u0102\u0103")
        buf.write("\7u\2\2\u0103\u0104\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108\7i\2\2\u0108$\3")
        buf.write("\2\2\2\u0109\u010a\7y\2\2\u010a\u010b\7j\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7n\2\2\u010d\u010e\7g\2\2\u010e&\3")
        buf.write("\2\2\2\u010f\u0110\7x\2\2\u0110\u0111\7q\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7f\2\2\u0113(\3\2\2\2\u0114\u0115")
        buf.write("\7q\2\2\u0115\u0116\7w\2\2\u0116\u0117\7v\2\2\u0117*\3")
        buf.write("\2\2\2\u0118\u0119\7e\2\2\u0119\u011a\7q\2\2\u011a\u011b")
        buf.write("\7p\2\2\u011b\u011c\7v\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7w\2\2\u011f\u0120\7g\2\2\u0120,\3")
        buf.write("\2\2\2\u0121\u0122\7q\2\2\u0122\u0123\7h\2\2\u0123.\3")
        buf.write("\2\2\2\u0124\u0125\7k\2\2\u0125\u0126\7p\2\2\u0126\u0127")
        buf.write("\7j\2\2\u0127\u0128\7g\2\2\u0128\u0129\7t\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7v\2\2\u012b\60\3\2\2\2\u012c\u012d")
        buf.write("\7c\2\2\u012d\u012e\7t\2\2\u012e\u012f\7t\2\2\u012f\u0130")
        buf.write("\7c\2\2\u0130\u0131\7{\2\2\u0131\62\3\2\2\2\u0132\u0133")
        buf.write("\7o\2\2\u0133\u0134\7c\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\7p\2\2\u0136\64\3\2\2\2\u0137\u0138\7h\2\2\u0138\u0139")
        buf.write("\7c\2\2\u0139\u013a\7n\2\2\u013a\u013b\7u\2\2\u013b\u013c")
        buf.write("\7g\2\2\u013c\66\3\2\2\2\u013d\u013e\7v\2\2\u013e\u013f")
        buf.write("\7t\2\2\u013f\u0140\7w\2\2\u0140\u0141\7g\2\2\u01418\3")
        buf.write("\2\2\2\u0142\u0145\5\65\33\2\u0143\u0145\5\67\34\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145:\3\2\2\2\u0146")
        buf.write("\u0148\5G$\2\u0147\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a<\3\2\2\2\u014b")
        buf.write("\u014d\t\6\2\2\u014c\u014e\t\7\2\2\u014d\u014c\3\2\2\2")
        buf.write("\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2\u014f\u0151\5")
        buf.write("G$\2\u0150\u014f\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0152\u0153\3\2\2\2\u0153>\3\2\2\2\u0154\u0157")
        buf.write("\5A!\2\u0155\u0157\5k\66\2\u0156\u0154\3\2\2\2\u0156\u0155")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015b\5S*\2\u015b")
        buf.write("\u015d\5;\36\2\u015c\u015e\5=\37\2\u015d\u015c\3\2\2\2")
        buf.write("\u015d\u015e\3\2\2\2\u015e\u016c\3\2\2\2\u015f\u0162\5")
        buf.write("A!\2\u0160\u0162\5k\66\2\u0161\u015f\3\2\2\2\u0161\u0160")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0164\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0169\5=\37\2")
        buf.write("\u0166\u0167\5S*\2\u0167\u0168\5;\36\2\u0168\u016a\3\2")
        buf.write("\2\2\u0169\u0166\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c")
        buf.write("\3\2\2\2\u016b\u0156\3\2\2\2\u016b\u0161\3\2\2\2\u016c")
        buf.write("\u016d\3\2\2\2\u016d\u016e\b \4\2\u016e@\3\2\2\2\u016f")
        buf.write("\u0176\t\b\2\2\u0170\u0171\5m\67\2\u0171\u0172\5G$\2\u0172")
        buf.write("\u0175\3\2\2\2\u0173\u0175\5G$\2\u0174\u0170\3\2\2\2\u0174")
        buf.write("\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177B\3\2\2\2\u0178\u0176\3\2\2")
        buf.write("\2\u0179\u017c\5A!\2\u017a\u017c\5k\66\2\u017b\u0179\3")
        buf.write("\2\2\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e")
        buf.write("\b\"\5\2\u017eD\3\2\2\2\u017f\u0180\5C\"\2\u0180\u0181")
        buf.write("\5M\'\2\u0181\u0182\5E#\2\u0182\u0185\3\2\2\2\u0183\u0185")
        buf.write("\5C\"\2\u0184\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("F\3\2\2\2\u0186\u0187\t\t\2\2\u0187H\3\2\2\2\u0188\u018a")
        buf.write("\t\n\2\2\u0189\u0188\3\2\2\2\u018aJ\3\2\2\2\u018b\u018e")
        buf.write("\5I%\2\u018c\u018e\5m\67\2\u018d\u018b\3\2\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0194\3\2\2\2\u018f\u0193\5I%\2\u0190\u0193")
        buf.write("\5m\67\2\u0191\u0193\5G$\2\u0192\u018f\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195L\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0197\u0198\7.\2\2\u0198N\3\2\2\2\u0199")
        buf.write("\u019a\7<\2\2\u019aP\3\2\2\2\u019b\u019c\7=\2\2\u019c")
        buf.write("R\3\2\2\2\u019d\u019e\7\60\2\2\u019eT\3\2\2\2\u019f\u01a0")
        buf.write("\7]\2\2\u01a0V\3\2\2\2\u01a1\u01a2\7_\2\2\u01a2X\3\2\2")
        buf.write("\2\u01a3\u01a4\7*\2\2\u01a4Z\3\2\2\2\u01a5\u01a6\7+\2")
        buf.write("\2\u01a6\\\3\2\2\2\u01a7\u01a8\7}\2\2\u01a8^\3\2\2\2\u01a9")
        buf.write("\u01aa\7\177\2\2\u01aa`\3\2\2\2\u01ab\u01ac\7?\2\2\u01ac")
        buf.write("b\3\2\2\2\u01ad\u01b2\5\t\5\2\u01ae\u01b2\5? \2\u01af")
        buf.write("\u01b2\5C\"\2\u01b0\u01b2\5K&\2\u01b1\u01ad\3\2\2\2\u01b1")
        buf.write("\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2")
        buf.write("\u01b2d\3\2\2\2\u01b3\u01b4\5c\62\2\u01b4\u01b5\5M\'\2")
        buf.write("\u01b5\u01b6\5e\63\2\u01b6\u01b9\3\2\2\2\u01b7\u01b9\5")
        buf.write("c\62\2\u01b8\u01b3\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9f")
        buf.write("\3\2\2\2\u01ba\u01bb\5]/\2\u01bb\u01bc\5e\63\2\u01bc\u01bd")
        buf.write("\5_\60\2\u01bd\u01be\b\64\6\2\u01beh\3\2\2\2\u01bf\u01c0")
        buf.write("\7$\2\2\u01c0j\3\2\2\2\u01c1\u01c2\7\62\2\2\u01c2l\3\2")
        buf.write("\2\2\u01c3\u01c4\7a\2\2\u01c4n\3\2\2\2\u01c5\u01c6\7-")
        buf.write("\2\2\u01c6p\3\2\2\2\u01c7\u01c8\7/\2\2\u01c8r\3\2\2\2")
        buf.write("\u01c9\u01ca\7,\2\2\u01cat\3\2\2\2\u01cb\u01cc\7\61\2")
        buf.write("\2\u01ccv\3\2\2\2\u01cd\u01ce\7\'\2\2\u01cex\3\2\2\2\u01cf")
        buf.write("\u01d0\7#\2\2\u01d0z\3\2\2\2\u01d1\u01d2\7(\2\2\u01d2")
        buf.write("\u01d3\7(\2\2\u01d3|\3\2\2\2\u01d4\u01d5\7~\2\2\u01d5")
        buf.write("\u01d6\7~\2\2\u01d6~\3\2\2\2\u01d7\u01d8\7?\2\2\u01d8")
        buf.write("\u01d9\7?\2\2\u01d9\u0080\3\2\2\2\u01da\u01db\7#\2\2\u01db")
        buf.write("\u01dc\7?\2\2\u01dc\u0082\3\2\2\2\u01dd\u01de\7>\2\2\u01de")
        buf.write("\u0084\3\2\2\2\u01df\u01e0\7>\2\2\u01e0\u01e1\7?\2\2\u01e1")
        buf.write("\u0086\3\2\2\2\u01e2\u01e3\7@\2\2\u01e3\u0088\3\2\2\2")
        buf.write("\u01e4\u01e5\7@\2\2\u01e5\u01e6\7?\2\2\u01e6\u008a\3\2")
        buf.write("\2\2\u01e7\u01e8\7<\2\2\u01e8\u01e9\7<\2\2\u01e9\u008c")
        buf.write("\3\2\2\2\u01ea\u01ec\t\13\2\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f0\bG\2\2\u01f0\u008e\3")
        buf.write("\2\2\2\u01f1\u01f2\13\2\2\2\u01f2\u01f3\bH\7\2\u01f3\u0090")
        buf.write("\3\2\2\2\u01f4\u01f9\5i\65\2\u01f5\u01f8\5\7\4\2\u01f6")
        buf.write("\u01f8\n\f\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2")
        buf.write("\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3")
        buf.write("\2\2\2\u01fa\u01fc\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd")
        buf.write("\bI\b\2\u01fd\u0092\3\2\2\2\u01fe\u01ff\13\2\2\2\u01ff")
        buf.write("\u0094\3\2\2\2 \2\u009b\u00a9\u00b2\u00b7\u00b9\u0144")
        buf.write("\u0149\u014d\u0152\u0156\u0158\u015d\u0161\u0163\u0169")
        buf.write("\u016b\u0174\u0176\u017b\u0184\u0189\u018d\u0192\u0194")
        buf.write("\u01b1\u01b8\u01ed\u01f7\u01f9\t\b\2\2\3\5\2\3 \3\3\"")
        buf.write("\4\3\64\5\3H\6\3I\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPP = 2
    STR = 3
    STRTYP = 4
    AUTO = 5
    BREAK = 6
    BOOLEAN = 7
    DO = 8
    ELSE = 9
    FLOAT = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    INTEGER = 14
    RETURN = 15
    STRING = 16
    WHILE = 17
    VOID = 18
    OUT = 19
    CONTINUE = 20
    OF = 21
    INHERIT = 22
    ARRAY = 23
    MAIN = 24
    FALSE = 25
    TRUE = 26
    BOOL = 27
    FLO = 28
    INT = 29
    DEMENTION = 30
    ID = 31
    COMA = 32
    COL = 33
    SEM = 34
    DOT = 35
    LSB = 36
    RSB = 37
    LB = 38
    RB = 39
    LCB = 40
    RCB = 41
    EQU = 42
    ARR = 43
    DB = 44
    ZERO = 45
    UNDE = 46
    PLUS = 47
    MINU = 48
    MUTI = 49
    DIVI = 50
    MODU = 51
    NOT = 52
    AND = 53
    OR = 54
    EQUL = 55
    NEQ = 56
    LESS = 57
    LOEQ = 58
    GREA = 59
    GOEQ = 60
    SCOPE = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'main'", "'false'", "'true'", "','", "':'", "';'", 
            "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'\"'", 
            "'0'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPP", "STR", "STRTYP", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
            "INHERIT", "ARRAY", "MAIN", "FALSE", "TRUE", "BOOL", "FLO", 
            "INT", "DEMENTION", "ID", "COMA", "COL", "SEM", "DOT", "LSB", 
            "RSB", "LB", "RB", "LCB", "RCB", "EQU", "ARR", "DB", "ZERO", 
            "UNDE", "PLUS", "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", 
            "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR", "STRTYP", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "MAIN", 
                  "FALSE", "TRUE", "BOOL", "DECIMAL", "EXPONENT", "FLO", 
                  "POSINT", "INT", "DEMENTION", "DIGIT", "LETTER", "ID", 
                  "COMA", "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", 
                  "LCB", "RCB", "EQU", "EXPR", "EXPRESSTIONS", "ARR", "DB", 
                  "ZERO", "UNDE", "PLUS", "MINU", "MUTI", "DIVI", "MODU", 
                  "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", 
                  "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[3] = self.STR_action 
            actions[30] = self.FLO_action 
            actions[32] = self.INT_action 
            actions[50] = self.ARR_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def FLO_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def ARR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace(' ','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise UncloseString(self.text[1:])
     



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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01f8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\3\2\3\2\3\2\3\2\7\2\u0094\n")
        buf.write("\2\f\2\16\2\u0097\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\7\3\u00a2\n\3\f\3\16\3\u00a5\13\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u00ad\n\4\3\5\3\5\3\5\7\5\u00b2\n\5\f\5\16")
        buf.write("\5\u00b5\13\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u0138\n\33\3\34\6\34\u013b\n\34\r")
        buf.write("\34\16\34\u013c\3\35\3\35\5\35\u0141\n\35\3\35\6\35\u0144")
        buf.write("\n\35\r\35\16\35\u0145\3\36\3\36\6\36\u014a\n\36\r\36")
        buf.write("\16\36\u014b\3\36\3\36\3\36\5\36\u0151\n\36\3\36\3\36")
        buf.write("\6\36\u0155\n\36\r\36\16\36\u0156\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u015d\n\36\5\36\u015f\n\36\3\36\3\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\7\37\u0168\n\37\f\37\16\37\u016b\13\37\3")
        buf.write(" \3 \5 \u016f\n \3 \3 \3!\3!\3\"\5\"\u0176\n\"\3#\3#\5")
        buf.write("#\u017a\n#\3#\3#\3#\7#\u017f\n#\f#\16#\u0182\13#\3$\3")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3/\3/\5/\u019e\n/\3\60\3\60\7\60\u01a2")
        buf.write("\n\60\f\60\16\60\u01a5\13\60\3\60\3\60\7\60\u01a9\n\60")
        buf.write("\f\60\16\60\u01ac\13\60\3\60\3\60\3\60\5\60\u01b1\n\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3;\3<\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3C\3D\6D\u01e4\nD\rD\16D\u01e5\3D\3D\3E")
        buf.write("\3E\3E\3F\3F\3F\7F\u01f0\nF\fF\16F\u01f3\13F\3F\3F\3G")
        buf.write("\3G\3\u0095\2H\3\3\5\4\7\2\t\5\13\6\r\7\17\b\21\t\23\n")
        buf.write("\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)\25")
        buf.write("+\26-\27/\30\61\31\63\32\65\33\67\29\2;\34=\2?\35A\2C")
        buf.write("\2E\36G\37I K!M\"O#Q$S%U&W\'Y([)]\2_\2a*c+e,g-i.k/m\60")
        buf.write("o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081:\u0083;\u0085")
        buf.write("<\u0087=\u0089>\u008b?\u008d@\3\2\r\4\2\f\f\17\17\b\2")
        buf.write("))ddhhppttvv\4\2$$^^\6\2\f\f\17\17$$^^\4\2GGgg\4\2--/")
        buf.write("/\3\2\63;\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\5\2\f\f")
        buf.write("\17\17$$\2\u0210\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write(";\3\2\2\2\2?\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2")
        buf.write("\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3")
        buf.write("\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2")
        buf.write("\2\u008d\3\2\2\2\3\u008f\3\2\2\2\5\u009d\3\2\2\2\7\u00a8")
        buf.write("\3\2\2\2\t\u00ae\3\2\2\2\13\u00ba\3\2\2\2\r\u00bf\3\2")
        buf.write("\2\2\17\u00c5\3\2\2\2\21\u00cd\3\2\2\2\23\u00d0\3\2\2")
        buf.write("\2\25\u00d5\3\2\2\2\27\u00db\3\2\2\2\31\u00df\3\2\2\2")
        buf.write("\33\u00e8\3\2\2\2\35\u00eb\3\2\2\2\37\u00f3\3\2\2\2!\u00fa")
        buf.write("\3\2\2\2#\u0101\3\2\2\2%\u0107\3\2\2\2\'\u010c\3\2\2\2")
        buf.write(")\u0110\3\2\2\2+\u0119\3\2\2\2-\u011c\3\2\2\2/\u0124\3")
        buf.write("\2\2\2\61\u012a\3\2\2\2\63\u0130\3\2\2\2\65\u0137\3\2")
        buf.write("\2\2\67\u013a\3\2\2\29\u013e\3\2\2\2;\u015e\3\2\2\2=\u0162")
        buf.write("\3\2\2\2?\u016e\3\2\2\2A\u0172\3\2\2\2C\u0175\3\2\2\2")
        buf.write("E\u0179\3\2\2\2G\u0183\3\2\2\2I\u0185\3\2\2\2K\u0187\3")
        buf.write("\2\2\2M\u0189\3\2\2\2O\u018b\3\2\2\2Q\u018d\3\2\2\2S\u018f")
        buf.write("\3\2\2\2U\u0191\3\2\2\2W\u0193\3\2\2\2Y\u0195\3\2\2\2")
        buf.write("[\u0197\3\2\2\2]\u019d\3\2\2\2_\u01b0\3\2\2\2a\u01b2\3")
        buf.write("\2\2\2c\u01b7\3\2\2\2e\u01b9\3\2\2\2g\u01bb\3\2\2\2i\u01bd")
        buf.write("\3\2\2\2k\u01bf\3\2\2\2m\u01c1\3\2\2\2o\u01c3\3\2\2\2")
        buf.write("q\u01c5\3\2\2\2s\u01c7\3\2\2\2u\u01c9\3\2\2\2w\u01cc\3")
        buf.write("\2\2\2y\u01cf\3\2\2\2{\u01d2\3\2\2\2}\u01d5\3\2\2\2\177")
        buf.write("\u01d7\3\2\2\2\u0081\u01da\3\2\2\2\u0083\u01dc\3\2\2\2")
        buf.write("\u0085\u01df\3\2\2\2\u0087\u01e3\3\2\2\2\u0089\u01e9\3")
        buf.write("\2\2\2\u008b\u01ec\3\2\2\2\u008d\u01f6\3\2\2\2\u008f\u0090")
        buf.write("\7\61\2\2\u0090\u0091\7,\2\2\u0091\u0095\3\2\2\2\u0092")
        buf.write("\u0094\13\2\2\2\u0093\u0092\3\2\2\2\u0094\u0097\3\2\2")
        buf.write("\2\u0095\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7,\2\2\u0099")
        buf.write("\u009a\7\61\2\2\u009a\u009b\3\2\2\2\u009b\u009c\b\2\2")
        buf.write("\2\u009c\4\3\2\2\2\u009d\u009e\7\61\2\2\u009e\u009f\7")
        buf.write("\61\2\2\u009f\u00a3\3\2\2\2\u00a0\u00a2\n\2\2\2\u00a1")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2\u00a3\u00a1\3\2\2\2")
        buf.write("\u00a3\u00a4\3\2\2\2\u00a4\u00a6\3\2\2\2\u00a5\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a7\b\3\2\2\u00a7\6\3\2\2\2\u00a8\u00ac")
        buf.write("\7^\2\2\u00a9\u00ad\t\3\2\2\u00aa\u00ad\5c\62\2\u00ab")
        buf.write("\u00ad\t\4\2\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\b\3\2\2\2\u00ae\u00b3\5c\62")
        buf.write("\2\u00af\u00b2\5\7\4\2\u00b0\u00b2\n\5\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b6\u00b7\5c\62\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00b9\b\5\3\2\u00b9\n\3\2\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7v\2\2\u00bd\u00be")
        buf.write("\7q\2\2\u00be\f\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1")
        buf.write("\7t\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4")
        buf.write("\7m\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6\u00c7")
        buf.write("\7q\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7n\2\2\u00c9\u00ca")
        buf.write("\7g\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7p\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf\7q\2\2\u00cf\22")
        buf.write("\3\2\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3")
        buf.write("\7u\2\2\u00d3\u00d4\7g\2\2\u00d4\24\3\2\2\2\u00d5\u00d6")
        buf.write("\7h\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7q\2\2\u00d8\u00d9")
        buf.write("\7c\2\2\u00d9\u00da\7v\2\2\u00da\26\3\2\2\2\u00db\u00dc")
        buf.write("\7h\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7t\2\2\u00de\30")
        buf.write("\3\2\2\2\u00df\u00e0\7h\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2")
        buf.write("\7p\2\2\u00e2\u00e3\7e\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5")
        buf.write("\7k\2\2\u00e5\u00e6\7q\2\2\u00e6\u00e7\7p\2\2\u00e7\32")
        buf.write("\3\2\2\2\u00e8\u00e9\7k\2\2\u00e9\u00ea\7h\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7i\2\2\u00f0\u00f1")
        buf.write("\7g\2\2\u00f1\u00f2\7t\2\2\u00f2\36\3\2\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7v\2\2\u00f6\u00f7")
        buf.write("\7w\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9\7p\2\2\u00f9 \3")
        buf.write("\2\2\2\u00fa\u00fb\7u\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd")
        buf.write("\7t\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100")
        buf.write("\7i\2\2\u0100\"\3\2\2\2\u0101\u0102\7y\2\2\u0102\u0103")
        buf.write("\7j\2\2\u0103\u0104\7k\2\2\u0104\u0105\7n\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106$\3\2\2\2\u0107\u0108\7x\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7k\2\2\u010a\u010b\7f\2\2\u010b&\3")
        buf.write("\2\2\2\u010c\u010d\7q\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7v\2\2\u010f(\3\2\2\2\u0110\u0111\7e\2\2\u0111\u0112")
        buf.write("\7q\2\2\u0112\u0113\7p\2\2\u0113\u0114\7v\2\2\u0114\u0115")
        buf.write("\7k\2\2\u0115\u0116\7p\2\2\u0116\u0117\7w\2\2\u0117\u0118")
        buf.write("\7g\2\2\u0118*\3\2\2\2\u0119\u011a\7q\2\2\u011a\u011b")
        buf.write("\7h\2\2\u011b,\3\2\2\2\u011c\u011d\7k\2\2\u011d\u011e")
        buf.write("\7p\2\2\u011e\u011f\7j\2\2\u011f\u0120\7g\2\2\u0120\u0121")
        buf.write("\7t\2\2\u0121\u0122\7k\2\2\u0122\u0123\7v\2\2\u0123.\3")
        buf.write("\2\2\2\u0124\u0125\7c\2\2\u0125\u0126\7t\2\2\u0126\u0127")
        buf.write("\7t\2\2\u0127\u0128\7c\2\2\u0128\u0129\7{\2\2\u0129\60")
        buf.write("\3\2\2\2\u012a\u012b\7h\2\2\u012b\u012c\7c\2\2\u012c\u012d")
        buf.write("\7n\2\2\u012d\u012e\7u\2\2\u012e\u012f\7g\2\2\u012f\62")
        buf.write("\3\2\2\2\u0130\u0131\7v\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7w\2\2\u0133\u0134\7g\2\2\u0134\64\3\2\2\2\u0135\u0138")
        buf.write("\5\61\31\2\u0136\u0138\5\63\32\2\u0137\u0135\3\2\2\2\u0137")
        buf.write("\u0136\3\2\2\2\u0138\66\3\2\2\2\u0139\u013b\5A!\2\u013a")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013a\3\2\2\2")
        buf.write("\u013c\u013d\3\2\2\2\u013d8\3\2\2\2\u013e\u0140\t\6\2")
        buf.write("\2\u013f\u0141\t\7\2\2\u0140\u013f\3\2\2\2\u0140\u0141")
        buf.write("\3\2\2\2\u0141\u0143\3\2\2\2\u0142\u0144\5A!\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146:\3\2\2\2\u0147\u014a\5=\37\2\u0148")
        buf.write("\u014a\5e\63\2\u0149\u0147\3\2\2\2\u0149\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c\u014d\3\2\2\2\u014d\u014e\5M\'\2\u014e\u0150")
        buf.write("\5\67\34\2\u014f\u0151\59\35\2\u0150\u014f\3\2\2\2\u0150")
        buf.write("\u0151\3\2\2\2\u0151\u015f\3\2\2\2\u0152\u0155\5=\37\2")
        buf.write("\u0153\u0155\5e\63\2\u0154\u0152\3\2\2\2\u0154\u0153\3")
        buf.write("\2\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u015c\59\35\2\u0159")
        buf.write("\u015a\5M\'\2\u015a\u015b\5\67\34\2\u015b\u015d\3\2\2")
        buf.write("\2\u015c\u0159\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f")
        buf.write("\3\2\2\2\u015e\u0149\3\2\2\2\u015e\u0154\3\2\2\2\u015f")
        buf.write("\u0160\3\2\2\2\u0160\u0161\b\36\4\2\u0161<\3\2\2\2\u0162")
        buf.write("\u0169\t\b\2\2\u0163\u0164\5g\64\2\u0164\u0165\5A!\2\u0165")
        buf.write("\u0168\3\2\2\2\u0166\u0168\5A!\2\u0167\u0163\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a>\3\2\2\2\u016b\u0169\3\2\2")
        buf.write("\2\u016c\u016f\5=\37\2\u016d\u016f\5e\63\2\u016e\u016c")
        buf.write("\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0171\b \5\2\u0171@\3\2\2\2\u0172\u0173\t\t\2\2\u0173")
        buf.write("B\3\2\2\2\u0174\u0176\t\n\2\2\u0175\u0174\3\2\2\2\u0176")
        buf.write("D\3\2\2\2\u0177\u017a\5C\"\2\u0178\u017a\5g\64\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u0178\3\2\2\2\u017a\u0180\3\2\2\2")
        buf.write("\u017b\u017f\5C\"\2\u017c\u017f\5g\64\2\u017d\u017f\5")
        buf.write("A!\2\u017e\u017b\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017d")
        buf.write("\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181F\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("\u0184\7.\2\2\u0184H\3\2\2\2\u0185\u0186\7<\2\2\u0186")
        buf.write("J\3\2\2\2\u0187\u0188\7=\2\2\u0188L\3\2\2\2\u0189\u018a")
        buf.write("\7\60\2\2\u018aN\3\2\2\2\u018b\u018c\7]\2\2\u018cP\3\2")
        buf.write("\2\2\u018d\u018e\7_\2\2\u018eR\3\2\2\2\u018f\u0190\7*")
        buf.write("\2\2\u0190T\3\2\2\2\u0191\u0192\7+\2\2\u0192V\3\2\2\2")
        buf.write("\u0193\u0194\7}\2\2\u0194X\3\2\2\2\u0195\u0196\7\177\2")
        buf.write("\2\u0196Z\3\2\2\2\u0197\u0198\7?\2\2\u0198\\\3\2\2\2\u0199")
        buf.write("\u019e\5\t\5\2\u019a\u019e\5;\36\2\u019b\u019e\5? \2\u019c")
        buf.write("\u019e\5E#\2\u019d\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e^\3\2\2\2\u019f")
        buf.write("\u01a3\5]/\2\u01a0\u01a2\7\"\2\2\u01a1\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01aa\5")
        buf.write("G$\2\u01a7\u01a9\7\"\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac")
        buf.write("\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab")
        buf.write("\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01ae\5_\60\2")
        buf.write("\u01ae\u01b1\3\2\2\2\u01af\u01b1\5]/\2\u01b0\u019f\3\2")
        buf.write("\2\2\u01b0\u01af\3\2\2\2\u01b1`\3\2\2\2\u01b2\u01b3\5")
        buf.write("W,\2\u01b3\u01b4\5_\60\2\u01b4\u01b5\5Y-\2\u01b5\u01b6")
        buf.write("\b\61\6\2\u01b6b\3\2\2\2\u01b7\u01b8\7$\2\2\u01b8d\3\2")
        buf.write("\2\2\u01b9\u01ba\7\62\2\2\u01baf\3\2\2\2\u01bb\u01bc\7")
        buf.write("a\2\2\u01bch\3\2\2\2\u01bd\u01be\7-\2\2\u01bej\3\2\2\2")
        buf.write("\u01bf\u01c0\7/\2\2\u01c0l\3\2\2\2\u01c1\u01c2\7,\2\2")
        buf.write("\u01c2n\3\2\2\2\u01c3\u01c4\7\61\2\2\u01c4p\3\2\2\2\u01c5")
        buf.write("\u01c6\7\'\2\2\u01c6r\3\2\2\2\u01c7\u01c8\7#\2\2\u01c8")
        buf.write("t\3\2\2\2\u01c9\u01ca\7(\2\2\u01ca\u01cb\7(\2\2\u01cb")
        buf.write("v\3\2\2\2\u01cc\u01cd\7~\2\2\u01cd\u01ce\7~\2\2\u01ce")
        buf.write("x\3\2\2\2\u01cf\u01d0\7?\2\2\u01d0\u01d1\7?\2\2\u01d1")
        buf.write("z\3\2\2\2\u01d2\u01d3\7#\2\2\u01d3\u01d4\7?\2\2\u01d4")
        buf.write("|\3\2\2\2\u01d5\u01d6\7>\2\2\u01d6~\3\2\2\2\u01d7\u01d8")
        buf.write("\7>\2\2\u01d8\u01d9\7?\2\2\u01d9\u0080\3\2\2\2\u01da\u01db")
        buf.write("\7@\2\2\u01db\u0082\3\2\2\2\u01dc\u01dd\7@\2\2\u01dd\u01de")
        buf.write("\7?\2\2\u01de\u0084\3\2\2\2\u01df\u01e0\7<\2\2\u01e0\u01e1")
        buf.write("\7<\2\2\u01e1\u0086\3\2\2\2\u01e2\u01e4\t\13\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e8\b")
        buf.write("D\2\2\u01e8\u0088\3\2\2\2\u01e9\u01ea\13\2\2\2\u01ea\u01eb")
        buf.write("\bE\7\2\u01eb\u008a\3\2\2\2\u01ec\u01f1\5c\62\2\u01ed")
        buf.write("\u01f0\5\7\4\2\u01ee\u01f0\n\f\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01ef\u01ee\3\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3")
        buf.write("\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f4\u01f5\bF\b\2\u01f5\u008c\3\2\2\2\u01f6")
        buf.write("\u01f7\13\2\2\2\u01f7\u008e\3\2\2\2!\2\u0095\u00a3\u00ac")
        buf.write("\u00b1\u00b3\u0137\u013c\u0140\u0145\u0149\u014b\u0150")
        buf.write("\u0154\u0156\u015c\u015e\u0167\u0169\u016e\u0175\u0179")
        buf.write("\u017e\u0180\u019d\u01a3\u01aa\u01b0\u01e5\u01ef\u01f1")
        buf.write("\t\b\2\2\3\5\2\3\36\3\3 \4\3\61\5\3E\6\3F\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_C = 1
    COMMENT_CPP = 2
    STR = 3
    AUTO = 4
    BREAK = 5
    BOOLEAN = 6
    DO = 7
    ELSE = 8
    FLOAT = 9
    FOR = 10
    FUNCTION = 11
    IF = 12
    INTEGER = 13
    RETURN = 14
    STRING = 15
    WHILE = 16
    VOID = 17
    OUT = 18
    CONTINUE = 19
    OF = 20
    INHERIT = 21
    ARRAY = 22
    FALSE = 23
    TRUE = 24
    BOOL = 25
    FLO = 26
    INT = 27
    ID = 28
    COMA = 29
    COL = 30
    SEM = 31
    DOT = 32
    LSB = 33
    RSB = 34
    LB = 35
    RB = 36
    LCB = 37
    RCB = 38
    EQU = 39
    ARR = 40
    DB = 41
    ZERO = 42
    UNDE = 43
    PLUS = 44
    MINU = 45
    MUTI = 46
    DIVI = 47
    MODU = 48
    NOT = 49
    AND = 50
    OR = 51
    EQUL = 52
    NEQ = 53
    LESS = 54
    LOEQ = 55
    GREA = 56
    GOEQ = 57
    SCOPE = 58
    WS = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'false'", "'true'", "','", "':'", "';'", "'.'", 
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'='", "'\"'", "'0'", 
            "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "FALSE", "TRUE", "BOOL", "FLO", "INT", "ID", "COMA", 
            "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", "RCB", 
            "EQU", "ARR", "DB", "ZERO", "UNDE", "PLUS", "MINU", "MUTI", 
            "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", 
            "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
                  "CONTINUE", "OF", "INHERIT", "ARRAY", "FALSE", "TRUE", 
                  "BOOL", "DECIMAL", "EXPONENT", "FLO", "POSINT", "INT", 
                  "DIGIT", "LETTER", "ID", "COMA", "COL", "SEM", "DOT", 
                  "LSB", "RSB", "LB", "RB", "LCB", "RCB", "EQU", "EXPR", 
                  "EXPRESSTIONS", "ARR", "DB", "ZERO", "UNDE", "PLUS", "MINU", 
                  "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", 
                  "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[28] = self.FLO_action 
            actions[30] = self.INT_action 
            actions[47] = self.ARR_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
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
     



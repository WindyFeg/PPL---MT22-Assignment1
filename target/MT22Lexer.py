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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0203\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\7\2\u0098\n\2\f\2\16\2\u009b\13\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\5\4\u00b1\n\4\3\5\3\5\3\5\7\5\u00b6")
        buf.write("\n\5\f\5\16\5\u00b9\13\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\5\33\u0138\n\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\36\6\36\u0146\n\36\r\36")
        buf.write("\16\36\u0147\3\37\3\37\5\37\u014c\n\37\3\37\6\37\u014f")
        buf.write("\n\37\r\37\16\37\u0150\3 \3 \6 \u0155\n \r \16 \u0156")
        buf.write("\3 \3 \3 \5 \u015c\n \3 \3 \6 \u0160\n \r \16 \u0161\3")
        buf.write(" \3 \3 \3 \5 \u0168\n \5 \u016a\n \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\7!\u0173\n!\f!\16!\u0176\13!\3\"\3\"\5\"\u017a\n\"\3")
        buf.write("\"\3\"\3#\3#\3$\5$\u0181\n$\3%\3%\5%\u0185\n%\3%\3%\3")
        buf.write("%\7%\u018a\n%\f%\16%\u018d\13%\3&\3&\3&\3&\5&\u0193\n")
        buf.write("&\3\'\3\'\7\'\u0197\n\'\f\'\16\'\u019a\13\'\3\'\3\'\7")
        buf.write("\'\u019e\n\'\f\'\16\'\u01a1\13\'\3\'\3\'\3\'\5\'\u01a6")
        buf.write("\n\'\3(\3(\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3")
        buf.write(";\3;\3<\3<\3=\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3D\3D\3D\3E\3E\3E\3F\6F\u01ef\nF\rF\16F")
        buf.write("\u01f0\3F\3F\3G\3G\3G\3H\3H\3H\7H\u01fb\nH\fH\16H\u01fe")
        buf.write("\13H\3H\3H\3I\3I\3\u0099\2J\3\3\5\4\7\2\t\5\13\6\r\7\17")
        buf.write("\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22")
        buf.write("%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35")
        buf.write(";\2=\2?\36A\2C\37E\2G\2I K\2M\2O!Q\"S#U$W%Y&[\'](_)a*")
        buf.write("c+e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008fA\u0091")
        buf.write("B\3\2\r\4\2\f\f\17\17\b\2))ddhhppttvv\4\2$$^^\6\2\f\f")
        buf.write("\17\17$$^^\4\2GGgg\4\2--//\3\2\63;\3\2\62;\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\5\2\f\f\17\17$$\2\u021b\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2?\3")
        buf.write("\2\2\2\2C\3\2\2\2\2I\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u00a1\3\2\2\2\7\u00ac")
        buf.write("\3\2\2\2\t\u00b2\3\2\2\2\13\u00be\3\2\2\2\r\u00c0\3\2")
        buf.write("\2\2\17\u00c5\3\2\2\2\21\u00cb\3\2\2\2\23\u00d3\3\2\2")
        buf.write("\2\25\u00d6\3\2\2\2\27\u00db\3\2\2\2\31\u00e1\3\2\2\2")
        buf.write("\33\u00e5\3\2\2\2\35\u00ee\3\2\2\2\37\u00f1\3\2\2\2!\u00f9")
        buf.write("\3\2\2\2#\u0100\3\2\2\2%\u0107\3\2\2\2\'\u010d\3\2\2\2")
        buf.write(")\u0112\3\2\2\2+\u0116\3\2\2\2-\u011f\3\2\2\2/\u0122\3")
        buf.write("\2\2\2\61\u012a\3\2\2\2\63\u0130\3\2\2\2\65\u0137\3\2")
        buf.write("\2\2\67\u0139\3\2\2\29\u013f\3\2\2\2;\u0145\3\2\2\2=\u0149")
        buf.write("\3\2\2\2?\u0169\3\2\2\2A\u016d\3\2\2\2C\u0179\3\2\2\2")
        buf.write("E\u017d\3\2\2\2G\u0180\3\2\2\2I\u0184\3\2\2\2K\u0192\3")
        buf.write("\2\2\2M\u01a5\3\2\2\2O\u01a7\3\2\2\2Q\u01ac\3\2\2\2S\u01ae")
        buf.write("\3\2\2\2U\u01b0\3\2\2\2W\u01b2\3\2\2\2Y\u01b4\3\2\2\2")
        buf.write("[\u01b6\3\2\2\2]\u01b8\3\2\2\2_\u01ba\3\2\2\2a\u01bc\3")
        buf.write("\2\2\2c\u01be\3\2\2\2e\u01c0\3\2\2\2g\u01c2\3\2\2\2i\u01c4")
        buf.write("\3\2\2\2k\u01c6\3\2\2\2m\u01c8\3\2\2\2o\u01ca\3\2\2\2")
        buf.write("q\u01cc\3\2\2\2s\u01ce\3\2\2\2u\u01d0\3\2\2\2w\u01d2\3")
        buf.write("\2\2\2y\u01d4\3\2\2\2{\u01d7\3\2\2\2}\u01da\3\2\2\2\177")
        buf.write("\u01dd\3\2\2\2\u0081\u01e0\3\2\2\2\u0083\u01e2\3\2\2\2")
        buf.write("\u0085\u01e5\3\2\2\2\u0087\u01e7\3\2\2\2\u0089\u01ea\3")
        buf.write("\2\2\2\u008b\u01ee\3\2\2\2\u008d\u01f4\3\2\2\2\u008f\u01f7")
        buf.write("\3\2\2\2\u0091\u0201\3\2\2\2\u0093\u0094\7\61\2\2\u0094")
        buf.write("\u0095\7,\2\2\u0095\u0099\3\2\2\2\u0096\u0098\13\2\2\2")
        buf.write("\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u009a\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099")
        buf.write("\3\2\2\2\u009c\u009d\7,\2\2\u009d\u009e\7\61\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\b\2\2\2\u00a0\4\3\2\2\2\u00a1")
        buf.write("\u00a2\7\61\2\2\u00a2\u00a3\7\61\2\2\u00a3\u00a7\3\2\2")
        buf.write("\2\u00a4\u00a6\n\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00aa\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ab\b\3\2\2")
        buf.write("\u00ab\6\3\2\2\2\u00ac\u00b0\7^\2\2\u00ad\u00b1\t\3\2")
        buf.write("\2\u00ae\u00b1\5g\64\2\u00af\u00b1\t\4\2\2\u00b0\u00ad")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1")
        buf.write("\b\3\2\2\2\u00b2\u00b7\5g\64\2\u00b3\u00b6\5\7\4\2\u00b4")
        buf.write("\u00b6\n\5\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8\3")
        buf.write("\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba\u00bb")
        buf.write("\5g\64\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\b\5\3\2\u00bd")
        buf.write("\n\3\2\2\2\u00be\u00bf\5\u0089E\2\u00bf\f\3\2\2\2\u00c0")
        buf.write("\u00c1\7c\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7q\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7d\2\2\u00c6")
        buf.write("\u00c7\7t\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7c\2\2\u00c9")
        buf.write("\u00ca\7m\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7d\2\2\u00cc")
        buf.write("\u00cd\7q\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf\7n\2\2\u00cf")
        buf.write("\u00d0\7g\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7p\2\2\u00d2")
        buf.write("\22\3\2\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7q\2\2\u00d5")
        buf.write("\24\3\2\2\2\u00d6\u00d7\7g\2\2\u00d7\u00d8\7n\2\2\u00d8")
        buf.write("\u00d9\7u\2\2\u00d9\u00da\7g\2\2\u00da\26\3\2\2\2\u00db")
        buf.write("\u00dc\7h\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7c\2\2\u00df\u00e0\7v\2\2\u00e0\30\3\2\2\2\u00e1")
        buf.write("\u00e2\7h\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\32\3\2\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7w\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7k\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\34\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7h\2\2\u00f0")
        buf.write("\36\3\2\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7g\2\2\u00f5\u00f6\7i\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\u00f8\7t\2\2\u00f8 \3\2\2\2\u00f9")
        buf.write("\u00fa\7t\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("\u00fd\7w\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7p\2\2\u00ff")
        buf.write("\"\3\2\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105")
        buf.write("\u0106\7i\2\2\u0106$\3\2\2\2\u0107\u0108\7y\2\2\u0108")
        buf.write("\u0109\7j\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c&\3\2\2\2\u010d\u010e\7x\2\2\u010e")
        buf.write("\u010f\7q\2\2\u010f\u0110\7k\2\2\u0110\u0111\7f\2\2\u0111")
        buf.write("(\3\2\2\2\u0112\u0113\7q\2\2\u0113\u0114\7w\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115*\3\2\2\2\u0116\u0117\7e\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7w\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e,\3\2\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0121\7h\2\2\u0121.\3\2\2\2\u0122\u0123\7k\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7j\2\2\u0125\u0126\7g\2\2\u0126")
        buf.write("\u0127\7t\2\2\u0127\u0128\7k\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\60\3\2\2\2\u012a\u012b\7c\2\2\u012b\u012c\7t\2\2\u012c")
        buf.write("\u012d\7t\2\2\u012d\u012e\7c\2\2\u012e\u012f\7{\2\2\u012f")
        buf.write("\62\3\2\2\2\u0130\u0131\7o\2\2\u0131\u0132\7c\2\2\u0132")
        buf.write("\u0133\7k\2\2\u0133\u0134\7p\2\2\u0134\64\3\2\2\2\u0135")
        buf.write("\u0138\5\67\34\2\u0136\u0138\59\35\2\u0137\u0135\3\2\2")
        buf.write("\2\u0137\u0136\3\2\2\2\u0138\66\3\2\2\2\u0139\u013a\7")
        buf.write("h\2\2\u013a\u013b\7c\2\2\u013b\u013c\7n\2\2\u013c\u013d")
        buf.write("\7u\2\2\u013d\u013e\7g\2\2\u013e8\3\2\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7t\2\2\u0141\u0142\7w\2\2\u0142\u0143")
        buf.write("\7g\2\2\u0143:\3\2\2\2\u0144\u0146\5E#\2\u0145\u0144\3")
        buf.write("\2\2\2\u0146\u0147\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148<\3\2\2\2\u0149\u014b\t\6\2\2\u014a\u014c")
        buf.write("\t\7\2\2\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014e\3\2\2\2\u014d\u014f\5E#\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0150\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151>\3\2\2\2\u0152\u0155\5A!\2\u0153\u0155\5i\65\2")
        buf.write("\u0154\u0152\3\2\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\u0159\5W,\2\u0159\u015b\5;\36\2\u015a\u015c")
        buf.write("\5=\37\2\u015b\u015a\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u016a\3\2\2\2\u015d\u0160\5A!\2\u015e\u0160\5i\65\2\u015f")
        buf.write("\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0161\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3")
        buf.write("\2\2\2\u0163\u0167\5=\37\2\u0164\u0165\5W,\2\u0165\u0166")
        buf.write("\5;\36\2\u0166\u0168\3\2\2\2\u0167\u0164\3\2\2\2\u0167")
        buf.write("\u0168\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u0154\3\2\2\2")
        buf.write("\u0169\u015f\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\b")
        buf.write(" \4\2\u016c@\3\2\2\2\u016d\u0174\t\b\2\2\u016e\u016f\5")
        buf.write("k\66\2\u016f\u0170\5E#\2\u0170\u0173\3\2\2\2\u0171\u0173")
        buf.write("\5E#\2\u0172\u016e\3\2\2\2\u0172\u0171\3\2\2\2\u0173\u0176")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("B\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u017a\5A!\2\u0178")
        buf.write("\u017a\5i\65\2\u0179\u0177\3\2\2\2\u0179\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017b\u017c\b\"\5\2\u017cD\3\2\2")
        buf.write("\2\u017d\u017e\t\t\2\2\u017eF\3\2\2\2\u017f\u0181\t\n")
        buf.write("\2\2\u0180\u017f\3\2\2\2\u0181H\3\2\2\2\u0182\u0185\5")
        buf.write("G$\2\u0183\u0185\5k\66\2\u0184\u0182\3\2\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u018b\3\2\2\2\u0186\u018a\5G$\2\u0187\u018a")
        buf.write("\5k\66\2\u0188\u018a\5E#\2\u0189\u0186\3\2\2\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cJ\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018e\u0193\5\t\5\2\u018f\u0193\5? \2\u0190")
        buf.write("\u0193\5C\"\2\u0191\u0193\5\65\33\2\u0192\u018e\3\2\2")
        buf.write("\2\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193L\3\2\2\2\u0194\u0198\5K&\2\u0195\u0197")
        buf.write("\7\"\2\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198")
        buf.write("\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019b\u019f\5Q)\2\u019c\u019e\7\"")
        buf.write("\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a2\u01a3\5M\'\2\u01a3\u01a6\3\2\2\2")
        buf.write("\u01a4\u01a6\5K&\2\u01a5\u0194\3\2\2\2\u01a5\u01a4\3\2")
        buf.write("\2\2\u01a6N\3\2\2\2\u01a7\u01a8\5a\61\2\u01a8\u01a9\5")
        buf.write("M\'\2\u01a9\u01aa\5c\62\2\u01aa\u01ab\b(\6\2\u01abP\3")
        buf.write("\2\2\2\u01ac\u01ad\7.\2\2\u01adR\3\2\2\2\u01ae\u01af\7")
        buf.write("<\2\2\u01afT\3\2\2\2\u01b0\u01b1\7=\2\2\u01b1V\3\2\2\2")
        buf.write("\u01b2\u01b3\7\60\2\2\u01b3X\3\2\2\2\u01b4\u01b5\7]\2")
        buf.write("\2\u01b5Z\3\2\2\2\u01b6\u01b7\7_\2\2\u01b7\\\3\2\2\2\u01b8")
        buf.write("\u01b9\7*\2\2\u01b9^\3\2\2\2\u01ba\u01bb\7+\2\2\u01bb")
        buf.write("`\3\2\2\2\u01bc\u01bd\7}\2\2\u01bdb\3\2\2\2\u01be\u01bf")
        buf.write("\7\177\2\2\u01bfd\3\2\2\2\u01c0\u01c1\7?\2\2\u01c1f\3")
        buf.write("\2\2\2\u01c2\u01c3\7$\2\2\u01c3h\3\2\2\2\u01c4\u01c5\7")
        buf.write("\62\2\2\u01c5j\3\2\2\2\u01c6\u01c7\7a\2\2\u01c7l\3\2\2")
        buf.write("\2\u01c8\u01c9\7-\2\2\u01c9n\3\2\2\2\u01ca\u01cb\7/\2")
        buf.write("\2\u01cbp\3\2\2\2\u01cc\u01cd\7,\2\2\u01cdr\3\2\2\2\u01ce")
        buf.write("\u01cf\7\61\2\2\u01cft\3\2\2\2\u01d0\u01d1\7\'\2\2\u01d1")
        buf.write("v\3\2\2\2\u01d2\u01d3\7#\2\2\u01d3x\3\2\2\2\u01d4\u01d5")
        buf.write("\7(\2\2\u01d5\u01d6\7(\2\2\u01d6z\3\2\2\2\u01d7\u01d8")
        buf.write("\7~\2\2\u01d8\u01d9\7~\2\2\u01d9|\3\2\2\2\u01da\u01db")
        buf.write("\7?\2\2\u01db\u01dc\7?\2\2\u01dc~\3\2\2\2\u01dd\u01de")
        buf.write("\7#\2\2\u01de\u01df\7?\2\2\u01df\u0080\3\2\2\2\u01e0\u01e1")
        buf.write("\7>\2\2\u01e1\u0082\3\2\2\2\u01e2\u01e3\7>\2\2\u01e3\u01e4")
        buf.write("\7?\2\2\u01e4\u0084\3\2\2\2\u01e5\u01e6\7@\2\2\u01e6\u0086")
        buf.write("\3\2\2\2\u01e7\u01e8\7@\2\2\u01e8\u01e9\7?\2\2\u01e9\u0088")
        buf.write("\3\2\2\2\u01ea\u01eb\7<\2\2\u01eb\u01ec\7<\2\2\u01ec\u008a")
        buf.write("\3\2\2\2\u01ed\u01ef\t\13\2\2\u01ee\u01ed\3\2\2\2\u01ef")
        buf.write("\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bF\2\2\u01f3\u008c\3")
        buf.write("\2\2\2\u01f4\u01f5\13\2\2\2\u01f5\u01f6\bG\7\2\u01f6\u008e")
        buf.write("\3\2\2\2\u01f7\u01fc\5g\64\2\u01f8\u01fb\5\7\4\2\u01f9")
        buf.write("\u01fb\n\f\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9\3\2\2\2")
        buf.write("\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u0200")
        buf.write("\bH\b\2\u0200\u0090\3\2\2\2\u0201\u0202\13\2\2\2\u0202")
        buf.write("\u0092\3\2\2\2!\2\u0099\u00a7\u00b0\u00b5\u00b7\u0137")
        buf.write("\u0147\u014b\u0150\u0154\u0156\u015b\u015f\u0161\u0167")
        buf.write("\u0169\u0172\u0174\u0179\u0180\u0184\u0189\u018b\u0192")
        buf.write("\u0198\u019f\u01a5\u01f0\u01fa\u01fc\t\b\2\2\3\5\2\3 ")
        buf.write("\3\3\"\4\3(\5\3G\6\3H\7")
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
    BOOL = 25
    FALSE = 26
    TRUE = 27
    FLO = 28
    INT = 29
    ID = 30
    ARR = 31
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
    DB = 43
    ZERO = 44
    UNDE = 45
    PLUS = 46
    MINU = 47
    MUTI = 48
    DIVI = 49
    MODU = 50
    NOT = 51
    AND = 52
    OR = 53
    EQUL = 54
    NEQ = 55
    LESS = 56
    LOEQ = 57
    GREA = 58
    GOEQ = 59
    SCOPE = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

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
            "INHERIT", "ARRAY", "MAIN", "BOOL", "FALSE", "TRUE", "FLO", 
            "INT", "ID", "ARR", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", 
            "LB", "RB", "LCB", "RCB", "EQU", "DB", "ZERO", "UNDE", "PLUS", 
            "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", 
            "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR", "STRTYP", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "MAIN", 
                  "BOOL", "FALSE", "TRUE", "DECIMAL", "EXPONENT", "FLO", 
                  "POSINT", "INT", "DIGIT", "LETTER", "ID", "ARRTYPE", "ARRTYPES", 
                  "ARR", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", "LB", 
                  "RB", "LCB", "RCB", "EQU", "DB", "ZERO", "UNDE", "PLUS", 
                  "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQUL", 
                  "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", 
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
            actions[3] = self.STR_action 
            actions[30] = self.FLO_action 
            actions[32] = self.INT_action 
            actions[38] = self.ARR_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
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
     



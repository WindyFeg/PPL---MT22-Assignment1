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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u022e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\7\2\u009e\n\2\f\2\16\2\u00a1\13\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u00ac\n\3\f\3\16")
        buf.write("\3\u00af\13\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b7\n\4\3")
        buf.write("\5\3\5\3\5\7\5\u00bc\n\5\f\5\16\5\u00bf\13\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\5\34\u0144\n\34\3\35\3\35\3\35\3\35\3\35\5")
        buf.write("\35\u014b\n\35\3\36\6\36\u014e\n\36\r\36\16\36\u014f\3")
        buf.write("\37\3\37\5\37\u0154\n\37\3\37\6\37\u0157\n\37\r\37\16")
        buf.write("\37\u0158\3 \3 \6 \u015d\n \r \16 \u015e\3 \3 \3 \5 \u0164")
        buf.write("\n \3 \3 \6 \u0168\n \r \16 \u0169\3 \3 \3 \3 \5 \u0170")
        buf.write("\n \5 \u0172\n \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5")
        buf.write("!\u0180\n!\3\"\3\"\3\"\3\"\3\"\7\"\u0187\n\"\f\"\16\"")
        buf.write("\u018a\13\"\3#\3#\5#\u018e\n#\3#\3#\3$\3$\7$\u0194\n$")
        buf.write("\f$\16$\u0197\13$\3$\3$\7$\u019b\n$\f$\16$\u019e\13$\3")
        buf.write("$\3$\3$\5$\u01a3\n$\3%\3%\5%\u01a7\n%\3&\3&\3\'\5\'\u01ac")
        buf.write("\n\'\3(\3(\5(\u01b0\n(\3(\3(\3(\7(\u01b5\n(\f(\16(\u01b8")
        buf.write("\13(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u01d4\n\64\3\65\3\65\7\65\u01d8\n\65\f\65\16\65")
        buf.write("\u01db\13\65\3\65\3\65\7\65\u01df\n\65\f\65\16\65\u01e2")
        buf.write("\13\65\3\65\3\65\3\65\5\65\u01e7\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3")
        buf.write("D\3E\3E\3E\3F\3F\3G\3G\3G\3H\3H\3H\3I\6I\u021a\nI\rI\16")
        buf.write("I\u021b\3I\3I\3J\3J\3J\3K\3K\3K\7K\u0226\nK\fK\16K\u0229")
        buf.write("\13K\3K\3K\3L\3L\3\u009f\2M\3\3\5\4\7\2\t\5\13\6\r\7\17")
        buf.write("\b\21\t\23\n\25\13\27\f\31\r\33\16\35\17\37\20!\21#\22")
        buf.write("%\23\'\24)\25+\26-\27/\30\61\31\63\32\65\33\67\349\35")
        buf.write(";\2=\2?\36A\37C\2E G!I\"K\2M\2O#Q$S%U&W\'Y([)]*_+a,c-")
        buf.write("e.g\2i\2k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008fA\u0091")
        buf.write("B\u0093C\u0095D\u0097E\3\2\r\4\2\f\f\17\17\b\2))ddhhp")
        buf.write("pttvv\4\2$$^^\6\2\f\f\17\17$$^^\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\3\2\62;\4\2C\\c|\5\2\13\f\17\17\"\"\5\2\f\f\17\17$$")
        buf.write("\2\u0257\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2E\3\2\2\2\2")
        buf.write("G\3\2\2\2\2I\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2")
        buf.write("\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2")
        buf.write("\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u0099\3\2\2\2\5\u00a7")
        buf.write("\3\2\2\2\7\u00b2\3\2\2\2\t\u00b8\3\2\2\2\13\u00c4\3\2")
        buf.write("\2\2\r\u00c6\3\2\2\2\17\u00cb\3\2\2\2\21\u00d1\3\2\2\2")
        buf.write("\23\u00d9\3\2\2\2\25\u00dc\3\2\2\2\27\u00e1\3\2\2\2\31")
        buf.write("\u00e7\3\2\2\2\33\u00eb\3\2\2\2\35\u00f4\3\2\2\2\37\u00f7")
        buf.write("\3\2\2\2!\u00ff\3\2\2\2#\u0106\3\2\2\2%\u010d\3\2\2\2")
        buf.write("\'\u0113\3\2\2\2)\u0118\3\2\2\2+\u011c\3\2\2\2-\u0125")
        buf.write("\3\2\2\2/\u0128\3\2\2\2\61\u0130\3\2\2\2\63\u0136\3\2")
        buf.write("\2\2\65\u013c\3\2\2\2\67\u0143\3\2\2\29\u014a\3\2\2\2")
        buf.write(";\u014d\3\2\2\2=\u0151\3\2\2\2?\u0171\3\2\2\2A\u017f\3")
        buf.write("\2\2\2C\u0181\3\2\2\2E\u018d\3\2\2\2G\u01a2\3\2\2\2I\u01a6")
        buf.write("\3\2\2\2K\u01a8\3\2\2\2M\u01ab\3\2\2\2O\u01af\3\2\2\2")
        buf.write("Q\u01b9\3\2\2\2S\u01bb\3\2\2\2U\u01bd\3\2\2\2W\u01bf\3")
        buf.write("\2\2\2Y\u01c1\3\2\2\2[\u01c3\3\2\2\2]\u01c5\3\2\2\2_\u01c7")
        buf.write("\3\2\2\2a\u01c9\3\2\2\2c\u01cb\3\2\2\2e\u01cd\3\2\2\2")
        buf.write("g\u01d3\3\2\2\2i\u01e6\3\2\2\2k\u01e8\3\2\2\2m\u01ed\3")
        buf.write("\2\2\2o\u01ef\3\2\2\2q\u01f1\3\2\2\2s\u01f3\3\2\2\2u\u01f5")
        buf.write("\3\2\2\2w\u01f7\3\2\2\2y\u01f9\3\2\2\2{\u01fb\3\2\2\2")
        buf.write("}\u01fd\3\2\2\2\177\u01ff\3\2\2\2\u0081\u0202\3\2\2\2")
        buf.write("\u0083\u0205\3\2\2\2\u0085\u0208\3\2\2\2\u0087\u020b\3")
        buf.write("\2\2\2\u0089\u020d\3\2\2\2\u008b\u0210\3\2\2\2\u008d\u0212")
        buf.write("\3\2\2\2\u008f\u0215\3\2\2\2\u0091\u0219\3\2\2\2\u0093")
        buf.write("\u021f\3\2\2\2\u0095\u0222\3\2\2\2\u0097\u022c\3\2\2\2")
        buf.write("\u0099\u009a\7\61\2\2\u009a\u009b\7,\2\2\u009b\u009f\3")
        buf.write("\2\2\2\u009c\u009e\13\2\2\2\u009d\u009c\3\2\2\2\u009e")
        buf.write("\u00a1\3\2\2\2\u009f\u00a0\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3\7")
        buf.write(",\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6")
        buf.write("\b\2\2\2\u00a6\4\3\2\2\2\u00a7\u00a8\7\61\2\2\u00a8\u00a9")
        buf.write("\7\61\2\2\u00a9\u00ad\3\2\2\2\u00aa\u00ac\n\2\2\2\u00ab")
        buf.write("\u00aa\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00b0\3\2\2\2\u00af\u00ad\3")
        buf.write("\2\2\2\u00b0\u00b1\b\3\2\2\u00b1\6\3\2\2\2\u00b2\u00b6")
        buf.write("\7^\2\2\u00b3\u00b7\t\3\2\2\u00b4\u00b7\5m\67\2\u00b5")
        buf.write("\u00b7\t\4\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b6\u00b5\3\2\2\2\u00b7\b\3\2\2\2\u00b8\u00bd\5m\67")
        buf.write("\2\u00b9\u00bc\5\7\4\2\u00ba\u00bc\n\5\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c0\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00c0\u00c1\5m\67\2\u00c1\u00c2\3")
        buf.write("\2\2\2\u00c2\u00c3\b\5\3\2\u00c3\n\3\2\2\2\u00c4\u00c5")
        buf.write("\5\u008fH\2\u00c5\f\3\2\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7q\2\2\u00ca\16")
        buf.write("\3\2\2\2\u00cb\u00cc\7d\2\2\u00cc\u00cd\7t\2\2\u00cd\u00ce")
        buf.write("\7g\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7m\2\2\u00d0\20")
        buf.write("\3\2\2\2\u00d1\u00d2\7d\2\2\u00d2\u00d3\7q\2\2\u00d3\u00d4")
        buf.write("\7q\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7")
        buf.write("\7c\2\2\u00d7\u00d8\7p\2\2\u00d8\22\3\2\2\2\u00d9\u00da")
        buf.write("\7f\2\2\u00da\u00db\7q\2\2\u00db\24\3\2\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\u00de\7n\2\2\u00de\u00df\7u\2\2\u00df\u00e0")
        buf.write("\7g\2\2\u00e0\26\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\30\3\2\2\2\u00e7\u00e8\7h\2\2\u00e8\u00e9")
        buf.write("\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\32\3\2\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\u00ed\7w\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef")
        buf.write("\7e\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\34\3\2\2\2\u00f4\u00f5")
        buf.write("\7k\2\2\u00f5\u00f6\7h\2\2\u00f6\36\3\2\2\2\u00f7\u00f8")
        buf.write("\7k\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7g\2\2\u00fb\u00fc\7i\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe")
        buf.write("\7t\2\2\u00fe \3\2\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101\u0102\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104")
        buf.write("\7t\2\2\u0104\u0105\7p\2\2\u0105\"\3\2\2\2\u0106\u0107")
        buf.write("\7u\2\2\u0107\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7p\2\2\u010b\u010c\7i\2\2\u010c$\3")
        buf.write("\2\2\2\u010d\u010e\7y\2\2\u010e\u010f\7j\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7n\2\2\u0111\u0112\7g\2\2\u0112&\3")
        buf.write("\2\2\2\u0113\u0114\7x\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7k\2\2\u0116\u0117\7f\2\2\u0117(\3\2\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7w\2\2\u011a\u011b\7v\2\2\u011b*\3")
        buf.write("\2\2\2\u011c\u011d\7e\2\2\u011d\u011e\7q\2\2\u011e\u011f")
        buf.write("\7p\2\2\u011f\u0120\7v\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122\u0123\7w\2\2\u0123\u0124\7g\2\2\u0124,\3")
        buf.write("\2\2\2\u0125\u0126\7q\2\2\u0126\u0127\7h\2\2\u0127.\3")
        buf.write("\2\2\2\u0128\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b")
        buf.write("\7j\2\2\u012b\u012c\7g\2\2\u012c\u012d\7t\2\2\u012d\u012e")
        buf.write("\7k\2\2\u012e\u012f\7v\2\2\u012f\60\3\2\2\2\u0130\u0131")
        buf.write("\7c\2\2\u0131\u0132\7t\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7{\2\2\u0135\62\3\2\2\2\u0136\u0137")
        buf.write("\7h\2\2\u0137\u0138\7c\2\2\u0138\u0139\7n\2\2\u0139\u013a")
        buf.write("\7u\2\2\u013a\u013b\7g\2\2\u013b\64\3\2\2\2\u013c\u013d")
        buf.write("\7v\2\2\u013d\u013e\7t\2\2\u013e\u013f\7w\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\66\3\2\2\2\u0141\u0144\5\63\32\2\u0142\u0144")
        buf.write("\5\65\33\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144")
        buf.write("8\3\2\2\2\u0145\u014b\5}?\2\u0146\u014b\5\177@\2\u0147")
        buf.write("\u014b\5\u0081A\2\u0148\u014b\5\u0083B\2\u0149\u014b\5")
        buf.write("\u0085C\2\u014a\u0145\3\2\2\2\u014a\u0146\3\2\2\2\u014a")
        buf.write("\u0147\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u0149\3\2\2\2")
        buf.write("\u014b:\3\2\2\2\u014c\u014e\5K&\2\u014d\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3")
        buf.write("\2\2\2\u0150<\3\2\2\2\u0151\u0153\t\6\2\2\u0152\u0154")
        buf.write("\t\7\2\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2\2\2\u0154")
        buf.write("\u0156\3\2\2\2\u0155\u0157\5K&\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159>\3\2\2\2\u015a\u015d\5C\"\2\u015b\u015d\5o8\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0160\3")
        buf.write("\2\2\2\u0160\u0161\5W,\2\u0161\u0163\5;\36\2\u0162\u0164")
        buf.write("\5=\37\2\u0163\u0162\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("\u0172\3\2\2\2\u0165\u0168\5C\"\2\u0166\u0168\5o8\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3")
        buf.write("\2\2\2\u016b\u016f\5=\37\2\u016c\u016d\5W,\2\u016d\u016e")
        buf.write("\5;\36\2\u016e\u0170\3\2\2\2\u016f\u016c\3\2\2\2\u016f")
        buf.write("\u0170\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u015c\3\2\2\2")
        buf.write("\u0171\u0167\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\b")
        buf.write(" \4\2\u0174@\3\2\2\2\u0175\u0180\5s:\2\u0176\u0180\5u")
        buf.write(";\2\u0177\u0180\5w<\2\u0178\u0180\5y=\2\u0179\u0180\5")
        buf.write("\u0083B\2\u017a\u0180\5\u0085C\2\u017b\u0180\5\u0087D")
        buf.write("\2\u017c\u0180\5\u0089E\2\u017d\u0180\5\u008bF\2\u017e")
        buf.write("\u0180\5\u008dG\2\u017f\u0175\3\2\2\2\u017f\u0176\3\2")
        buf.write("\2\2\u017f\u0177\3\2\2\2\u017f\u0178\3\2\2\2\u017f\u0179")
        buf.write("\3\2\2\2\u017f\u017a\3\2\2\2\u017f\u017b\3\2\2\2\u017f")
        buf.write("\u017c\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2")
        buf.write("\u0180B\3\2\2\2\u0181\u0188\t\b\2\2\u0182\u0183\5q9\2")
        buf.write("\u0183\u0184\5K&\2\u0184\u0187\3\2\2\2\u0185\u0187\5K")
        buf.write("&\2\u0186\u0182\3\2\2\2\u0186\u0185\3\2\2\2\u0187\u018a")
        buf.write("\3\2\2\2\u0188\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189")
        buf.write("D\3\2\2\2\u018a\u0188\3\2\2\2\u018b\u018e\5C\"\2\u018c")
        buf.write("\u018e\5o8\2\u018d\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018e")
        buf.write("\u018f\3\2\2\2\u018f\u0190\b#\5\2\u0190F\3\2\2\2\u0191")
        buf.write("\u0195\5E#\2\u0192\u0194\7\"\2\2\u0193\u0192\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019c\5")
        buf.write("Q)\2\u0199\u019b\7\"\2\2\u019a\u0199\3\2\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d")
        buf.write("\u019f\3\2\2\2\u019e\u019c\3\2\2\2\u019f\u01a0\5G$\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u01a3\5E#\2\u01a2\u0191\3\2\2\2\u01a2")
        buf.write("\u01a1\3\2\2\2\u01a3H\3\2\2\2\u01a4\u01a7\5A!\2\u01a5")
        buf.write("\u01a7\5{>\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("J\3\2\2\2\u01a8\u01a9\t\t\2\2\u01a9L\3\2\2\2\u01aa\u01ac")
        buf.write("\t\n\2\2\u01ab\u01aa\3\2\2\2\u01acN\3\2\2\2\u01ad\u01b0")
        buf.write("\5M\'\2\u01ae\u01b0\5q9\2\u01af\u01ad\3\2\2\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b6\3\2\2\2\u01b1\u01b5\5M\'\2\u01b2")
        buf.write("\u01b5\5q9\2\u01b3\u01b5\5K&\2\u01b4\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2")
        buf.write("\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7P\3\2\2")
        buf.write("\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\7.\2\2\u01baR\3\2\2")
        buf.write("\2\u01bb\u01bc\7<\2\2\u01bcT\3\2\2\2\u01bd\u01be\7=\2")
        buf.write("\2\u01beV\3\2\2\2\u01bf\u01c0\7\60\2\2\u01c0X\3\2\2\2")
        buf.write("\u01c1\u01c2\7]\2\2\u01c2Z\3\2\2\2\u01c3\u01c4\7_\2\2")
        buf.write("\u01c4\\\3\2\2\2\u01c5\u01c6\7*\2\2\u01c6^\3\2\2\2\u01c7")
        buf.write("\u01c8\7+\2\2\u01c8`\3\2\2\2\u01c9\u01ca\7}\2\2\u01ca")
        buf.write("b\3\2\2\2\u01cb\u01cc\7\177\2\2\u01ccd\3\2\2\2\u01cd\u01ce")
        buf.write("\7?\2\2\u01cef\3\2\2\2\u01cf\u01d4\5\t\5\2\u01d0\u01d4")
        buf.write("\5? \2\u01d1\u01d4\5E#\2\u01d2\u01d4\5O(\2\u01d3\u01cf")
        buf.write("\3\2\2\2\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4h\3\2\2\2\u01d5\u01d9\5g\64\2\u01d6")
        buf.write("\u01d8\7\"\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2")
        buf.write("\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01dc\3")
        buf.write("\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01e0\5Q)\2\u01dd\u01df")
        buf.write("\7\"\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3\2\2\2")
        buf.write("\u01e2\u01e0\3\2\2\2\u01e3\u01e4\5i\65\2\u01e4\u01e7\3")
        buf.write("\2\2\2\u01e5\u01e7\5g\64\2\u01e6\u01d5\3\2\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7j\3\2\2\2\u01e8\u01e9\5a\61\2\u01e9\u01ea")
        buf.write("\5i\65\2\u01ea\u01eb\5c\62\2\u01eb\u01ec\b\66\6\2\u01ec")
        buf.write("l\3\2\2\2\u01ed\u01ee\7$\2\2\u01een\3\2\2\2\u01ef\u01f0")
        buf.write("\7\62\2\2\u01f0p\3\2\2\2\u01f1\u01f2\7a\2\2\u01f2r\3\2")
        buf.write("\2\2\u01f3\u01f4\7-\2\2\u01f4t\3\2\2\2\u01f5\u01f6\7/")
        buf.write("\2\2\u01f6v\3\2\2\2\u01f7\u01f8\7,\2\2\u01f8x\3\2\2\2")
        buf.write("\u01f9\u01fa\7\61\2\2\u01faz\3\2\2\2\u01fb\u01fc\7\'\2")
        buf.write("\2\u01fc|\3\2\2\2\u01fd\u01fe\7#\2\2\u01fe~\3\2\2\2\u01ff")
        buf.write("\u0200\7(\2\2\u0200\u0201\7(\2\2\u0201\u0080\3\2\2\2\u0202")
        buf.write("\u0203\7~\2\2\u0203\u0204\7~\2\2\u0204\u0082\3\2\2\2\u0205")
        buf.write("\u0206\7?\2\2\u0206\u0207\7?\2\2\u0207\u0084\3\2\2\2\u0208")
        buf.write("\u0209\7#\2\2\u0209\u020a\7?\2\2\u020a\u0086\3\2\2\2\u020b")
        buf.write("\u020c\7>\2\2\u020c\u0088\3\2\2\2\u020d\u020e\7>\2\2\u020e")
        buf.write("\u020f\7?\2\2\u020f\u008a\3\2\2\2\u0210\u0211\7@\2\2\u0211")
        buf.write("\u008c\3\2\2\2\u0212\u0213\7@\2\2\u0213\u0214\7?\2\2\u0214")
        buf.write("\u008e\3\2\2\2\u0215\u0216\7<\2\2\u0216\u0217\7<\2\2\u0217")
        buf.write("\u0090\3\2\2\2\u0218\u021a\t\13\2\2\u0219\u0218\3\2\2")
        buf.write("\2\u021a\u021b\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\bI\2\2\u021e")
        buf.write("\u0092\3\2\2\2\u021f\u0220\13\2\2\2\u0220\u0221\bJ\7\2")
        buf.write("\u0221\u0094\3\2\2\2\u0222\u0227\5m\67\2\u0223\u0226\5")
        buf.write("\7\4\2\u0224\u0226\n\f\2\2\u0225\u0223\3\2\2\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022b\bK\b\2\u022b\u0096\3\2\2\2\u022c\u022d\13")
        buf.write("\2\2\2\u022d\u0098\3\2\2\2\'\2\u009f\u00ad\u00b6\u00bb")
        buf.write("\u00bd\u0143\u014a\u014f\u0153\u0158\u015c\u015e\u0163")
        buf.write("\u0167\u0169\u016f\u0171\u017f\u0186\u0188\u018d\u0195")
        buf.write("\u019c\u01a2\u01a6\u01ab\u01af\u01b4\u01b6\u01d3\u01d9")
        buf.write("\u01e0\u01e6\u021b\u0225\u0227\t\b\2\2\3\5\2\3 \3\3#\4")
        buf.write("\3\66\5\3J\6\3K\7")
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
    FALSE = 24
    TRUE = 25
    BOOL = 26
    BOOLTYP = 27
    FLO = 28
    FLOTYP = 29
    INT = 30
    DEMENTION = 31
    INTTYP = 32
    ID = 33
    COMA = 34
    COL = 35
    SEM = 36
    DOT = 37
    LSB = 38
    RSB = 39
    LB = 40
    RB = 41
    LCB = 42
    RCB = 43
    EQU = 44
    ARR = 45
    DB = 46
    ZERO = 47
    UNDE = 48
    PLUS = 49
    MINU = 50
    MUTI = 51
    DIVI = 52
    MODU = 53
    NOT = 54
    AND = 55
    OR = 56
    EQUL = 57
    NEQ = 58
    LESS = 59
    LOEQ = 60
    GREA = 61
    GOEQ = 62
    SCOPE = 63
    WS = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

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
            "COMMENT_C", "COMMENT_CPP", "STR", "STRTYP", "AUTO", "BREAK", 
            "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", 
            "INHERIT", "ARRAY", "FALSE", "TRUE", "BOOL", "BOOLTYP", "FLO", 
            "FLOTYP", "INT", "DEMENTION", "INTTYP", "ID", "COMA", "COL", 
            "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", "RCB", "EQU", 
            "ARR", "DB", "ZERO", "UNDE", "PLUS", "MINU", "MUTI", "DIVI", 
            "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", 
            "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR", "STRTYP", 
                  "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", 
                  "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "FALSE", 
                  "TRUE", "BOOL", "BOOLTYP", "DECIMAL", "EXPONENT", "FLO", 
                  "FLOTYP", "POSINT", "INT", "DEMENTION", "INTTYP", "DIGIT", 
                  "LETTER", "ID", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", 
                  "LB", "RB", "LCB", "RCB", "EQU", "EXPR", "EXPRESSTIONS", 
                  "ARR", "DB", "ZERO", "UNDE", "PLUS", "MINU", "MUTI", "DIVI", 
                  "MODU", "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", 
                  "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[33] = self.INT_action 
            actions[52] = self.ARR_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
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
     



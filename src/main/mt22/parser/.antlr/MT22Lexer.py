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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\7\2\u0092\n\2\f\2")
        buf.write("\16\2\u0095\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7")
        buf.write("\3\u00a0\n\3\f\3\16\3\u00a3\13\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4\u00ab\n\4\3\5\3\5\3\5\7\5\u00b0\n\5\f\5\16\5\u00b3")
        buf.write("\13\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\5\33\u0136\n\33\3\34\6\34\u0139\n\34\r\34\16\34")
        buf.write("\u013a\3\35\3\35\5\35\u013f\n\35\3\35\6\35\u0142\n\35")
        buf.write("\r\35\16\35\u0143\3\36\3\36\6\36\u0148\n\36\r\36\16\36")
        buf.write("\u0149\3\36\3\36\3\36\5\36\u014f\n\36\3\36\3\36\6\36\u0153")
        buf.write("\n\36\r\36\16\36\u0154\3\36\3\36\3\36\3\36\5\36\u015b")
        buf.write("\n\36\5\36\u015d\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\7\37\u0166\n\37\f\37\16\37\u0169\13\37\3 \3 \5 \u016d")
        buf.write("\n \3 \3 \3!\3!\3\"\5\"\u0174\n\"\3#\3#\5#\u0178\n#\3")
        buf.write("#\3#\3#\7#\u017d\n#\f#\16#\u0180\13#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write(".\3.\5.\u019a\n.\3/\3/\3/\3/\3/\3\60\3\60\3\60\7\60\u01a4")
        buf.write("\n\60\f\60\16\60\u01a7\13\60\3\60\3\60\3\60\5\60\u01ac")
        buf.write("\n\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<")
        buf.write("\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3B\3")
        buf.write("B\3C\6C\u01da\nC\rC\16C\u01db\3C\3C\3D\3D\3E\3E\3F\3F")
        buf.write("\3\u0093\2G\3\3\5\4\7\2\t\5\13\6\r\7\17\b\21\t\23\n\25")
        buf.write("\13\27\f\31\r\33\16\35\17\37\20!\21#\22%\23\'\24)\25+")
        buf.write("\26-\27/\30\61\31\63\32\65\33\67\29\2;\34=\2?\35A\2C\2")
        buf.write("E\36G\37I K!M\"O#Q$S%U&W\'Y([\2])_*a+c,e-g.i/k\60m\61")
        buf.write("o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\u0083<\u0085")
        buf.write("=\u0087>\u0089?\u008b@\3\2\n\4\2\f\f\17\17\b\2))ddhhp")
        buf.write("pttvv\4\2GGgg\4\2--//\3\2\63;\3\2\62;\4\2C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2\u01fb\2\3\3\2\2\2\2\5\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2;\3\2\2\2\2?\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I")
        buf.write("\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2")
        buf.write("S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\3\u008d\3\2\2\2\5\u009b\3\2\2\2\7\u00a6")
        buf.write("\3\2\2\2\t\u00ac\3\2\2\2\13\u00b8\3\2\2\2\r\u00bd\3\2")
        buf.write("\2\2\17\u00c3\3\2\2\2\21\u00cb\3\2\2\2\23\u00ce\3\2\2")
        buf.write("\2\25\u00d3\3\2\2\2\27\u00d9\3\2\2\2\31\u00dd\3\2\2\2")
        buf.write("\33\u00e6\3\2\2\2\35\u00e9\3\2\2\2\37\u00f1\3\2\2\2!\u00f8")
        buf.write("\3\2\2\2#\u00ff\3\2\2\2%\u0105\3\2\2\2\'\u010a\3\2\2\2")
        buf.write(")\u010e\3\2\2\2+\u0117\3\2\2\2-\u011a\3\2\2\2/\u0122\3")
        buf.write("\2\2\2\61\u0128\3\2\2\2\63\u012e\3\2\2\2\65\u0135\3\2")
        buf.write("\2\2\67\u0138\3\2\2\29\u013c\3\2\2\2;\u015c\3\2\2\2=\u0160")
        buf.write("\3\2\2\2?\u016c\3\2\2\2A\u0170\3\2\2\2C\u0173\3\2\2\2")
        buf.write("E\u0177\3\2\2\2G\u0181\3\2\2\2I\u0183\3\2\2\2K\u0185\3")
        buf.write("\2\2\2M\u0187\3\2\2\2O\u0189\3\2\2\2Q\u018b\3\2\2\2S\u018d")
        buf.write("\3\2\2\2U\u018f\3\2\2\2W\u0191\3\2\2\2Y\u0193\3\2\2\2")
        buf.write("[\u0199\3\2\2\2]\u019b\3\2\2\2_\u01ab\3\2\2\2a\u01ad\3")
        buf.write("\2\2\2c\u01af\3\2\2\2e\u01b1\3\2\2\2g\u01b3\3\2\2\2i\u01b5")
        buf.write("\3\2\2\2k\u01b7\3\2\2\2m\u01b9\3\2\2\2o\u01bb\3\2\2\2")
        buf.write("q\u01bd\3\2\2\2s\u01bf\3\2\2\2u\u01c2\3\2\2\2w\u01c5\3")
        buf.write("\2\2\2y\u01c8\3\2\2\2{\u01cb\3\2\2\2}\u01cd\3\2\2\2\177")
        buf.write("\u01d0\3\2\2\2\u0081\u01d2\3\2\2\2\u0083\u01d5\3\2\2\2")
        buf.write("\u0085\u01d9\3\2\2\2\u0087\u01df\3\2\2\2\u0089\u01e1\3")
        buf.write("\2\2\2\u008b\u01e3\3\2\2\2\u008d\u008e\7\61\2\2\u008e")
        buf.write("\u008f\7,\2\2\u008f\u0093\3\2\2\2\u0090\u0092\13\2\2\2")
        buf.write("\u0091\u0090\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0093\u0091\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093")
        buf.write("\3\2\2\2\u0096\u0097\7,\2\2\u0097\u0098\7\61\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\b\2\2\2\u009a\4\3\2\2\2\u009b")
        buf.write("\u009c\7\61\2\2\u009c\u009d\7\61\2\2\u009d\u00a1\3\2\2")
        buf.write("\2\u009e\u00a0\n\2\2\2\u009f\u009e\3\2\2\2\u00a0\u00a3")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\b\3\2\2")
        buf.write("\u00a5\6\3\2\2\2\u00a6\u00aa\7^\2\2\u00a7\u00ab\t\3\2")
        buf.write("\2\u00a8\u00ab\5a\61\2\u00a9\u00ab\7^\2\2\u00aa\u00a7")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\b\3\2\2\2\u00ac\u00b1\5a\61\2\u00ad\u00b0\5\7\4\2\u00ae")
        buf.write("\u00b0\n\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2\u00b1\u00b2\3")
        buf.write("\2\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b4\u00b5")
        buf.write("\5a\61\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\b\5\3\2\u00b7")
        buf.write("\n\3\2\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7w\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7q\2\2\u00bc\f\3\2\2\2\u00bd")
        buf.write("\u00be\7d\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\u00c1\7c\2\2\u00c1\u00c2\7m\2\2\u00c2\16\3\2\2\2\u00c3")
        buf.write("\u00c4\7d\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7q\2\2\u00c6")
        buf.write("\u00c7\7n\2\2\u00c7\u00c8\7g\2\2\u00c8\u00c9\7c\2\2\u00c9")
        buf.write("\u00ca\7p\2\2\u00ca\20\3\2\2\2\u00cb\u00cc\7f\2\2\u00cc")
        buf.write("\u00cd\7q\2\2\u00cd\22\3\2\2\2\u00ce\u00cf\7g\2\2\u00cf")
        buf.write("\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2\7g\2\2\u00d2")
        buf.write("\24\3\2\2\2\u00d3\u00d4\7h\2\2\u00d4\u00d5\7n\2\2\u00d5")
        buf.write("\u00d6\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8")
        buf.write("\26\3\2\2\2\u00d9\u00da\7h\2\2\u00da\u00db\7q\2\2\u00db")
        buf.write("\u00dc\7t\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7h\2\2\u00de")
        buf.write("\u00df\7w\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7e\2\2\u00e1")
        buf.write("\u00e2\7v\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7p\2\2\u00e5\32\3\2\2\2\u00e6\u00e7\7k\2\2\u00e7")
        buf.write("\u00e8\7h\2\2\u00e8\34\3\2\2\2\u00e9\u00ea\7k\2\2\u00ea")
        buf.write("\u00eb\7p\2\2\u00eb\u00ec\7v\2\2\u00ec\u00ed\7g\2\2\u00ed")
        buf.write("\u00ee\7i\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7t\2\2\u00f0")
        buf.write("\36\3\2\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7w\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\u00f7\7p\2\2\u00f7 \3\2\2\2\u00f8\u00f9\7u\2\2\u00f9")
        buf.write("\u00fa\7v\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7k\2\2\u00fc")
        buf.write("\u00fd\7p\2\2\u00fd\u00fe\7i\2\2\u00fe\"\3\2\2\2\u00ff")
        buf.write("\u0100\7y\2\2\u0100\u0101\7j\2\2\u0101\u0102\7k\2\2\u0102")
        buf.write("\u0103\7n\2\2\u0103\u0104\7g\2\2\u0104$\3\2\2\2\u0105")
        buf.write("\u0106\7x\2\2\u0106\u0107\7q\2\2\u0107\u0108\7k\2\2\u0108")
        buf.write("\u0109\7f\2\2\u0109&\3\2\2\2\u010a\u010b\7q\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7v\2\2\u010d(\3\2\2\2\u010e")
        buf.write("\u010f\7e\2\2\u010f\u0110\7q\2\2\u0110\u0111\7p\2\2\u0111")
        buf.write("\u0112\7v\2\2\u0112\u0113\7k\2\2\u0113\u0114\7p\2\2\u0114")
        buf.write("\u0115\7w\2\2\u0115\u0116\7g\2\2\u0116*\3\2\2\2\u0117")
        buf.write("\u0118\7q\2\2\u0118\u0119\7h\2\2\u0119,\3\2\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7j\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\u011f\7t\2\2\u011f\u0120\7k\2\2\u0120")
        buf.write("\u0121\7v\2\2\u0121.\3\2\2\2\u0122\u0123\7c\2\2\u0123")
        buf.write("\u0124\7t\2\2\u0124\u0125\7t\2\2\u0125\u0126\7c\2\2\u0126")
        buf.write("\u0127\7{\2\2\u0127\60\3\2\2\2\u0128\u0129\7h\2\2\u0129")
        buf.write("\u012a\7c\2\2\u012a\u012b\7n\2\2\u012b\u012c\7u\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d\62\3\2\2\2\u012e\u012f\7v\2\2\u012f")
        buf.write("\u0130\7t\2\2\u0130\u0131\7w\2\2\u0131\u0132\7g\2\2\u0132")
        buf.write("\64\3\2\2\2\u0133\u0136\5\61\31\2\u0134\u0136\5\63\32")
        buf.write("\2\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136\66\3")
        buf.write("\2\2\2\u0137\u0139\5A!\2\u0138\u0137\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b")
        buf.write("8\3\2\2\2\u013c\u013e\t\4\2\2\u013d\u013f\t\5\2\2\u013e")
        buf.write("\u013d\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2")
        buf.write("\u0140\u0142\5A!\2\u0141\u0140\3\2\2\2\u0142\u0143\3\2")
        buf.write("\2\2\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144:\3")
        buf.write("\2\2\2\u0145\u0148\5=\37\2\u0146\u0148\5c\62\2\u0147\u0145")
        buf.write("\3\2\2\2\u0147\u0146\3\2\2\2\u0148\u0149\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u014c\5M\'\2\u014c\u014e\5\67\34\2\u014d\u014f")
        buf.write("\59\35\2\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f")
        buf.write("\u015d\3\2\2\2\u0150\u0153\5=\37\2\u0151\u0153\5c\62\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3")
        buf.write("\2\2\2\u0154\u0152\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u015a\59\35\2\u0157\u0158\5M\'\2\u0158")
        buf.write("\u0159\5\67\34\2\u0159\u015b\3\2\2\2\u015a\u0157\3\2\2")
        buf.write("\2\u015a\u015b\3\2\2\2\u015b\u015d\3\2\2\2\u015c\u0147")
        buf.write("\3\2\2\2\u015c\u0152\3\2\2\2\u015d\u015e\3\2\2\2\u015e")
        buf.write("\u015f\b\36\4\2\u015f<\3\2\2\2\u0160\u0167\t\6\2\2\u0161")
        buf.write("\u0162\5e\63\2\u0162\u0163\5A!\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0166\5A!\2\u0165\u0161\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\u0169\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2")
        buf.write("\u0168>\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016d\5=\37")
        buf.write("\2\u016b\u016d\5c\62\2\u016c\u016a\3\2\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e\u016f\b \5\2\u016f")
        buf.write("@\3\2\2\2\u0170\u0171\t\7\2\2\u0171B\3\2\2\2\u0172\u0174")
        buf.write("\t\b\2\2\u0173\u0172\3\2\2\2\u0174D\3\2\2\2\u0175\u0178")
        buf.write("\5C\"\2\u0176\u0178\5e\63\2\u0177\u0175\3\2\2\2\u0177")
        buf.write("\u0176\3\2\2\2\u0178\u017e\3\2\2\2\u0179\u017d\5C\"\2")
        buf.write("\u017a\u017d\5e\63\2\u017b\u017d\5A!\2\u017c\u0179\3\2")
        buf.write("\2\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d\u0180")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("F\3\2\2\2\u0180\u017e\3\2\2\2\u0181\u0182\7.\2\2\u0182")
        buf.write("H\3\2\2\2\u0183\u0184\7<\2\2\u0184J\3\2\2\2\u0185\u0186")
        buf.write("\7=\2\2\u0186L\3\2\2\2\u0187\u0188\7\60\2\2\u0188N\3\2")
        buf.write("\2\2\u0189\u018a\7]\2\2\u018aP\3\2\2\2\u018b\u018c\7_")
        buf.write("\2\2\u018cR\3\2\2\2\u018d\u018e\7*\2\2\u018eT\3\2\2\2")
        buf.write("\u018f\u0190\7+\2\2\u0190V\3\2\2\2\u0191\u0192\7}\2\2")
        buf.write("\u0192X\3\2\2\2\u0193\u0194\7\177\2\2\u0194Z\3\2\2\2\u0195")
        buf.write("\u019a\5\t\5\2\u0196\u019a\5;\36\2\u0197\u019a\5? \2\u0198")
        buf.write("\u019a\5E#\2\u0199\u0195\3\2\2\2\u0199\u0196\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019a\\\3\2\2\2\u019b")
        buf.write("\u019c\5W,\2\u019c\u019d\5_\60\2\u019d\u019e\5Y-\2\u019e")
        buf.write("\u019f\b/\6\2\u019f^\3\2\2\2\u01a0\u01a1\5[.\2\u01a1\u01a5")
        buf.write("\5G$\2\u01a2\u01a4\7\"\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7")
        buf.write("\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01a8\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01a9\5_\60\2")
        buf.write("\u01a9\u01ac\3\2\2\2\u01aa\u01ac\5[.\2\u01ab\u01a0\3\2")
        buf.write("\2\2\u01ab\u01aa\3\2\2\2\u01ac`\3\2\2\2\u01ad\u01ae\7")
        buf.write("$\2\2\u01aeb\3\2\2\2\u01af\u01b0\7\62\2\2\u01b0d\3\2\2")
        buf.write("\2\u01b1\u01b2\7a\2\2\u01b2f\3\2\2\2\u01b3\u01b4\7-\2")
        buf.write("\2\u01b4h\3\2\2\2\u01b5\u01b6\7/\2\2\u01b6j\3\2\2\2\u01b7")
        buf.write("\u01b8\7,\2\2\u01b8l\3\2\2\2\u01b9\u01ba\7\61\2\2\u01ba")
        buf.write("n\3\2\2\2\u01bb\u01bc\7\'\2\2\u01bcp\3\2\2\2\u01bd\u01be")
        buf.write("\7#\2\2\u01ber\3\2\2\2\u01bf\u01c0\7(\2\2\u01c0\u01c1")
        buf.write("\7(\2\2\u01c1t\3\2\2\2\u01c2\u01c3\7~\2\2\u01c3\u01c4")
        buf.write("\7~\2\2\u01c4v\3\2\2\2\u01c5\u01c6\7?\2\2\u01c6\u01c7")
        buf.write("\7?\2\2\u01c7x\3\2\2\2\u01c8\u01c9\7#\2\2\u01c9\u01ca")
        buf.write("\7?\2\2\u01caz\3\2\2\2\u01cb\u01cc\7>\2\2\u01cc|\3\2\2")
        buf.write("\2\u01cd\u01ce\7>\2\2\u01ce\u01cf\7?\2\2\u01cf~\3\2\2")
        buf.write("\2\u01d0\u01d1\7@\2\2\u01d1\u0080\3\2\2\2\u01d2\u01d3")
        buf.write("\7@\2\2\u01d3\u01d4\7?\2\2\u01d4\u0082\3\2\2\2\u01d5\u01d6")
        buf.write("\7<\2\2\u01d6\u01d7\7<\2\2\u01d7\u0084\3\2\2\2\u01d8\u01da")
        buf.write("\t\t\2\2\u01d9\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01de\bC\2\2\u01de\u0086\3\2\2\2\u01df\u01e0\13")
        buf.write("\2\2\2\u01e0\u0088\3\2\2\2\u01e1\u01e2\13\2\2\2\u01e2")
        buf.write("\u008a\3\2\2\2\u01e3\u01e4\13\2\2\2\u01e4\u008c\3\2\2")
        buf.write("\2\36\2\u0093\u00a1\u00aa\u00af\u00b1\u0135\u013a\u013e")
        buf.write("\u0143\u0147\u0149\u014e\u0152\u0154\u015a\u015c\u0165")
        buf.write("\u0167\u016c\u0173\u0177\u017c\u017e\u0199\u01a5\u01ab")
        buf.write("\u01db\7\b\2\2\3\5\2\3\36\3\3 \4\3/\5")
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
    ARR = 39
    EXPRESSTIONS = 40
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
    EQU = 52
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
            "'['", "']'", "'('", "')'", "'{'", "'}'", "'\"'", "'0'", "'_'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_C", "COMMENT_CPP", "STR", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
            "STRING", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "FALSE", "TRUE", "BOOL", "FLO", "INT", "ID", "COMA", 
            "COL", "SEM", "DOT", "LSB", "RSB", "LB", "RB", "LCB", "RCB", 
            "ARR", "EXPRESSTIONS", "DB", "ZERO", "UNDE", "PLUS", "MINU", 
            "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQU", "NEQ", "LESS", 
            "LOEQ", "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_C", "COMMENT_CPP", "ESCAPE", "STR", "AUTO", "BREAK", 
                  "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
                  "CONTINUE", "OF", "INHERIT", "ARRAY", "FALSE", "TRUE", 
                  "BOOL", "DECIMAL", "EXPONENT", "FLO", "POSINT", "INT", 
                  "DIGIT", "LETTER", "ID", "COMA", "COL", "SEM", "DOT", 
                  "LSB", "RSB", "LB", "RB", "LCB", "RCB", "EXPR", "ARR", 
                  "EXPRESSTIONS", "DB", "ZERO", "UNDE", "PLUS", "MINU", 
                  "MUTI", "DIVI", "MODU", "NOT", "AND", "OR", "EQU", "NEQ", 
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
            actions[45] = self.ARR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1].replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
     

    def FLO_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

    def ARR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            self.text = self.text.replace(' ','')
     



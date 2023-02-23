# Generated from f:\Univercity\S2 Y3\PRINCIPLES OF PROGRAMMING LANGUAGES\Assignment\assignment1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0180\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\7\2Z\n\2\f")
        buf.write("\2\16\2]\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\5\bo\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\tv\n\t\3\n\3\n\3\n\3\n\5\n|\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u008f\n\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\7\13\u009a\n\13\f\13\16\13\u009d\13")
        buf.write("\13\3\f\3\f\3\r\3\r\3\r\5\r\u00a4\n\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\17\5\17\u00ac\n\17\3\17\5\17\u00af\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00bf\n\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u00c8\n\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00d1\n\23\3\24\3\24\3\25\3\25\3\26\3\26\5")
        buf.write("\26\u00d9\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u00e5\n\27\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\5\31\u00f2\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\7!\u0124\n!\f!\16!\u0127\13!\3!\3!\3\"\3\"\3\"\3\"\5")
        buf.write("\"\u012f\n\"\3#\3#\3#\3#\3#\3#\5#\u0137\n#\5#\u0139\n")
        buf.write("#\3$\3$\3$\3$\3$\5$\u0140\n$\3%\3%\3%\3%\3%\5%\u0147\n")
        buf.write("%\3&\3&\3&\3&\3&\3&\5&\u014f\n&\5&\u0151\n&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(")
        buf.write("\u0166\n(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\5,\u017e\n,\3,\3\u0125\3\24-\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTV\2\n\6\2\t\t\f\f\20\20\22\22\3\2\60")
        buf.write("\64\3\2\65\67\3\28=\3\2\66\67\3\2\60\61\3\2\62\64\5\2")
        buf.write("\5\5\33\33\36!\2\u0185\2[\3\2\2\2\4`\3\2\2\2\6b\3\2\2")
        buf.write("\2\bd\3\2\2\2\nf\3\2\2\2\fh\3\2\2\2\16n\3\2\2\2\20u\3")
        buf.write("\2\2\2\22{\3\2\2\2\24\u008e\3\2\2\2\26\u009e\3\2\2\2\30")
        buf.write("\u00a0\3\2\2\2\32\u00a7\3\2\2\2\34\u00ab\3\2\2\2\36\u00b4")
        buf.write("\3\2\2\2 \u00b6\3\2\2\2\"\u00b8\3\2\2\2$\u00c2\3\2\2\2")
        buf.write("&\u00d2\3\2\2\2(\u00d4\3\2\2\2*\u00d8\3\2\2\2,\u00e4\3")
        buf.write("\2\2\2.\u00e6\3\2\2\2\60\u00ea\3\2\2\2\62\u00f3\3\2\2")
        buf.write("\2\64\u0102\3\2\2\2\66\u010b\3\2\2\28\u0113\3\2\2\2:\u0116")
        buf.write("\3\2\2\2<\u0119\3\2\2\2>\u011d\3\2\2\2@\u0120\3\2\2\2")
        buf.write("B\u012e\3\2\2\2D\u0138\3\2\2\2F\u013f\3\2\2\2H\u0146\3")
        buf.write("\2\2\2J\u0150\3\2\2\2L\u0152\3\2\2\2N\u0165\3\2\2\2P\u0167")
        buf.write("\3\2\2\2R\u016a\3\2\2\2T\u016d\3\2\2\2V\u017d\3\2\2\2")
        buf.write("XZ\5V,\2YX\3\2\2\2Z]\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\^\3")
        buf.write("\2\2\2][\3\2\2\2^_\7\2\2\3_\3\3\2\2\2`a\t\2\2\2a\5\3\2")
        buf.write("\2\2bc\t\3\2\2c\7\3\2\2\2de\t\4\2\2e\t\3\2\2\2fg\7>\2")
        buf.write("\2g\13\3\2\2\2hi\t\5\2\2i\r\3\2\2\2jk\7\37\2\2kl\7\"\2")
        buf.write("\2lo\5\16\b\2mo\7\37\2\2nj\3\2\2\2nm\3\2\2\2o\17\3\2\2")
        buf.write("\2pv\5\6\4\2qv\5\b\5\2rv\5\n\6\2sv\5\f\7\2tv\5\32\16\2")
        buf.write("up\3\2\2\2uq\3\2\2\2ur\3\2\2\2us\3\2\2\2ut\3\2\2\2v\21")
        buf.write("\3\2\2\2w|\5\26\f\2x|\5\4\3\2y|\5\20\t\2z|\5\30\r\2{w")
        buf.write("\3\2\2\2{x\3\2\2\2{y\3\2\2\2{z\3\2\2\2|\23\3\2\2\2}~\b")
        buf.write("\13\1\2~\177\5\22\n\2\177\u0080\5\n\6\2\u0080\u0081\5")
        buf.write("\22\n\2\u0081\u008f\3\2\2\2\u0082\u0083\5\22\n\2\u0083")
        buf.write("\u0084\5\f\7\2\u0084\u0085\5\22\n\2\u0085\u008f\3\2\2")
        buf.write("\2\u0086\u0087\7\65\2\2\u0087\u008f\5\22\n\2\u0088\u0089")
        buf.write("\7\61\2\2\u0089\u008f\5\22\n\2\u008a\u008b\5\32\16\2\u008b")
        buf.write("\u008c\5\22\n\2\u008c\u008f\3\2\2\2\u008d\u008f\5\22\n")
        buf.write("\2\u008e}\3\2\2\2\u008e\u0082\3\2\2\2\u008e\u0086\3\2")
        buf.write("\2\2\u008e\u0088\3\2\2\2\u008e\u008a\3\2\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u009b\3\2\2\2\u0090\u0091\f\t\2\2\u0091")
        buf.write("\u0092\t\6\2\2\u0092\u009a\5\22\n\2\u0093\u0094\f\b\2")
        buf.write("\2\u0094\u0095\t\7\2\2\u0095\u009a\5\22\n\2\u0096\u0097")
        buf.write("\f\7\2\2\u0097\u0098\t\b\2\2\u0098\u009a\5\22\n\2\u0099")
        buf.write("\u0090\3\2\2\2\u0099\u0093\3\2\2\2\u0099\u0096\3\2\2\2")
        buf.write("\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3")
        buf.write("\2\2\2\u009c\25\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f")
        buf.write("\t\t\2\2\u009f\27\3\2\2\2\u00a0\u00a1\7 \2\2\u00a1\u00a3")
        buf.write("\7(\2\2\u00a2\u00a4\5H%\2\u00a3\u00a2\3\2\2\2\u00a3\u00a4")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a6\7)\2\2\u00a6")
        buf.write("\31\3\2\2\2\u00a7\u00a8\7 \2\2\u00a8\u00a9\5D#\2\u00a9")
        buf.write("\33\3\2\2\2\u00aa\u00ac\7\30\2\2\u00ab\u00aa\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00af\7\25\2")
        buf.write("\2\u00ae\u00ad\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b0")
        buf.write("\3\2\2\2\u00b0\u00b1\7 \2\2\u00b1\u00b2\7#\2\2\u00b2\u00b3")
        buf.write("\5\4\3\2\u00b3\35\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\37")
        buf.write("\3\2\2\2\u00b6\u00b7\5\24\13\2\u00b7!\3\2\2\2\u00b8\u00b9")
        buf.write("\7\32\2\2\u00b9\u00ba\7#\2\2\u00ba\u00bb\7\16\2\2\u00bb")
        buf.write("\u00bc\7\24\2\2\u00bc\u00be\7(\2\2\u00bd\u00bf\5F$\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2")
        buf.write("\u00c0\u00c1\7)\2\2\u00c1#\3\2\2\2\u00c2\u00c3\7 \2\2")
        buf.write("\u00c3\u00c4\7#\2\2\u00c4\u00c7\7\16\2\2\u00c5\u00c8\7")
        buf.write("\24\2\2\u00c6\u00c8\5\4\3\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\7(\2\2")
        buf.write("\u00ca\u00cb\5F$\2\u00cb\u00d0\7)\2\2\u00cc\u00cd\7\30")
        buf.write("\2\2\u00cd\u00ce\7 \2\2\u00ce\u00cf\7&\2\2\u00cf\u00d1")
        buf.write("\7\'\2\2\u00d0\u00cc\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("%\3\2\2\2\u00d2\u00d3\5@!\2\u00d3\'\3\2\2\2\u00d4\u00d5")
        buf.write("\7 \2\2\u00d5)\3\2\2\2\u00d6\u00d9\5(\25\2\u00d7\u00d9")
        buf.write("\5\36\20\2\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9")
        buf.write("+\3\2\2\2\u00da\u00e5\5.\30\2\u00db\u00e5\5\60\31\2\u00dc")
        buf.write("\u00e5\5\62\32\2\u00dd\u00e5\5\64\33\2\u00de\u00e5\5\66")
        buf.write("\34\2\u00df\u00e5\58\35\2\u00e0\u00e5\5:\36\2\u00e1\u00e5")
        buf.write("\5<\37\2\u00e2\u00e5\5> \2\u00e3\u00e5\5@!\2\u00e4\u00da")
        buf.write("\3\2\2\2\u00e4\u00db\3\2\2\2\u00e4\u00dc\3\2\2\2\u00e4")
        buf.write("\u00dd\3\2\2\2\u00e4\u00de\3\2\2\2\u00e4\u00df\3\2\2\2")
        buf.write("\u00e4\u00e0\3\2\2\2\u00e4\u00e1\3\2\2\2\u00e4\u00e2\3")
        buf.write("\2\2\2\u00e4\u00e3\3\2\2\2\u00e5-\3\2\2\2\u00e6\u00e7")
        buf.write("\5*\26\2\u00e7\u00e8\7,\2\2\u00e8\u00e9\5\24\13\2\u00e9")
        buf.write("/\3\2\2\2\u00ea\u00eb\7\17\2\2\u00eb\u00ec\7(\2\2\u00ec")
        buf.write("\u00ed\5\24\13\2\u00ed\u00ee\7)\2\2\u00ee\u00f1\5,\27")
        buf.write("\2\u00ef\u00f0\7\13\2\2\u00f0\u00f2\5,\27\2\u00f1\u00ef")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\61\3\2\2\2\u00f3\u00f4")
        buf.write("\7\r\2\2\u00f4\u00f5\7(\2\2\u00f5\u00f6\5(\25\2\u00f6")
        buf.write("\u00f7\7,\2\2\u00f7\u00f8\5\24\13\2\u00f8\u00f9\7\"\2")
        buf.write("\2\u00f9\u00fa\5\24\13\2\u00fa\u00fb\7\"\2\2\u00fb\u00fc")
        buf.write("\5\24\13\2\u00fc\u00fd\7)\2\2\u00fd\u00fe\7*\2\2\u00fe")
        buf.write("\u00ff\5,\27\2\u00ff\u0100\7+\2\2\u0100\u0101\7$\2\2\u0101")
        buf.write("\63\3\2\2\2\u0102\u0103\7\23\2\2\u0103\u0104\7(\2\2\u0104")
        buf.write("\u0105\5\24\13\2\u0105\u0106\7)\2\2\u0106\u0107\7*\2\2")
        buf.write("\u0107\u0108\5,\27\2\u0108\u0109\7+\2\2\u0109\u010a\7")
        buf.write("$\2\2\u010a\65\3\2\2\2\u010b\u010c\7\n\2\2\u010c\u010d")
        buf.write("\5@!\2\u010d\u010e\7\23\2\2\u010e\u010f\7(\2\2\u010f\u0110")
        buf.write("\5\24\13\2\u0110\u0111\7)\2\2\u0111\u0112\7$\2\2\u0112")
        buf.write("\67\3\2\2\2\u0113\u0114\7\b\2\2\u0114\u0115\7$\2\2\u0115")
        buf.write("9\3\2\2\2\u0116\u0117\7\26\2\2\u0117\u0118\7$\2\2\u0118")
        buf.write(";\3\2\2\2\u0119\u011a\7\21\2\2\u011a\u011b\5\24\13\2\u011b")
        buf.write("\u011c\7$\2\2\u011c=\3\2\2\2\u011d\u011e\5\30\r\2\u011e")
        buf.write("\u011f\7$\2\2\u011f?\3\2\2\2\u0120\u0125\7*\2\2\u0121")
        buf.write("\u0124\5J&\2\u0122\u0124\5L\'\2\u0123\u0121\3\2\2\2\u0123")
        buf.write("\u0122\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0126\3\2\2\2")
        buf.write("\u0125\u0123\3\2\2\2\u0126\u0128\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0128\u0129\7+\2\2\u0129A\3\2\2\2\u012a\u012b\7")
        buf.write(" \2\2\u012b\u012c\7\"\2\2\u012c\u012f\5B\"\2\u012d\u012f")
        buf.write("\7 \2\2\u012e\u012a\3\2\2\2\u012e\u012d\3\2\2\2\u012f")
        buf.write("C\3\2\2\2\u0130\u0131\5\24\13\2\u0131\u0132\7\"\2\2\u0132")
        buf.write("\u0133\5D#\2\u0133\u0139\3\2\2\2\u0134\u0136\5\24\13\2")
        buf.write("\u0135\u0137\7$\2\2\u0136\u0135\3\2\2\2\u0136\u0137\3")
        buf.write("\2\2\2\u0137\u0139\3\2\2\2\u0138\u0130\3\2\2\2\u0138\u0134")
        buf.write("\3\2\2\2\u0139E\3\2\2\2\u013a\u013b\5\34\17\2\u013b\u013c")
        buf.write("\7\"\2\2\u013c\u013d\5F$\2\u013d\u0140\3\2\2\2\u013e\u0140")
        buf.write("\5\34\17\2\u013f\u013a\3\2\2\2\u013f\u013e\3\2\2\2\u0140")
        buf.write("G\3\2\2\2\u0141\u0142\5 \21\2\u0142\u0143\7\"\2\2\u0143")
        buf.write("\u0144\5H%\2\u0144\u0147\3\2\2\2\u0145\u0147\5 \21\2\u0146")
        buf.write("\u0141\3\2\2\2\u0146\u0145\3\2\2\2\u0147I\3\2\2\2\u0148")
        buf.write("\u0149\5,\27\2\u0149\u014a\7$\2\2\u014a\u014b\5J&\2\u014b")
        buf.write("\u0151\3\2\2\2\u014c\u014e\5,\27\2\u014d\u014f\7$\2\2")
        buf.write("\u014e\u014d\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3")
        buf.write("\2\2\2\u0150\u0148\3\2\2\2\u0150\u014c\3\2\2\2\u0151K")
        buf.write("\3\2\2\2\u0152\u0153\5N(\2\u0153\u0154\7$\2\2\u0154M\3")
        buf.write("\2\2\2\u0155\u0156\7 \2\2\u0156\u0157\7\"\2\2\u0157\u0158")
        buf.write("\5N(\2\u0158\u0159\7\"\2\2\u0159\u015a\5\24\13\2\u015a")
        buf.write("\u0166\3\2\2\2\u015b\u015c\7 \2\2\u015c\u015d\7#\2\2\u015d")
        buf.write("\u015e\5\4\3\2\u015e\u015f\7,\2\2\u015f\u0160\5\24\13")
        buf.write("\2\u0160\u0166\3\2\2\2\u0161\u0162\5B\"\2\u0162\u0163")
        buf.write("\7#\2\2\u0163\u0164\5\4\3\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u0155\3\2\2\2\u0165\u015b\3\2\2\2\u0165\u0161\3\2\2\2")
        buf.write("\u0166O\3\2\2\2\u0167\u0168\5$\23\2\u0168\u0169\5&\24")
        buf.write("\2\u0169Q\3\2\2\2\u016a\u016b\5\"\22\2\u016b\u016c\5&")
        buf.write("\24\2\u016cS\3\2\2\2\u016d\u016e\7\31\2\2\u016e\u016f")
        buf.write("\7&\2\2\u016f\u0170\5\16\b\2\u0170\u0171\7\'\2\2\u0171")
        buf.write("\u0172\7\27\2\2\u0172\u0173\5\4\3\2\u0173U\3\2\2\2\u0174")
        buf.write("\u017e\5R*\2\u0175\u017e\5P)\2\u0176\u0177\5N(\2\u0177")
        buf.write("\u0178\7$\2\2\u0178\u017e\3\2\2\2\u0179\u017a\5T+\2\u017a")
        buf.write("\u017b\7$\2\2\u017b\u017e\3\2\2\2\u017c\u017e\5D#\2\u017d")
        buf.write("\u0174\3\2\2\2\u017d\u0175\3\2\2\2\u017d\u0176\3\2\2\2")
        buf.write("\u017d\u0179\3\2\2\2\u017d\u017c\3\2\2\2\u017eW\3\2\2")
        buf.write("\2\35[nu{\u008e\u0099\u009b\u00a3\u00ab\u00ae\u00be\u00c7")
        buf.write("\u00d0\u00d8\u00e4\u00f1\u0123\u0125\u012e\u0136\u0138")
        buf.write("\u013f\u0146\u014e\u0150\u0165\u017d")
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
                     "'main'", "<INVALID>", "'false'", "'true'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "':'", 
                     "';'", "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "'='", "'\"'", "'0'", "'_'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "STRTYP", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                      "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                      "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                      "ARRAY", "MAIN", "BOOL", "FALSE", "TRUE", "FLO", "INT", 
                      "ID", "ARR", "COMA", "COL", "SEM", "DOT", "LSB", "RSB", 
                      "LB", "RB", "LCB", "RCB", "EQU", "DB", "ZERO", "UNDE", 
                      "PLUS", "MINU", "MUTI", "DIVI", "MODU", "NOT", "AND", 
                      "OR", "EQUL", "NEQ", "LESS", "LOEQ", "GREA", "GOEQ", 
                      "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vartype = 1
    RULE_arithmetricop = 2
    RULE_booleanop = 3
    RULE_stringop = 4
    RULE_relationalop = 5
    RULE_demention = 6
    RULE_operator = 7
    RULE_operand = 8
    RULE_expression = 9
    RULE_constant = 10
    RULE_functioncall = 11
    RULE_indexop = 12
    RULE_parameter = 13
    RULE_indexexpression = 14
    RULE_arguement = 15
    RULE_functionmainprot = 16
    RULE_functionprot = 17
    RULE_functionbody = 18
    RULE_scalarvar = 19
    RULE_lhs = 20
    RULE_statement = 21
    RULE_assignstatement = 22
    RULE_ifstatement = 23
    RULE_forstatement = 24
    RULE_whilestatement = 25
    RULE_dowhilestatement = 26
    RULE_breakstatement = 27
    RULE_continuestatement = 28
    RULE_returnstatement = 29
    RULE_callstatement = 30
    RULE_blockstatement = 31
    RULE_idlist = 32
    RULE_expressionlist = 33
    RULE_parameterlist = 34
    RULE_arguementlist = 35
    RULE_statementlist = 36
    RULE_variabledecl = 37
    RULE_variabledecls = 38
    RULE_functiondecl = 39
    RULE_mainfunction = 40
    RULE_arraydecl = 41
    RULE_mt22language = 42

    ruleNames =  [ "program", "vartype", "arithmetricop", "booleanop", "stringop", 
                   "relationalop", "demention", "operator", "operand", "expression", 
                   "constant", "functioncall", "indexop", "parameter", "indexexpression", 
                   "arguement", "functionmainprot", "functionprot", "functionbody", 
                   "scalarvar", "lhs", "statement", "assignstatement", "ifstatement", 
                   "forstatement", "whilestatement", "dowhilestatement", 
                   "breakstatement", "continuestatement", "returnstatement", 
                   "callstatement", "blockstatement", "idlist", "expressionlist", 
                   "parameterlist", "arguementlist", "statementlist", "variabledecl", 
                   "variabledecls", "functiondecl", "mainfunction", "arraydecl", 
                   "mt22language" ]

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
    MAIN=24
    BOOL=25
    FALSE=26
    TRUE=27
    FLO=28
    INT=29
    ID=30
    ARR=31
    COMA=32
    COL=33
    SEM=34
    DOT=35
    LSB=36
    RSB=37
    LB=38
    RB=39
    LCB=40
    RCB=41
    EQU=42
    DB=43
    ZERO=44
    UNDE=45
    PLUS=46
    MINU=47
    MUTI=48
    DIVI=49
    MODU=50
    NOT=51
    AND=52
    OR=53
    EQUL=54
    NEQ=55
    LESS=56
    LOEQ=57
    GREA=58
    GOEQ=59
    SCOPE=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

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

        def mt22language(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Mt22languageContext)
            else:
                return self.getTypedRuleContext(MT22Parser.Mt22languageContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.ARRAY) | (1 << MT22Parser.MAIN) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.ARR) | (1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU) | (1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ) | (1 << MT22Parser.SCOPE))) != 0):
                self.state = 86
                self.mt22language()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 92
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_vartype




    def vartype(self):

        localctx = MT22Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmetricopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arithmetricop




    def arithmetricop(self):

        localctx = MT22Parser.ArithmetricopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_arithmetricop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_booleanop




    def booleanop(self):

        localctx = MT22Parser.BooleanopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_booleanop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCOPE(self):
            return self.getToken(MT22Parser.SCOPE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_stringop




    def stringop(self):

        localctx = MT22Parser.StringopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stringop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(MT22Parser.SCOPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUL(self):
            return self.getToken(MT22Parser.EQUL, 0)

        def NEQ(self):
            return self.getToken(MT22Parser.NEQ, 0)

        def LESS(self):
            return self.getToken(MT22Parser.LESS, 0)

        def GREA(self):
            return self.getToken(MT22Parser.GREA, 0)

        def LOEQ(self):
            return self.getToken(MT22Parser.LOEQ, 0)

        def GOEQ(self):
            return self.getToken(MT22Parser.GOEQ, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_relationalop




    def relationalop(self):

        localctx = MT22Parser.RelationalopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_relationalop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DementionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def demention(self):
            return self.getTypedRuleContext(MT22Parser.DementionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_demention




    def demention(self):

        localctx = MT22Parser.DementionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_demention)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(MT22Parser.INT)
                self.state = 105
                self.match(MT22Parser.COMA)
                self.state = 106
                self.demention()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(MT22Parser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetricop(self):
            return self.getTypedRuleContext(MT22Parser.ArithmetricopContext,0)


        def booleanop(self):
            return self.getTypedRuleContext(MT22Parser.BooleanopContext,0)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operator




    def operator(self):

        localctx = MT22Parser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operator)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PLUS, MT22Parser.MINU, MT22Parser.MUTI, MT22Parser.DIVI, MT22Parser.MODU]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.arithmetricop()
                pass
            elif token in [MT22Parser.NOT, MT22Parser.AND, MT22Parser.OR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.booleanop()
                pass
            elif token in [MT22Parser.SCOPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 112
                self.stringop()
                pass
            elif token in [MT22Parser.EQUL, MT22Parser.NEQ, MT22Parser.LESS, MT22Parser.LOEQ, MT22Parser.GREA, MT22Parser.GOEQ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 113
                self.relationalop()
                pass
            elif token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 114
                self.indexop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MT22Parser.ConstantContext,0)


        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def operator(self):
            return self.getTypedRuleContext(MT22Parser.OperatorContext,0)


        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_operand




    def operand(self):

        localctx = MT22Parser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operand)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.vartype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.operator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.functioncall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.OperandContext)
            else:
                return self.getTypedRuleContext(MT22Parser.OperandContext,i)


        def stringop(self):
            return self.getTypedRuleContext(MT22Parser.StringopContext,0)


        def relationalop(self):
            return self.getTypedRuleContext(MT22Parser.RelationalopContext,0)


        def NOT(self):
            return self.getToken(MT22Parser.NOT, 0)

        def MINU(self):
            return self.getToken(MT22Parser.MINU, 0)

        def indexop(self):
            return self.getTypedRuleContext(MT22Parser.IndexopContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def AND(self):
            return self.getToken(MT22Parser.AND, 0)

        def OR(self):
            return self.getToken(MT22Parser.OR, 0)

        def PLUS(self):
            return self.getToken(MT22Parser.PLUS, 0)

        def MUTI(self):
            return self.getToken(MT22Parser.MUTI, 0)

        def DIVI(self):
            return self.getToken(MT22Parser.DIVI, 0)

        def MODU(self):
            return self.getToken(MT22Parser.MODU, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expression



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 124
                self.operand()
                self.state = 125
                self.stringop()
                self.state = 126
                self.operand()
                pass

            elif la_ == 2:
                self.state = 128
                self.operand()
                self.state = 129
                self.relationalop()
                self.state = 130
                self.operand()
                pass

            elif la_ == 3:
                self.state = 132
                self.match(MT22Parser.NOT)
                self.state = 133
                self.operand()
                pass

            elif la_ == 4:
                self.state = 134
                self.match(MT22Parser.MINU)
                self.state = 135
                self.operand()
                pass

            elif la_ == 5:
                self.state = 136
                self.indexop()
                self.state = 137
                self.operand()
                pass

            elif la_ == 6:
                self.state = 139
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 151
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 143
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.operand()
                        pass

                    elif la_ == 2:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 146
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINU):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.operand()
                        pass

                    elif la_ == 3:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 149
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.operand()
                        pass

             
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(MT22Parser.STR, 0)

        def BOOL(self):
            return self.getToken(MT22Parser.BOOL, 0)

        def FLO(self):
            return self.getToken(MT22Parser.FLO, 0)

        def INT(self):
            return self.getToken(MT22Parser.INT, 0)

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def ARR(self):
            return self.getToken(MT22Parser.ARR, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_constant




    def constant(self):

        localctx = MT22Parser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.ARR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctioncallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functioncall




    def functioncall(self):

        localctx = MT22Parser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functioncall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(MT22Parser.ID)
            self.state = 159
            self.match(MT22Parser.LB)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID) | (1 << MT22Parser.ARR) | (1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU) | (1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ) | (1 << MT22Parser.SCOPE))) != 0):
                self.state = 160
                self.arguementlist()


            self.state = 163
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_indexop




    def indexop(self):

        localctx = MT22Parser.IndexopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MT22Parser.ID)
            self.state = 166
            self.expressionlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_parameter




    def parameter(self):

        localctx = MT22Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 168
                self.match(MT22Parser.INHERIT)


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 171
                self.match(MT22Parser.OUT)


            self.state = 174
            self.match(MT22Parser.ID)
            self.state = 175
            self.match(MT22Parser.COL)
            self.state = 176
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexexpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MT22Parser.RULE_indexexpression




    def indexexpression(self):

        localctx = MT22Parser.IndexexpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_indexexpression)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguement




    def arguement(self):

        localctx = MT22Parser.ArguementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arguement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionmainprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MT22Parser.MAIN, 0)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionmainprot




    def functionmainprot(self):

        localctx = MT22Parser.FunctionmainprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_functionmainprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MT22Parser.MAIN)
            self.state = 183
            self.match(MT22Parser.COL)
            self.state = 184
            self.match(MT22Parser.FUNCTION)
            self.state = 185
            self.match(MT22Parser.VOID)
            self.state = 186
            self.match(MT22Parser.LB)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 187
                self.parameterlist()


            self.state = 190
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionprotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionprot




    def functionprot(self):

        localctx = MT22Parser.FunctionprotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MT22Parser.ID)
            self.state = 193
            self.match(MT22Parser.COL)
            self.state = 194
            self.match(MT22Parser.FUNCTION)
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VOID]:
                self.state = 195
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 196
                self.vartype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 199
            self.match(MT22Parser.LB)
            self.state = 200
            self.parameterlist()
            self.state = 201
            self.match(MT22Parser.RB)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 202
                self.match(MT22Parser.INHERIT)
                self.state = 203
                self.match(MT22Parser.ID)
                self.state = 204
                self.match(MT22Parser.LSB)
                self.state = 205
                self.match(MT22Parser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionbody




    def functionbody(self):

        localctx = MT22Parser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.blockstatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_scalarvar




    def scalarvar(self):

        localctx = MT22Parser.ScalarvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scalarvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(MT22Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def indexexpression(self):
            return self.getTypedRuleContext(MT22Parser.IndexexpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.scalarvar()
                pass
            elif token in [MT22Parser.EQU]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.indexexpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstatement(self):
            return self.getTypedRuleContext(MT22Parser.AssignstatementContext,0)


        def ifstatement(self):
            return self.getTypedRuleContext(MT22Parser.IfstatementContext,0)


        def forstatement(self):
            return self.getTypedRuleContext(MT22Parser.ForstatementContext,0)


        def whilestatement(self):
            return self.getTypedRuleContext(MT22Parser.WhilestatementContext,0)


        def dowhilestatement(self):
            return self.getTypedRuleContext(MT22Parser.DowhilestatementContext,0)


        def breakstatement(self):
            return self.getTypedRuleContext(MT22Parser.BreakstatementContext,0)


        def continuestatement(self):
            return self.getTypedRuleContext(MT22Parser.ContinuestatementContext,0)


        def returnstatement(self):
            return self.getTypedRuleContext(MT22Parser.ReturnstatementContext,0)


        def callstatement(self):
            return self.getTypedRuleContext(MT22Parser.CallstatementContext,0)


        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.assignstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.ifstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.forstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.whilestatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.dowhilestatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                self.breakstatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.continuestatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 223
                self.returnstatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 224
                self.callstatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 225
                self.blockstatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_assignstatement




    def assignstatement(self):

        localctx = MT22Parser.AssignstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assignstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.lhs()
            self.state = 229
            self.match(MT22Parser.EQU)
            self.state = 230
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_ifstatement




    def ifstatement(self):

        localctx = MT22Parser.IfstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MT22Parser.IF)
            self.state = 233
            self.match(MT22Parser.LB)
            self.state = 234
            self.expression(0)
            self.state = 235
            self.match(MT22Parser.RB)
            self.state = 236
            self.statement()
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(MT22Parser.ELSE)
                self.state = 238
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def scalarvar(self):
            return self.getTypedRuleContext(MT22Parser.ScalarvarContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_forstatement




    def forstatement(self):

        localctx = MT22Parser.ForstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_forstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MT22Parser.FOR)
            self.state = 242
            self.match(MT22Parser.LB)
            self.state = 243
            self.scalarvar()
            self.state = 244
            self.match(MT22Parser.EQU)
            self.state = 245
            self.expression(0)
            self.state = 246
            self.match(MT22Parser.COMA)
            self.state = 247
            self.expression(0)
            self.state = 248
            self.match(MT22Parser.COMA)
            self.state = 249
            self.expression(0)
            self.state = 250
            self.match(MT22Parser.RB)
            self.state = 251
            self.match(MT22Parser.LCB)
            self.state = 252
            self.statement()
            self.state = 253
            self.match(MT22Parser.RCB)
            self.state = 254
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_whilestatement




    def whilestatement(self):

        localctx = MT22Parser.WhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_whilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MT22Parser.WHILE)
            self.state = 257
            self.match(MT22Parser.LB)
            self.state = 258
            self.expression(0)
            self.state = 259
            self.match(MT22Parser.RB)
            self.state = 260
            self.match(MT22Parser.LCB)
            self.state = 261
            self.statement()
            self.state = 262
            self.match(MT22Parser.RCB)
            self.state = 263
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DowhilestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def blockstatement(self):
            return self.getTypedRuleContext(MT22Parser.BlockstatementContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_dowhilestatement




    def dowhilestatement(self):

        localctx = MT22Parser.DowhilestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_dowhilestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MT22Parser.DO)
            self.state = 266
            self.blockstatement()
            self.state = 267
            self.match(MT22Parser.WHILE)
            self.state = 268
            self.match(MT22Parser.LB)
            self.state = 269
            self.expression(0)
            self.state = 270
            self.match(MT22Parser.RB)
            self.state = 271
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MT22Parser.BREAK, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_breakstatement




    def breakstatement(self):

        localctx = MT22Parser.BreakstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_breakstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.BREAK)
            self.state = 274
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continuestatement




    def continuestatement(self):

        localctx = MT22Parser.ContinuestatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_continuestatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(MT22Parser.CONTINUE)
            self.state = 277
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_returnstatement




    def returnstatement(self):

        localctx = MT22Parser.ReturnstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_returnstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(MT22Parser.RETURN)
            self.state = 280
            self.expression(0)
            self.state = 281
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functioncall(self):
            return self.getTypedRuleContext(MT22Parser.FunctioncallContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_callstatement




    def callstatement(self):

        localctx = MT22Parser.CallstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_callstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.functioncall()
            self.state = 284
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def statementlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementlistContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementlistContext,i)


        def variabledecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VariabledeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VariabledeclContext,i)


        def getRuleIndex(self):
            return MT22Parser.RULE_blockstatement




    def blockstatement(self):

        localctx = MT22Parser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(MT22Parser.LCB)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 289
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 287
                        self.statementlist()
                        pass

                    elif la_ == 2:
                        self.state = 288
                        self.variabledecl()
                        pass

             
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 294
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_idlist




    def idlist(self):

        localctx = MT22Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_idlist)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(MT22Parser.ID)
                self.state = 297
                self.match(MT22Parser.COMA)
                self.state = 298
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(MT22Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expressionlist




    def expressionlist(self):

        localctx = MT22Parser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressionlist)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.expression(0)
                self.state = 303
                self.match(MT22Parser.COMA)
                self.state = 304
                self.expressionlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.expression(0)
                self.state = 308
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 307
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MT22Parser.ParameterContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def parameterlist(self):
            return self.getTypedRuleContext(MT22Parser.ParameterlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_parameterlist




    def parameterlist(self):

        localctx = MT22Parser.ParameterlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_parameterlist)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.parameter()
                self.state = 313
                self.match(MT22Parser.COMA)
                self.state = 314
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArguementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguement(self):
            return self.getTypedRuleContext(MT22Parser.ArguementContext,0)


        def COMA(self):
            return self.getToken(MT22Parser.COMA, 0)

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arguementlist




    def arguementlist(self):

        localctx = MT22Parser.ArguementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_arguementlist)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.arguement()
                self.state = 320
                self.match(MT22Parser.COMA)
                self.state = 321
                self.arguementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.arguement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statementlist




    def statementlist(self):

        localctx = MT22Parser.StatementlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_statementlist)
        self._la = 0 # Token type
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.statement()
                self.state = 327
                self.match(MT22Parser.SEM)
                self.state = 328
                self.statementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.statement()
                self.state = 332
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MT22Parser.SEM:
                    self.state = 331
                    self.match(MT22Parser.SEM)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecl




    def variabledecl(self):

        localctx = MT22Parser.VariabledeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variabledecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.variabledecls()
            self.state = 337
            self.match(MT22Parser.SEM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariabledeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MT22Parser.ID, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def expression(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionContext,0)


        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecls




    def variabledecls(self):

        localctx = MT22Parser.VariabledeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_variabledecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 339
                self.match(MT22Parser.ID)
                self.state = 340
                self.match(MT22Parser.COMA)
                self.state = 341
                self.variabledecls()
                self.state = 342
                self.match(MT22Parser.COMA)
                self.state = 343
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 345
                self.match(MT22Parser.ID)
                self.state = 346
                self.match(MT22Parser.COL)
                self.state = 347
                self.vartype()
                self.state = 348
                self.match(MT22Parser.EQU)
                self.state = 349
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 351
                self.idlist()
                self.state = 352
                self.match(MT22Parser.COL)
                self.state = 353
                self.vartype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctiondeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functiondecl




    def functiondecl(self):

        localctx = MT22Parser.FunctiondeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functiondecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.functionprot()
            self.state = 358
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainfunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionmainprot(self):
            return self.getTypedRuleContext(MT22Parser.FunctionmainprotContext,0)


        def functionbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_mainfunction




    def mainfunction(self):

        localctx = MT22Parser.MainfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_mainfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.functionmainprot()
            self.state = 361
            self.functionbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def demention(self):
            return self.getTypedRuleContext(MT22Parser.DementionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_arraydecl




    def arraydecl(self):

        localctx = MT22Parser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(MT22Parser.ARRAY)
            self.state = 364
            self.match(MT22Parser.LSB)
            self.state = 365
            self.demention()
            self.state = 366
            self.match(MT22Parser.RSB)
            self.state = 367
            self.match(MT22Parser.OF)
            self.state = 368
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mt22languageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainfunction(self):
            return self.getTypedRuleContext(MT22Parser.MainfunctionContext,0)


        def functiondecl(self):
            return self.getTypedRuleContext(MT22Parser.FunctiondeclContext,0)


        def variabledecls(self):
            return self.getTypedRuleContext(MT22Parser.VariabledeclsContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def arraydecl(self):
            return self.getTypedRuleContext(MT22Parser.ArraydeclContext,0)


        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_mt22language




    def mt22language(self):

        localctx = MT22Parser.Mt22languageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_mt22language)
        try:
            self.state = 379
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
                self.mainfunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.functiondecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 372
                self.variabledecls()
                self.state = 373
                self.match(MT22Parser.SEM)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 375
                self.arraydecl()
                self.state = 376
                self.match(MT22Parser.SEM)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 378
                self.expressionlist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         





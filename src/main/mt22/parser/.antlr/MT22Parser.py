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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u016c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2g\n")
        buf.write("\2\f\2\16\2j\13\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6")
        buf.write("\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b}\n\b\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u0083\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0096\n\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n\u00a1\n\n\f\n\16\n\u00a4")
        buf.write("\13\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\5")
        buf.write("\16\u00b1\n\16\3\16\5\16\u00b4\n\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c4\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\5\22\u00cd")
        buf.write("\n\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d6\n")
        buf.write("\22\3\23\3\23\5\23\u00da\n\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\26\3\26\5\26\u00e6\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u00f2\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u00ff\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"\u0136")
        buf.write("\n\"\3#\3#\3#\3#\3#\5#\u013d\n#\3$\3$\3$\3$\3$\5$\u0144")
        buf.write("\n$\3%\3%\3%\3%\3%\5%\u014b\n%\3&\3&\3&\3&\3&\3&\3&\5")
        buf.write("&\u0154\n&\3\'\3\'\3\'\3\'\3\'\5\'\u015b\n\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\2\3\22+\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPR\2\n\6\2\t\t\f\f\20\20\22\22\3\2\61\65\3")
        buf.write("\2\668\3\29>\3\2\678\3\2\61\62\3\2\63\65\5\2\5\5\35\37")
        buf.write("!!\2\u017a\2h\3\2\2\2\4m\3\2\2\2\6o\3\2\2\2\bq\3\2\2\2")
        buf.write("\ns\3\2\2\2\fu\3\2\2\2\16|\3\2\2\2\20\u0082\3\2\2\2\22")
        buf.write("\u0095\3\2\2\2\24\u00a5\3\2\2\2\26\u00a7\3\2\2\2\30\u00ac")
        buf.write("\3\2\2\2\32\u00b0\3\2\2\2\34\u00b9\3\2\2\2\36\u00bb\3")
        buf.write("\2\2\2 \u00bd\3\2\2\2\"\u00c7\3\2\2\2$\u00d7\3\2\2\2&")
        buf.write("\u00dd\3\2\2\2(\u00e1\3\2\2\2*\u00e5\3\2\2\2,\u00f1\3")
        buf.write("\2\2\2.\u00f3\3\2\2\2\60\u00f7\3\2\2\2\62\u0100\3\2\2")
        buf.write("\2\64\u010f\3\2\2\2\66\u0118\3\2\2\28\u0120\3\2\2\2:\u0123")
        buf.write("\3\2\2\2<\u0126\3\2\2\2>\u012a\3\2\2\2@\u012d\3\2\2\2")
        buf.write("B\u0135\3\2\2\2D\u013c\3\2\2\2F\u0143\3\2\2\2H\u014a\3")
        buf.write("\2\2\2J\u0153\3\2\2\2L\u0155\3\2\2\2N\u015e\3\2\2\2P\u0161")
        buf.write("\3\2\2\2R\u0164\3\2\2\2Tg\5\22\n\2Ug\5,\27\2Vg\5N(\2W")
        buf.write("g\5P)\2Xg\5L\'\2Yg\5R*\2Zg\7\3\2\2[g\7\4\2\2\\g\7\5\2")
        buf.write("\2]g\7\36\2\2^g\7 \2\2_g\7\37\2\2`g\7!\2\2ag\7*\2\2bg")
        buf.write("\7\"\2\2cg\7+\2\2dg\7-\2\2eg\7$\2\2fT\3\2\2\2fU\3\2\2")
        buf.write("\2fV\3\2\2\2fW\3\2\2\2fX\3\2\2\2fY\3\2\2\2fZ\3\2\2\2f")
        buf.write("[\3\2\2\2f\\\3\2\2\2f]\3\2\2\2f^\3\2\2\2f_\3\2\2\2f`\3")
        buf.write("\2\2\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2")
        buf.write("\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2k")
        buf.write("l\7\2\2\3l\3\3\2\2\2mn\t\2\2\2n\5\3\2\2\2op\t\3\2\2p\7")
        buf.write("\3\2\2\2qr\t\4\2\2r\t\3\2\2\2st\7?\2\2t\13\3\2\2\2uv\t")
        buf.write("\5\2\2v\r\3\2\2\2w}\5\6\4\2x}\5\b\5\2y}\5\n\6\2z}\5\f")
        buf.write("\7\2{}\5\30\r\2|w\3\2\2\2|x\3\2\2\2|y\3\2\2\2|z\3\2\2")
        buf.write("\2|{\3\2\2\2}\17\3\2\2\2~\u0083\5\24\13\2\177\u0083\5")
        buf.write("\4\3\2\u0080\u0083\5\16\b\2\u0081\u0083\5\26\f\2\u0082")
        buf.write("~\3\2\2\2\u0082\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0081\3\2\2\2\u0083\21\3\2\2\2\u0084\u0085\b\n\1\2\u0085")
        buf.write("\u0086\5\20\t\2\u0086\u0087\5\n\6\2\u0087\u0088\5\20\t")
        buf.write("\2\u0088\u0096\3\2\2\2\u0089\u008a\5\20\t\2\u008a\u008b")
        buf.write("\5\f\7\2\u008b\u008c\5\20\t\2\u008c\u0096\3\2\2\2\u008d")
        buf.write("\u008e\7\66\2\2\u008e\u0096\5\20\t\2\u008f\u0090\7\62")
        buf.write("\2\2\u0090\u0096\5\20\t\2\u0091\u0092\5\30\r\2\u0092\u0093")
        buf.write("\5\20\t\2\u0093\u0096\3\2\2\2\u0094\u0096\5\20\t\2\u0095")
        buf.write("\u0084\3\2\2\2\u0095\u0089\3\2\2\2\u0095\u008d\3\2\2\2")
        buf.write("\u0095\u008f\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0094\3")
        buf.write("\2\2\2\u0096\u00a2\3\2\2\2\u0097\u0098\f\t\2\2\u0098\u0099")
        buf.write("\t\6\2\2\u0099\u00a1\5\20\t\2\u009a\u009b\f\b\2\2\u009b")
        buf.write("\u009c\t\7\2\2\u009c\u00a1\5\20\t\2\u009d\u009e\f\7\2")
        buf.write("\2\u009e\u009f\t\b\2\2\u009f\u00a1\5\20\t\2\u00a0\u0097")
        buf.write("\3\2\2\2\u00a0\u009a\3\2\2\2\u00a0\u009d\3\2\2\2\u00a1")
        buf.write("\u00a4\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\23\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\t\t")
        buf.write("\2\2\u00a6\25\3\2\2\2\u00a7\u00a8\7!\2\2\u00a8\u00a9\7")
        buf.write("(\2\2\u00a9\u00aa\5H%\2\u00aa\u00ab\7)\2\2\u00ab\27\3")
        buf.write("\2\2\2\u00ac\u00ad\7!\2\2\u00ad\u00ae\5D#\2\u00ae\31\3")
        buf.write("\2\2\2\u00af\u00b1\7\30\2\2\u00b0\u00af\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00b4\7\25\2")
        buf.write("\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b6\7!\2\2\u00b6\u00b7\7#\2\2\u00b7\u00b8")
        buf.write("\5\4\3\2\u00b8\33\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\35")
        buf.write("\3\2\2\2\u00bb\u00bc\5\22\n\2\u00bc\37\3\2\2\2\u00bd\u00be")
        buf.write("\7\32\2\2\u00be\u00bf\7#\2\2\u00bf\u00c0\7\16\2\2\u00c0")
        buf.write("\u00c1\7\24\2\2\u00c1\u00c3\7(\2\2\u00c2\u00c4\5F$\2\u00c3")
        buf.write("\u00c2\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\7)\2\2\u00c6!\3\2\2\2\u00c7\u00c8\7!\2\2")
        buf.write("\u00c8\u00c9\7#\2\2\u00c9\u00cc\7\16\2\2\u00ca\u00cd\7")
        buf.write("\24\2\2\u00cb\u00cd\5\4\3\2\u00cc\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00cf\7(\2\2")
        buf.write("\u00cf\u00d0\5F$\2\u00d0\u00d5\7)\2\2\u00d1\u00d2\7\30")
        buf.write("\2\2\u00d2\u00d3\7!\2\2\u00d3\u00d4\7&\2\2\u00d4\u00d6")
        buf.write("\7\'\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("#\3\2\2\2\u00d7\u00d9\7*\2\2\u00d8\u00da\5J&\2\u00d9\u00d8")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dc\7+\2\2\u00dc%\3\2\2\2\u00dd\u00de\7*\2\2\u00de")
        buf.write("\u00df\5J&\2\u00df\u00e0\7+\2\2\u00e0\'\3\2\2\2\u00e1")
        buf.write("\u00e2\7!\2\2\u00e2)\3\2\2\2\u00e3\u00e6\5(\25\2\u00e4")
        buf.write("\u00e6\5\34\17\2\u00e5\u00e3\3\2\2\2\u00e5\u00e4\3\2\2")
        buf.write("\2\u00e6+\3\2\2\2\u00e7\u00f2\5.\30\2\u00e8\u00f2\5\60")
        buf.write("\31\2\u00e9\u00f2\5\62\32\2\u00ea\u00f2\5\64\33\2\u00eb")
        buf.write("\u00f2\5\66\34\2\u00ec\u00f2\58\35\2\u00ed\u00f2\5:\36")
        buf.write("\2\u00ee\u00f2\5<\37\2\u00ef\u00f2\5> \2\u00f0\u00f2\5")
        buf.write("@!\2\u00f1\u00e7\3\2\2\2\u00f1\u00e8\3\2\2\2\u00f1\u00e9")
        buf.write("\3\2\2\2\u00f1\u00ea\3\2\2\2\u00f1\u00eb\3\2\2\2\u00f1")
        buf.write("\u00ec\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f1\u00ee\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2-\3\2\2")
        buf.write("\2\u00f3\u00f4\5*\26\2\u00f4\u00f5\7,\2\2\u00f5\u00f6")
        buf.write("\5\22\n\2\u00f6/\3\2\2\2\u00f7\u00f8\7\17\2\2\u00f8\u00f9")
        buf.write("\7(\2\2\u00f9\u00fa\5\22\n\2\u00fa\u00fb\7)\2\2\u00fb")
        buf.write("\u00fe\5,\27\2\u00fc\u00fd\7\13\2\2\u00fd\u00ff\5,\27")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\61\3")
        buf.write("\2\2\2\u0100\u0101\7\r\2\2\u0101\u0102\7(\2\2\u0102\u0103")
        buf.write("\5(\25\2\u0103\u0104\7,\2\2\u0104\u0105\5\22\n\2\u0105")
        buf.write("\u0106\7\"\2\2\u0106\u0107\5\22\n\2\u0107\u0108\7\"\2")
        buf.write("\2\u0108\u0109\5\22\n\2\u0109\u010a\7)\2\2\u010a\u010b")
        buf.write("\7*\2\2\u010b\u010c\5,\27\2\u010c\u010d\7+\2\2\u010d\u010e")
        buf.write("\7$\2\2\u010e\63\3\2\2\2\u010f\u0110\7\23\2\2\u0110\u0111")
        buf.write("\7(\2\2\u0111\u0112\5\22\n\2\u0112\u0113\7)\2\2\u0113")
        buf.write("\u0114\7*\2\2\u0114\u0115\5,\27\2\u0115\u0116\7+\2\2\u0116")
        buf.write("\u0117\7$\2\2\u0117\65\3\2\2\2\u0118\u0119\7\n\2\2\u0119")
        buf.write("\u011a\5@!\2\u011a\u011b\7\23\2\2\u011b\u011c\7(\2\2\u011c")
        buf.write("\u011d\5\22\n\2\u011d\u011e\7)\2\2\u011e\u011f\7$\2\2")
        buf.write("\u011f\67\3\2\2\2\u0120\u0121\7\b\2\2\u0121\u0122\7$\2")
        buf.write("\2\u01229\3\2\2\2\u0123\u0124\7\26\2\2\u0124\u0125\7$")
        buf.write("\2\2\u0125;\3\2\2\2\u0126\u0127\7\21\2\2\u0127\u0128\5")
        buf.write("\22\n\2\u0128\u0129\7$\2\2\u0129=\3\2\2\2\u012a\u012b")
        buf.write("\5\26\f\2\u012b\u012c\7$\2\2\u012c?\3\2\2\2\u012d\u012e")
        buf.write("\7*\2\2\u012e\u012f\5J&\2\u012f\u0130\7+\2\2\u0130A\3")
        buf.write("\2\2\2\u0131\u0132\7!\2\2\u0132\u0133\7\"\2\2\u0133\u0136")
        buf.write("\5B\"\2\u0134\u0136\7!\2\2\u0135\u0131\3\2\2\2\u0135\u0134")
        buf.write("\3\2\2\2\u0136C\3\2\2\2\u0137\u0138\5\22\n\2\u0138\u0139")
        buf.write("\7\"\2\2\u0139\u013a\5D#\2\u013a\u013d\3\2\2\2\u013b\u013d")
        buf.write("\5\22\n\2\u013c\u0137\3\2\2\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("E\3\2\2\2\u013e\u013f\5\32\16\2\u013f\u0140\7\"\2\2\u0140")
        buf.write("\u0141\5F$\2\u0141\u0144\3\2\2\2\u0142\u0144\5\32\16\2")
        buf.write("\u0143\u013e\3\2\2\2\u0143\u0142\3\2\2\2\u0144G\3\2\2")
        buf.write("\2\u0145\u0146\5\36\20\2\u0146\u0147\7\"\2\2\u0147\u0148")
        buf.write("\5H%\2\u0148\u014b\3\2\2\2\u0149\u014b\5\36\20\2\u014a")
        buf.write("\u0145\3\2\2\2\u014a\u0149\3\2\2\2\u014bI\3\2\2\2\u014c")
        buf.write("\u014d\5,\27\2\u014d\u014e\7$\2\2\u014e\u014f\5J&\2\u014f")
        buf.write("\u0154\3\2\2\2\u0150\u0151\5,\27\2\u0151\u0152\7$\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u014c\3\2\2\2\u0153\u0150\3")
        buf.write("\2\2\2\u0154K\3\2\2\2\u0155\u0156\5B\"\2\u0156\u0157\7")
        buf.write("#\2\2\u0157\u015a\5\4\3\2\u0158\u0159\7,\2\2\u0159\u015b")
        buf.write("\5D#\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015d\7$\2\2\u015dM\3\2\2\2\u015e\u015f")
        buf.write("\5\"\22\2\u015f\u0160\5&\24\2\u0160O\3\2\2\2\u0161\u0162")
        buf.write("\5 \21\2\u0162\u0163\5$\23\2\u0163Q\3\2\2\2\u0164\u0165")
        buf.write("\7\31\2\2\u0165\u0166\7&\2\2\u0166\u0167\7 \2\2\u0167")
        buf.write("\u0168\7\'\2\2\u0168\u0169\7\27\2\2\u0169\u016a\7\20\2")
        buf.write("\2\u016aS\3\2\2\2\30fh|\u0082\u0095\u00a0\u00a2\u00b0")
        buf.write("\u00b3\u00c3\u00cc\u00d5\u00d9\u00e5\u00f1\u00fe\u0135")
        buf.write("\u013c\u0143\u014a\u0153\u015a")
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
                     "'main'", "'false'", "'true'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "':'", 
                     "';'", "'.'", "'['", "']'", "'('", "')'", "'{'", "'}'", 
                     "'='", "<INVALID>", "'\"'", "'0'", "'_'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'::'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_C", "COMMENT_CPP", "STR", "STRTYP", 
                      "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", 
                      "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                      "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                      "ARRAY", "MAIN", "FALSE", "TRUE", "BOOL", "FLO", "INT", 
                      "DEMENTION", "ID", "COMA", "COL", "SEM", "DOT", "LSB", 
                      "RSB", "LB", "RB", "LCB", "RCB", "EQU", "ARR", "DB", 
                      "ZERO", "UNDE", "PLUS", "MINU", "MUTI", "DIVI", "MODU", 
                      "NOT", "AND", "OR", "EQUL", "NEQ", "LESS", "LOEQ", 
                      "GREA", "GOEQ", "SCOPE", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_vartype = 1
    RULE_arithmetricop = 2
    RULE_booleanop = 3
    RULE_stringop = 4
    RULE_relationalop = 5
    RULE_operator = 6
    RULE_operand = 7
    RULE_expression = 8
    RULE_constant = 9
    RULE_functioncall = 10
    RULE_indexop = 11
    RULE_parameter = 12
    RULE_indexexpression = 13
    RULE_arguement = 14
    RULE_functionmainprot = 15
    RULE_functionprot = 16
    RULE_functionmainbody = 17
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
    RULE_functiondecl = 38
    RULE_mainfunction = 39
    RULE_arraytype = 40

    ruleNames =  [ "program", "vartype", "arithmetricop", "booleanop", "stringop", 
                   "relationalop", "operator", "operand", "expression", 
                   "constant", "functioncall", "indexop", "parameter", "indexexpression", 
                   "arguement", "functionmainprot", "functionprot", "functionmainbody", 
                   "functionbody", "scalarvar", "lhs", "statement", "assignstatement", 
                   "ifstatement", "forstatement", "whilestatement", "dowhilestatement", 
                   "breakstatement", "continuestatement", "returnstatement", 
                   "callstatement", "blockstatement", "idlist", "expressionlist", 
                   "parameterlist", "arguementlist", "statementlist", "variabledecl", 
                   "functiondecl", "mainfunction", "arraytype" ]

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
    FALSE=25
    TRUE=26
    BOOL=27
    FLO=28
    INT=29
    DEMENTION=30
    ID=31
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
    ARR=43
    DB=44
    ZERO=45
    UNDE=46
    PLUS=47
    MINU=48
    MUTI=49
    DIVI=50
    MODU=51
    NOT=52
    AND=53
    OR=54
    EQUL=55
    NEQ=56
    LESS=57
    LOEQ=58
    GREA=59
    GOEQ=60
    SCOPE=61
    WS=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65

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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExpressionContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.StatementContext)
            else:
                return self.getTypedRuleContext(MT22Parser.StatementContext,i)


        def functiondecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.FunctiondeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.FunctiondeclContext,i)


        def mainfunction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.MainfunctionContext)
            else:
                return self.getTypedRuleContext(MT22Parser.MainfunctionContext,i)


        def variabledecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.VariabledeclContext)
            else:
                return self.getTypedRuleContext(MT22Parser.VariabledeclContext,i)


        def arraytype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ArraytypeContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ArraytypeContext,i)


        def COMMENT_C(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMENT_C)
            else:
                return self.getToken(MT22Parser.COMMENT_C, i)

        def COMMENT_CPP(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMENT_CPP)
            else:
                return self.getToken(MT22Parser.COMMENT_CPP, i)

        def STR(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.STR)
            else:
                return self.getToken(MT22Parser.STR, i)

        def FLO(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.FLO)
            else:
                return self.getToken(MT22Parser.FLO, i)

        def DEMENTION(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.DEMENTION)
            else:
                return self.getToken(MT22Parser.DEMENTION, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.INT)
            else:
                return self.getToken(MT22Parser.INT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ID)
            else:
                return self.getToken(MT22Parser.ID, i)

        def LCB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.LCB)
            else:
                return self.getToken(MT22Parser.LCB, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMA)
            else:
                return self.getToken(MT22Parser.COMA, i)

        def RCB(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.RCB)
            else:
                return self.getToken(MT22Parser.RCB, i)

        def ARR(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.ARR)
            else:
                return self.getToken(MT22Parser.ARR, i)

        def SEM(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.SEM)
            else:
                return self.getToken(MT22Parser.SEM, i)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.COMMENT_C) | (1 << MT22Parser.COMMENT_CPP) | (1 << MT22Parser.STR) | (1 << MT22Parser.BREAK) | (1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.DO) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.STRING) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ARRAY) | (1 << MT22Parser.MAIN) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.DEMENTION) | (1 << MT22Parser.ID) | (1 << MT22Parser.COMA) | (1 << MT22Parser.SEM) | (1 << MT22Parser.LCB) | (1 << MT22Parser.RCB) | (1 << MT22Parser.EQU) | (1 << MT22Parser.ARR) | (1 << MT22Parser.PLUS) | (1 << MT22Parser.MINU) | (1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU) | (1 << MT22Parser.NOT) | (1 << MT22Parser.AND) | (1 << MT22Parser.OR) | (1 << MT22Parser.EQUL) | (1 << MT22Parser.NEQ) | (1 << MT22Parser.LESS) | (1 << MT22Parser.LOEQ) | (1 << MT22Parser.GREA) | (1 << MT22Parser.GOEQ) | (1 << MT22Parser.SCOPE))) != 0):
                self.state = 100
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 82
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 83
                    self.statement()
                    pass

                elif la_ == 3:
                    self.state = 84
                    self.functiondecl()
                    pass

                elif la_ == 4:
                    self.state = 85
                    self.mainfunction()
                    pass

                elif la_ == 5:
                    self.state = 86
                    self.variabledecl()
                    pass

                elif la_ == 6:
                    self.state = 87
                    self.arraytype()
                    pass

                elif la_ == 7:
                    self.state = 88
                    self.match(MT22Parser.COMMENT_C)
                    pass

                elif la_ == 8:
                    self.state = 89
                    self.match(MT22Parser.COMMENT_CPP)
                    pass

                elif la_ == 9:
                    self.state = 90
                    self.match(MT22Parser.STR)
                    pass

                elif la_ == 10:
                    self.state = 91
                    self.match(MT22Parser.FLO)
                    pass

                elif la_ == 11:
                    self.state = 92
                    self.match(MT22Parser.DEMENTION)
                    pass

                elif la_ == 12:
                    self.state = 93
                    self.match(MT22Parser.INT)
                    pass

                elif la_ == 13:
                    self.state = 94
                    self.match(MT22Parser.ID)
                    pass

                elif la_ == 14:
                    self.state = 95
                    self.match(MT22Parser.LCB)
                    pass

                elif la_ == 15:
                    self.state = 96
                    self.match(MT22Parser.COMA)
                    pass

                elif la_ == 16:
                    self.state = 97
                    self.match(MT22Parser.RCB)
                    pass

                elif la_ == 17:
                    self.state = 98
                    self.match(MT22Parser.ARR)
                    pass

                elif la_ == 18:
                    self.state = 99
                    self.match(MT22Parser.SEM)
                    pass


                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
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
            self.state = 107
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
            self.state = 109
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
            self.state = 111
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
            self.state = 113
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
            self.state = 115
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
        self.enterRule(localctx, 12, self.RULE_operator)
        try:
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.PLUS, MT22Parser.MINU, MT22Parser.MUTI, MT22Parser.DIVI, MT22Parser.MODU]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.arithmetricop()
                pass
            elif token in [MT22Parser.NOT, MT22Parser.AND, MT22Parser.OR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.booleanop()
                pass
            elif token in [MT22Parser.SCOPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.stringop()
                pass
            elif token in [MT22Parser.EQUL, MT22Parser.NEQ, MT22Parser.LESS, MT22Parser.LOEQ, MT22Parser.GREA, MT22Parser.GOEQ]:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.relationalop()
                pass
            elif token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
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
        self.enterRule(localctx, 14, self.RULE_operand)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.vartype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.operator()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 127
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 131
                self.operand()
                self.state = 132
                self.stringop()
                self.state = 133
                self.operand()
                pass

            elif la_ == 2:
                self.state = 135
                self.operand()
                self.state = 136
                self.relationalop()
                self.state = 137
                self.operand()
                pass

            elif la_ == 3:
                self.state = 139
                self.match(MT22Parser.NOT)
                self.state = 140
                self.operand()
                pass

            elif la_ == 4:
                self.state = 141
                self.match(MT22Parser.MINU)
                self.state = 142
                self.operand()
                pass

            elif la_ == 5:
                self.state = 143
                self.indexop()
                self.state = 144
                self.operand()
                pass

            elif la_ == 6:
                self.state = 146
                self.operand()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 149
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 150
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.AND or _la==MT22Parser.OR):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 151
                        self.operand()
                        pass

                    elif la_ == 2:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 152
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 153
                        _la = self._input.LA(1)
                        if not(_la==MT22Parser.PLUS or _la==MT22Parser.MINU):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 154
                        self.operand()
                        pass

                    elif la_ == 3:
                        localctx = MT22Parser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 155
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 156
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MUTI) | (1 << MT22Parser.DIVI) | (1 << MT22Parser.MODU))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 157
                        self.operand()
                        pass

             
                self.state = 162
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

        def getRuleIndex(self):
            return MT22Parser.RULE_constant




    def constant(self):

        localctx = MT22Parser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.STR) | (1 << MT22Parser.BOOL) | (1 << MT22Parser.FLO) | (1 << MT22Parser.INT) | (1 << MT22Parser.ID))) != 0)):
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

        def arguementlist(self):
            return self.getTypedRuleContext(MT22Parser.ArguementlistContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functioncall




    def functioncall(self):

        localctx = MT22Parser.FunctioncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functioncall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MT22Parser.ID)
            self.state = 166
            self.match(MT22Parser.LB)
            self.state = 167
            self.arguementlist()
            self.state = 168
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
        self.enterRule(localctx, 22, self.RULE_indexop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MT22Parser.ID)
            self.state = 171
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
        self.enterRule(localctx, 24, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 173
                self.match(MT22Parser.INHERIT)


            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.OUT:
                self.state = 176
                self.match(MT22Parser.OUT)


            self.state = 179
            self.match(MT22Parser.ID)
            self.state = 180
            self.match(MT22Parser.COL)
            self.state = 181
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
        self.enterRule(localctx, 26, self.RULE_indexexpression)
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
        self.enterRule(localctx, 28, self.RULE_arguement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
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
        self.enterRule(localctx, 30, self.RULE_functionmainprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(MT22Parser.MAIN)
            self.state = 188
            self.match(MT22Parser.COL)
            self.state = 189
            self.match(MT22Parser.FUNCTION)
            self.state = 190
            self.match(MT22Parser.VOID)
            self.state = 191
            self.match(MT22Parser.LB)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.OUT) | (1 << MT22Parser.INHERIT) | (1 << MT22Parser.ID))) != 0):
                self.state = 192
                self.parameterlist()


            self.state = 195
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
        self.enterRule(localctx, 32, self.RULE_functionprot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(MT22Parser.ID)
            self.state = 198
            self.match(MT22Parser.COL)
            self.state = 199
            self.match(MT22Parser.FUNCTION)
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VOID]:
                self.state = 200
                self.match(MT22Parser.VOID)
                pass
            elif token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 201
                self.vartype()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 204
            self.match(MT22Parser.LB)
            self.state = 205
            self.parameterlist()
            self.state = 206
            self.match(MT22Parser.RB)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.INHERIT:
                self.state = 207
                self.match(MT22Parser.INHERIT)
                self.state = 208
                self.match(MT22Parser.ID)
                self.state = 209
                self.match(MT22Parser.LSB)
                self.state = 210
                self.match(MT22Parser.RSB)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionmainbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_functionmainbody




    def functionmainbody(self):

        localctx = MT22Parser.FunctionmainbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_functionmainbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MT22Parser.LCB)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BREAK) | (1 << MT22Parser.DO) | (1 << MT22Parser.FOR) | (1 << MT22Parser.IF) | (1 << MT22Parser.RETURN) | (1 << MT22Parser.WHILE) | (1 << MT22Parser.CONTINUE) | (1 << MT22Parser.ID) | (1 << MT22Parser.LCB) | (1 << MT22Parser.EQU))) != 0):
                self.state = 214
                self.statementlist()


            self.state = 217
            self.match(MT22Parser.RCB)
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

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_functionbody




    def functionbody(self):

        localctx = MT22Parser.FunctionbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_functionbody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(MT22Parser.LCB)
            self.state = 220
            self.statementlist()
            self.state = 221
            self.match(MT22Parser.RCB)
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
            self.state = 223
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
            self.state = 227
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.scalarvar()
                pass
            elif token in [MT22Parser.EQU]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.assignstatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.ifstatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 231
                self.forstatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 232
                self.whilestatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 233
                self.dowhilestatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 234
                self.breakstatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 235
                self.continuestatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 236
                self.returnstatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 237
                self.callstatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 238
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
            self.state = 241
            self.lhs()
            self.state = 242
            self.match(MT22Parser.EQU)
            self.state = 243
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
            self.state = 245
            self.match(MT22Parser.IF)
            self.state = 246
            self.match(MT22Parser.LB)
            self.state = 247
            self.expression(0)
            self.state = 248
            self.match(MT22Parser.RB)
            self.state = 249
            self.statement()
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 250
                self.match(MT22Parser.ELSE)
                self.state = 251
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
            self.state = 254
            self.match(MT22Parser.FOR)
            self.state = 255
            self.match(MT22Parser.LB)
            self.state = 256
            self.scalarvar()
            self.state = 257
            self.match(MT22Parser.EQU)
            self.state = 258
            self.expression(0)
            self.state = 259
            self.match(MT22Parser.COMA)
            self.state = 260
            self.expression(0)
            self.state = 261
            self.match(MT22Parser.COMA)
            self.state = 262
            self.expression(0)
            self.state = 263
            self.match(MT22Parser.RB)
            self.state = 264
            self.match(MT22Parser.LCB)
            self.state = 265
            self.statement()
            self.state = 266
            self.match(MT22Parser.RCB)
            self.state = 267
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
            self.state = 269
            self.match(MT22Parser.WHILE)
            self.state = 270
            self.match(MT22Parser.LB)
            self.state = 271
            self.expression(0)
            self.state = 272
            self.match(MT22Parser.RB)
            self.state = 273
            self.match(MT22Parser.LCB)
            self.state = 274
            self.statement()
            self.state = 275
            self.match(MT22Parser.RCB)
            self.state = 276
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
            self.state = 278
            self.match(MT22Parser.DO)
            self.state = 279
            self.blockstatement()
            self.state = 280
            self.match(MT22Parser.WHILE)
            self.state = 281
            self.match(MT22Parser.LB)
            self.state = 282
            self.expression(0)
            self.state = 283
            self.match(MT22Parser.RB)
            self.state = 284
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
            self.state = 286
            self.match(MT22Parser.BREAK)
            self.state = 287
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
            self.state = 289
            self.match(MT22Parser.CONTINUE)
            self.state = 290
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
            self.state = 292
            self.match(MT22Parser.RETURN)
            self.state = 293
            self.expression(0)
            self.state = 294
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
            self.state = 296
            self.functioncall()
            self.state = 297
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

        def statementlist(self):
            return self.getTypedRuleContext(MT22Parser.StatementlistContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_blockstatement




    def blockstatement(self):

        localctx = MT22Parser.BlockstatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_blockstatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MT22Parser.LCB)
            self.state = 300
            self.statementlist()
            self.state = 301
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
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(MT22Parser.ID)
                self.state = 304
                self.match(MT22Parser.COMA)
                self.state = 305
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
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


        def getRuleIndex(self):
            return MT22Parser.RULE_expressionlist




    def expressionlist(self):

        localctx = MT22Parser.ExpressionlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expressionlist)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.expression(0)
                self.state = 310
                self.match(MT22Parser.COMA)
                self.state = 311
                self.expressionlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.expression(0)
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
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.parameter()
                self.state = 317
                self.match(MT22Parser.COMA)
                self.state = 318
                self.parameterlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
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
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.arguement()
                self.state = 324
                self.match(MT22Parser.COMA)
                self.state = 325
                self.arguementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
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
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.statement()
                self.state = 331
                self.match(MT22Parser.SEM)
                self.state = 332
                self.statementlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.statement()
                self.state = 335
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

        def idlist(self):
            return self.getTypedRuleContext(MT22Parser.IdlistContext,0)


        def COL(self):
            return self.getToken(MT22Parser.COL, 0)

        def vartype(self):
            return self.getTypedRuleContext(MT22Parser.VartypeContext,0)


        def SEM(self):
            return self.getToken(MT22Parser.SEM, 0)

        def EQU(self):
            return self.getToken(MT22Parser.EQU, 0)

        def expressionlist(self):
            return self.getTypedRuleContext(MT22Parser.ExpressionlistContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variabledecl




    def variabledecl(self):

        localctx = MT22Parser.VariabledeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variabledecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.idlist()
            self.state = 340
            self.match(MT22Parser.COL)
            self.state = 341
            self.vartype()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MT22Parser.EQU:
                self.state = 342
                self.match(MT22Parser.EQU)
                self.state = 343
                self.expressionlist()


            self.state = 346
            self.match(MT22Parser.SEM)
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
        self.enterRule(localctx, 76, self.RULE_functiondecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.functionprot()
            self.state = 349
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


        def functionmainbody(self):
            return self.getTypedRuleContext(MT22Parser.FunctionmainbodyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_mainfunction




    def mainfunction(self):

        localctx = MT22Parser.MainfunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_mainfunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.functionmainprot()
            self.state = 352
            self.functionmainbody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def DEMENTION(self):
            return self.getToken(MT22Parser.DEMENTION, 0)

        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_arraytype




    def arraytype(self):

        localctx = MT22Parser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_arraytype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(MT22Parser.ARRAY)
            self.state = 355
            self.match(MT22Parser.LSB)
            self.state = 356
            self.match(MT22Parser.DEMENTION)
            self.state = 357
            self.match(MT22Parser.RSB)
            self.state = 358
            self.match(MT22Parser.OF)
            self.state = 359
            self.match(MT22Parser.INTEGER)
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
        self._predicates[8] = self.expression_sempred
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
         





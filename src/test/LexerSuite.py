import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test_Uppercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("Test", "Test,<EOF>", 102))

    def test_UnderscoreAndNumber_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_test12", "_test12,<EOF>", 103))

    # def test_ErrorNumber_identifier(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("12_test", "12_test,<EOF>", 104))

    def test_Character_Set(self):
        """test character set"""
        self.assertTrue(TestLexer.test("Iden1 \n \b \r \fIden2", "Iden1,Error Token ", 105))

    def test_Comment_C(self):
        """test Comment """
        self.assertTrue(TestLexer.test("Var //thislineiscomment \n ThisIsVar ","Var,ThisIsVar,<EOF>", 106))

    def test_Comment_Cpp(self):
        """test Comment """
        self.assertTrue(TestLexer.test("Var /*thislineiscomment \n ThisIsVar */ ", "Var,<EOF>", 107))

    def test_KeyWord(self):
        """KeyWord """
        self.assertTrue(TestLexer.test("auto \n break \n boolean\n do else false float\n for function if integer return string true while void out continue\n of inherit \narray", "auto,break,boolean,do,else,false,float,for,function,if,integer,return,string,true,while,void,out,continue,of,inherit,array,<EOF>", 108))

    def test_Operator(self):
        """test Operator """
        self.assertTrue(TestLexer.test("+ - * / % ! && || == != < <= > >= ::", "+,-,*,/,%,!,&&,||,==,!=,<,<=,>,>=,::,<EOF>", 109))

    def test_Separator(self):
        """test Separator """
        self.assertTrue(TestLexer.test("( ) [ ] . , ; : { } =", "(,),[,],.,,,;,:,{,},=,<EOF>", 110))

    def test_Integer(self):
        """test Integer """
        self.assertTrue(TestLexer.test("1234\n12\n1_2_3\n12_234", "1234,12,123,12234,<EOF>", 111))
    
    def test_Zero(self):
        """test Integer zero """
        self.assertTrue(TestLexer.test("0a12", "0,a12,<EOF>", 112))

    def test_Integer2(self):
        """test Integer """
        self.assertTrue(TestLexer.test("0 aa12 0_12", "0,aa12,0,_12,<EOF>", 113))

    def test_Integer3(self):
        """test Integer """
        self.assertTrue(TestLexer.test("123_456", "123456,<EOF>", 114))

    def test_decimal(self):
        """test decimal"""
        self.assertTrue(TestLexer.test(".0987", ".,0,987,<EOF>", 115))
    def test_decimal2(self):
        """test decimal2"""
        self.assertTrue(TestLexer.test("1.234 1.2e3 7E-10 1_234.567", "1.234,1.2e3,7E-10,1234.567,<EOF>", 116))
    
    def test_decimal3(self):
        """test decimal2"""
        self.assertTrue(TestLexer.test("1_23.234 1_3_4.2e3 7E-10 1_234.567", "123.234,134.2e3,7E-10,1234.567,<EOF>", 117))

    def test_bool(self):
        """test bool"""
        self.assertTrue(TestLexer.test("true false false3 34true", "true,false,false3,34,true,<EOF>", 118))

    def test_String(self):
        """test bool"""
        self.assertTrue(TestLexer.test("\"Hello world\"", "Hello world,<EOF>", 119))

    def test_String3(self):
        """test bool"""
        self.assertTrue(TestLexer.test("\"Hello\\nworld\\nThis is a string containing tab\\t\"", "Hello\\nworld\\nThis is a string containing tab\\t,<EOF>", 120))

    def test_String4(self):
        """test String"""
        self.assertTrue(TestLexer.test("\"The first is a close string\"\n\"This is a unclose string", "The first is a close string,Unclosed String: This is a unclose string", 121))

    def test_String5(self):
        """test String again"""
        self.assertTrue(TestLexer.test("\"Bac Ho noi \\\" Yeu to quoc yeu dong bao,... \\\" \"", "Bac Ho noi \\\" Yeu to quoc yeu dong bao,... \\\" ,<EOF>", 122))

    def testArray(self):
        """test TestArray"""
        self.assertTrue(TestLexer.test("{1, 5, 7, 12}", "{1,5,7,12},<EOF>", 123))

    def testArray2(self):
        """test TestArray2"""
        self.assertTrue(TestLexer.test("{\"Kangxi\"    , \"Yongzheng\", \"Qianlong\"}", "{\"Kangxi\",\"Yongzheng\",\"Qianlong\"},<EOF>", 124))

    def testArray3(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{1.2, 3.4,   5.6, 7_88.2}", "{1.2,3.4,5.6,7_88.2},<EOF>", 125))

    def testArray4(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{true, true, false, false}", "{true,true,false,false},<EOF>", 126))\
        
    def testArray5(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{1,2,3,4,5.4,5_6.34,true}", "{1,2,3,4,5.4,5_6.34,true},<EOF>", 127))

    def testArray6(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 128))
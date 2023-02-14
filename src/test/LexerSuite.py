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
        self.assertTrue(TestLexer.test("Iden1 \n \b \r \fIden2", "Iden1,Iden2,<EOF>", 105))

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
        self.assertTrue(TestLexer.test("0a12", "Error Token 0", 112))

    def test_Integer2(self):
        """test Integer """
        self.assertTrue(TestLexer.test("0 aa12 0_12", "0,aa12,Error Token 0", 113))

    def test_Integer3(self):
        """test Integer """
        self.assertTrue(TestLexer.test("123_456", "123456,<EOF>", 114))

    def test_decimal(self):
        """test decimal"""
        self.assertTrue(TestLexer.test(".0987", ".,Error Token 0", 115))
    def test_decimal2(self):
        """test decimal2"""
        self.assertTrue(TestLexer.test("0.0987 0.123e12 114e2 12.e2", "0.0987,0.123e12,114e2,Error Token 1", 116))


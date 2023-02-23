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
        self.assertTrue(TestLexer.test("{1, 5, 7, 12}", "{1, 5, 7, 12},<EOF>", 123))

    def testArray2(self):
        """test TestArray2"""
        self.assertTrue(TestLexer.test("{\"Kangxi\"    , \"Yongzheng\", \"Qianlong\"}", "{\"Kangxi\"    , \"Yongzheng\", \"Qianlong\"},<EOF>", 124))

    def testArray3(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{1.2, 3.4,   5.6, 7_88.2}", "{1.2, 3.4,   5.6, 7_88.2},<EOF>", 125))

    def testArray4(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{true, true, false, false}", "{true, true, false, false},<EOF>", 126))\
        
    def testArray5(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("{1,2,3,4,5.4,5_6.34,true}", "{1,2,3,4,5.4,5_6.34,true},<EOF>", 127))

    def testArray6(self):
        """test testArray"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 128))

    def testunclosestring(self):
        """test testArray"""
        self.assertTrue(TestLexer.test(""""He"llooooo" """, """He,llooooo,Unclosed String:  """, 129))

    def test_int_lit(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.test(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            130
        ))
    
    def test_real_lit(self):
        """ Test Real Literal """
        self.assertTrue(TestLexer.test(
            r"""
1.2 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42
     12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1e2,1.2E-2,1.2e-2,.1E2,9.0,12e8,0.33E-3,128e-42,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            131
        ))

    def test_escape_singlequote(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
" abc \' xyz "
""",

            r" abc \' xyz ,<EOF>",
            132
        ))
    
    def test_34_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc" 123 __123 "abc xyz"
" abc\m "
""",

            "abc,123,__123,abc xyz,Illegal Escape In String:  abc\m",
            133
        ))

    def test_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
!== != & ^ % $ # ... \
""",

            "!=,=,!=,Error Token &",
            134
        ))

    def test_err_tok2(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
if a != b then
""",

            "if,a,!=,b,then,<EOF>",
            135
        ))

    def test_err_tok3(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.test(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            136
        ))
    
    def test_num_leading(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
1234 0000001234 0000043123
""",
            "1234,0,0,0,0,0,0,1234,0,0,0,0,0,43123,<EOF>",
            137
        ))
        

    def test_38_num_leading1(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.test(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",
            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            138
        ))

    def testillegalescape(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            139
        ))
    
    def testillegalescape2(self):
        """ Test Error String """
        self.assertTrue(TestLexer.test(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            140
        ))
    
    def test_escape_backsplash_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            141
        ))

    def test_escape_backsplash_trim(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            142
        ))
    
    def test_escape_backsplash_tail_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.test(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            143
        ))
        

    def test_unclose_use_escape(self):
        """test testArray"""
        self.assertTrue(TestLexer.test(r""""\"""", r"""Unclosed String: \"""", 144))

    def test__unclose_eof(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.test(
            r"""
s = "abc""",

            r"s,=,Unclosed String: abc",
            144
        ))

    def test_unclose_newline(self):
        """ Test Unclosed """
        self.assertTrue(TestLexer.test(
            "s = \"abc;\na = \"xyz\""
            ,"s,=,Unclosed String: abc;\n",145
        ))

    def test_complex(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    while 1<2<3<4<5 do ok();
end
""",

            r"procedure,foo,(,),;,begin,while,1,<,2,<,3,<,4,<,5,do,ok,(,),;,end,<EOF>",
            146
        ))
    
    def test_complex2(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a: string do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,:,string,do,ok,(,),;,end,<EOF>",
            147
        ))

    def test_complex2(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    with a,b,c,d:string; f:integer do ok();
end
""",

            r"procedure,foo,(,),;,begin,with,a,,,b,,,c,,,d,:,string,;,f,:,integer,do,ok,(,),;,end,<EOF>",
            148
        ))

    def test_complex3(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
var a: real;
begin
    for i := 1 to 10 do begin
        for j := i downto 1 do
            if (i + j) mod 2 = 1 then continue break;
    end
end
""",

            r"procedure,foo,(,),;,var,a,:,real,;,begin,for,i,:,=,1,to,10,do,begin,for,j,:,=,i,downto,1,do,if,(,i,+,j,),mod,2,=,1,then,continue,break,;,end,end,<EOF>",
            149
        ))

    def test_complex4(self):
        """ Test Complex Function """
        self.assertTrue(TestLexer.test(
            r"""
procedure foo();
begin
    a := a[d < y(5 > 3) + 3 * n(12)] := 5[3] := 3[2] := b;
end
""",

            r"procedure,foo,(,),;,begin,a,:,=,a,[,d,<,y,(,5,>,3,),+,3,*,n,(,12,),],:,=,5,[,3,],:,=,3,[,2,],:,=,b,;,end,<EOF>",
            150
        ))

    def test_bool(self):
        """test String again"""
        self.assertTrue(TestLexer.test("true"
        , "true,<EOF>", 151))

    def test_arr(self):
        """test String again"""
        self.assertTrue(TestLexer.test("""{"he ee loo"  , true  , false}"""
        , """{"he ee loo"  , true  , false},<EOF>""", 152))

    
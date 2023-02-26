import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_arraytype(self):
        """Simple program: int main() {} """
        input = """array [2, 3] of integer"""
        expect = "Error on line 1 col 0: array"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_vardecl(self):
        """variable declaration  """
        input = """delta: integer;
                    anpha, beta, gama, delta: boolean;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_vardecl2(self):
        """variable declaration  """
        input = """x: integer = 65;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_vardecl3(self):
        """variable declaration  """
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_vardecl4(self):
        """variable declaration  """
        input = """a, b, c, d: integer = 3, 4, 6, 5;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_last_submisstion(self):
        """variable declaration  """
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_var_decl(self):
        """variable declaration  """
        input = """aalo: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_var_decl2(self):
        """variable declaration  """
        input = """aalo, balo: integer = 3, 4;
        aalo: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_var_decl3(self):
        """variable declaration  """
        input = """str, boo: integer = "helo", true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    
    def test_var_decl4(self):
        """variable declaration  """
        input = """str, boo: boolean = "helo", true;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
   
    def test_var_decl5(self):
        """variable declaration  """
        input = """str, boo: string = "helo", true;
        str, boo: boolean = "helo", false;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_var_decl6(self):
        """variable declaration  """
        input = """phong493 : integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_var_decl7(self):
        """variable declaration  """
        input = """phong493 : float = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_function_decl(self):
        """function declaration  """
        input = """inc: function void(out n: integer, delta: integer) {
            n = n + delta;
            return n;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_function_decl2(self):
        """function declaration  """
        input = """inasdfalse: function void(out n: integer, delta: integer) {
            n = n + delta;
            return n;
        }
        main: function void() {        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    
    # this test case should be failed
    def test_function_decl3(self):
        """main function declaration  """
        input = """
        main: function void() {        }
        main: function void() {        }"""
        expect = "Error on line 3 col 8: main"
        self.assertTrue(TestParser.test(input, expect, 217))

    # this test case should be success
    def test_function_decl4(self):
        """function declaration  """
        input = """
        one: function integer() {
            return 1;
                }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_function_decl5(self):
        """function declaration  """
        input = """
        number: function integer(out n: integer) {
            return n;
                }
        main: function void() {        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_function_decl6(self):
        """function declaration  """
        input = """
number: function stringb(out n: integer) {
return n;
}
main: function void() {        }
        """
        expect = "Error on line 2 col 17: stringb"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_function_decl7(self):
        """function declaration  """
        input = """main: function void() {
functioninmain: function void() {retrun null;}
        }
        """
        expect = "Error on line 2 col 16: function"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_vardecl8(self):
        """variable declaration  """
        input = """main:function void(){
a = a c;
        }"""
        expect = "Error on line 2 col 6: c"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_vardecl9(self):
        """variable declaration  """
        input = """main:function void(){
a = a c[1,2];
        }"""
        expect = "Error on line 2 col 6: c"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_vardecl10(self):
        """variable declaration  """
        input = """tenfunction:function void(){
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_vardecl11(self):
        """variable declaration  """
        input = """as:function float(){

           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_vardecl12(self):
        """variable declaration  """
        input = """as:function float(){
            a = a + 1;
            b = b + 1;
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_indexop(self):
        """index operator  """
        input = """main:function void(){
            a = a[1,2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_indexop2(self):
        """index operator  """
        input = """main:function void(){
        i: integer;
            a = a[1,2,i];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_indexop3(self):
        """index operator  """
        input = """tenfuc: function integer(){
        return 10 + 9 - 9 * 3;
}
main:function void(){
        i: integer;
            a = a[1,2,i,tenfuc];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_state(self):
        """index operator  """
        input = """i=1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_state2(self):
        """index operator  """
        input = """i=1;
        i = i < 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_state3(self):
        """index operator  """
        input = """i=1 + i + a;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_for(self):
        """for statement  """
        input = """for (i = 1, i < 10, i + 1) {
writeInt(i);
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_expr(self):
        """for statement  """
        input = """1+2+3-4/5*2.6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test_expr1(self):
        """for statement  """
        input = """1+true+ "stringnest";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test_expr2(self):
        """for statement  """
        input = """a = -2 + 2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
    # error integer or =
    def test_expr3(self):
        """for statement  """
        input = """a = int % 2;
        int = int / 2;
        integer = integer + 1;
        """
        expect = "Error on line 3 col 8: integer"
        self.assertTrue(TestParser.test(input, expect, 237))

    # ask the other
    def test_expr4(self):
        """for statement  """
        input = """integer : integer;
        """
        expect = "Error on line 1 col 0: integer"
        self.assertTrue(TestParser.test(input, expect, 238))
    
    def test_expr5(self):
        """for statement  """
        input = """
        boll : boolean = true;
        bool = false && bool; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_expr6(self):
        """for statement  """
        input = """
        boll : boolean = true;
        bool = !boll && boll; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_expr7(self):
        """for statement  """
        input = r"""
        strin : string = "some kind of string \n ";
        strin2 : string = "some kind of string2 \n ";
        strin3 : string = strin :: strin2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_expr8(self):
        """for statement  """
        input = r"""
        bool : boolean = true == a;
        bool : boolean = true != a;
        bool : boolean = true > a;
        bool : boolean = false < a;
        bool : boolean = true >= a;
        bool : boolean = true <= a;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_expr9(self):
        """for statement  """
        input = r"""
        a[1,2] = b;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    
    def test_expr10(self):
        """for statement  """
        input = r"""
        a[1,2] = b[3,4] + aloho(a[i]);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test_expr11(self):
        """for statement  """
        input = r"""
        inherit out iden: integer;
        """
        expect = "Error on line 2 col 8: inherit"
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_funcinit(self):
        """for statement  """
        input = r"""
        name____as: function integer(){}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        
    def test_funiinit2(self):
        """for statement  """
        input = r"""
        name____as: function integer(){}
        name____ass: function integer() inherit name____as{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
    
    def test_blockstmt(self):
        """for statement  """
        input = r"""
        {
            a = 1;
            b = 2;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_blockstmt2(self):
        """for statement  """
        input = r"""
        {
            a = 1;
            b = 2;
            {
                a = 1;
                b = 2;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_blockstmt3(self):
        """for statement  """
        input = r"""
        {
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_blockstmt4(self):
        """for statement  """
        input = r"""
        {
r, s: integer;
r = 2.0;
a, b: array [5] of integer;
s = r * r * myPI;
a[0] = s;
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_blockstmt5(self):
        """for statement  """
        input = r"""
        {
            a : void;
        }
        """
        expect = "Error on line 3 col 16: void"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_blockstmt6(self):
        """for statement  """
        input = r"""
        {
            a, b: array [5] of auto;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    # what is result of this
    def test_blockstmt7(self):
        """for statement  """
        input = r"""
            string;
            array;
        """
        expect = "Error on line 2 col 12: string"
        self.assertTrue(TestParser.test(input, expect, 254))
    
    def test_ifstmt(self):
        """for statement  """
        input = r"""
        if(a>b) a= b + dunf();
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_ifstmt2(self):
        """for statement  """
        input = r"""
        if(a>b) a= b + dunf();
        else a = dunf() ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_ifstmt3(self):
        """for statement  """
        input = r"""
        if(a>b) if(a>b) a= b + dunf();
        else a = dunf() ;
        else if (a<b) a = dunf() ;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))
    
    def test_ifstmt4(self):
        """for statement  """
        input = r"""
        if(a>b) if(a>c) a= b + dunf(a[2.34442,4_3]);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_ifstmt5(self):
        """for statement  """
        input = r"""
        if(a>b) 
            fund: function float(){
                a = 1;
                break;
            }
        ;
        """
        expect = "Error on line 3 col 16: :"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_ifstmt6(self):
        """for statement  """
        input = r"""
        if(a[2,i]>a[b[2,5_6]]) 
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
                if(a[i] == 0) return 0;
            }
        else a = 2;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def testforstmt(self):
        """for statement  """
        input = r"""
        for (i = a, i < 10, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def testforstmt2(self):
        """for statement  """
        input = r"""
        for (i = a, 1+ 1, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "Error on line 2 col 21: +"
        self.assertTrue(TestParser.test(input, expect, 262))

    def testforstmt3(self):
        """for statement  """
        input = r"""
        for (i = a, 1+ 1 + true, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "Error on line 2 col 21: +"
        self.assertTrue(TestParser.test(input, expect, 263))

    def testforstmt4(self):
        """for statement  """
        input = r"""
        for (i = a, i <= 10.0, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
    
    def testforstmt5(self):
        """for statement  """
        input = r"""
        for (i = a, true, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def testforstmt6(self):
        """for statement  """
        input = r"""
        for (i = a, true, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def testforstmt7(self):
        """for statement  """
        input = r"""
        for (i = a, true, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def testforstmt8(self):
        """for statement  """
        input = r"""
        for (i = a, 1 == 2, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def testforstmt9(self):
        """for statement  """
        input = r"""
        as: boolean = false;
        for (i = a, (!as) == true, i * b[2,5]) {
            varii = writeInt(i);
            if(a[i,as] == 0) break;
            else continue;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def testforstmt10(self):
        """for statement  """
        input = r"""
        for (i = a, i < 10, i * b[2,5]) {
            varii = writeInt(i) - true;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))

    def testwhilestmt(self):
        """while statement  """
        input = r"""
        while (i < 10) 
            writeInt(i);
if(a[i] == 0) break;
else continue;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def testwhilestmt2(self):
        """while statement  """
        input = r"""
        while (i < 10) ;"""
        expect = "Error on line 2 col 23: ;"
        self.assertTrue(TestParser.test(input, expect, 272))

    def testwhilestmt3(self):
        """while statement  """
        input = r"""
        while (i < 10) 
            while (i < 20) return 20; 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def testwhilestmt4(self):
        """while statement  """
        input = r"""
        do {
            writeInt(i);
            break;
        } while (true);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def testwhilestmt5(self):
        """while statement  """
        input = r"""
        while (i < 10) 
    var = 2 + i;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def testwhilestmt6(self):
        """while statement  """
        input = r"""
        while (i < 10)
        var;
        """
        expect = "Error on line 3 col 11: ;"
        self.assertTrue(TestParser.test(input, expect, 276))

    def testwhilestmt7(self):
        """while statement  """
        input = r"""
        do {
        }
        while (i < 10);
        var = 2 + i;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))


    # should have ; after while
    def testwhilestmt8(self):
        """while statement  """
        input = r"""
        do {
                var = 2 + i;
            {
                var = 2 + i;
            }
            return 2;
        }
        while (i < 10)
        var = 2 + i;
        """
        expect = "Error on line 10 col 8: var"
        self.assertTrue(TestParser.test(input, expect, 278))

    def testwhilestmt9(self):
        """while statement  """
        input = r"""
        while(i<2) do {
        asda = 2;
        } while (i < 10);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def testwhilestmt10(self):
        """while statement  """
        input = r"""
        while(i<2) do {
        asda = 2;
        break;
        continue;
        return adas();
        } while (i < 10);
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def testcallst(self):
        """do while statement  """
        input = r""" call1(x); """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def testcallst2(self):
        """do while statement  """
        input = r"""
        
        main: function void() {
            test: array [5] of float;
            test[1] = 0;
            test[2] = 1_23.0;
            test[3] = 2.23e3;
            test[4] = 332_23e23;
            test[5] = 4.5;
        }
           """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def testcall3(self):
        """do while statement  """
        input = r"""
        main: function void() {
            test: array [5] of float;
            test[1] = 0;
            test[2] = 1_23.0;
            test[3] = 2.23e3;
            test[4] = 332_23e23;
            test[5] = 4.5;

            sortitem(test);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def testcallst4(self):
        """do while statement  """
        input = r"""
        sortitem: function void(arr: array [5] of float) 
        {
            for (i = 0, i < 5, i + 1) {
                for (j = i + 1, j < 5, j + 1) {
                    if (arr[i] > arr[j]) {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }

        }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def testcallst5(self):
        """do while statement  """
        input = r"""
        sortitem: function void(arr: array [5] of float) 
        {
            for (i = 0, i < 5, i + 1) {
                for (j = i + 1, j < 5, j + 1) {
                    if (arr[i] > arr[j]) {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }

            result: array [5] of float = {0, 1_23.0, 2.23e3, 332_23e23, 4.5}; 
            return result;
        }

        main: function void() {
            test: array [5] of float;
            test[1] = 0;
            test[2] = 1_23.0;
            test[3] = 2.23e3;
            test[4] = 332_23e23;
            test[5] = 4.5;

            sortitem(test);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def testcallst6(self):
        """do while statement  """
        input = r"""
        sorttwoarray: function void(arr: array [5] of float, arr2: array [5] of float)) 
        {
            for (i = 0, i < 5, i + 1) {
                for (j = i + 1, j < 5, j + 1) {
                    if (arr[i] > arr[j]) {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }

            result: array [5] of float = {0, 1_23.0, 2.23e3, 332_23e23, 4.5}; 
            return result;
        }

        main: function void() {
            test: array [5] of float;
            test[1] = 0;
            test[2] = 1_23.0;
            test[3] = 2.23e3;
            test[4] = 332_23e23;
            test[5] = 4.5;

            test2: array [5] of boolean;
            test2[1] = true;
            test2[2] = false;
            test2[3] = true;
            test2[4] = false;
            test2[5] = true;

            sorttwoarray(test, test2, 5, 6);
        }
        """
        expect = "Error on line 2 col 86: )"
        self.assertTrue(TestParser.test(input, expect, 286))

    def testcallst7(self):
        """do while statement  """
        input = r"""

        capitalizestring: function void(str: string) {
            for (i = 0, i < length(str), i + 1) {
                if ((str[i] >= "a") && (str[i] <= "z")) {
                    str[i] = str[i] - 32;
                    
                }
            }
            return capitalizestring(null);
        }

        main: function void() {
            test: array [5] of float;
            test[1] = 0;
            test[2] = 1_23.0;
            test[3] = 2.23e3;
            test[4] = 332_23e23;
            test[5] = 4.5;

            test2: array [5] of boolean;
            test2[1] = true;
            test2[2] = false;
            test2[3] = true;
            test2[4] = false;
            test2[5] = true;

            sorttwoarray(test, test2);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def testcallst8(self):
        """do while statement  """
        input = r"""

        functio2time: function void(str: string) {}

        main: function void() {
            a: string = "hello world!";
            b: string = "phong";
            c: string = a :: c;

        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def testcallst9(self):
        """do while statement  """
        input = r"""

        functio2time: function void(str: string) {}

        main: function void() {
            a: string = "hello world!";
            b: string = "phong";
            c: string = a :: c;

            functio2time(functio2time(c));
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
    
    def testcal(self):
        """do while statement  """
        input = r"""
        main: function void() {
            a: integer = 12;
            b: float = 24.345e24;
            result: integer = 0;

            result = a + ((b * 2 - 4) + b / 2) / 2;
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_simple_program1(self):
        input = """ asdasd_sdasda: auto = return helloworld();"""
        expect = "Error on line 1 col 23: return"
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test_simple_program2(self):
        input = """ asadsqeDADSADAdasda: auto = main: function void() {};"""
        expect = "Error on line 1 col 29: main"
        self.assertTrue(TestParser.test(input, expect, 292))
    
    def test_simple_program3(self):
        input = """ func1: function void() inherit a{}
                    func2: function string(inherit out a: integer, inherit out b: float){}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_simple_program4(self):
        input = """func1: function auto(inherit out ASD_ad: float) inherit asd_as {
                        if (asdas == ADsa) {
                            for (i = 1, true + false + true, true) {
                                asdas = a + 1 + 100_00 + 123.123e-123;
                                if (e == asdasd) break;
                            }
                        }
                        else do {
                            aasdas = SDA :: ASdsas + asdas - asdsw2 * qwe;
                            return func2(assd);
                            continue
                        } while (A > (B <= C));
                    }
                """
        expect = "Error on line 3 col 45: +"    
        self.assertTrue(TestParser.test(input, expect, 294))    
    
    def test_simple_program5(self):
        input = """func1_213.2: function array()
                    {
                        vassse_weAs: array [1,1,0,0] of string = {{{{}}}};
                    }
                """
        expect = "Error on line 1 col 9: ."    
        self.assertTrue(TestParser.test(input, expect, 295)) 

    def test_simple_program6(self):
        input = """func14_2132: function array(inherit out asdd: float)
                    {
                        vassse_weAs: array [1,1,0,0] of string = {{{{}}};
                    }
                """
        expect = "Error on line 3 col 65: {"    
        self.assertTrue(TestParser.test(input, expect, 296))    

    def test_simple_program7(self):
        input =  """func1: function string (inherit str1: string, out a: boolean)
                    {
                        if((a == 123) && (str1 != "hello") ) return func1("hello", a);
                        else {
                            if(a :: "b" == 3 || !(r + 2 * 3)){} 
                            else readIndteger(a); 
                        }
                    }
                """
        expect = "Error on line 5 col 40: =="    
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_simple_program8(self):
        input = """DSA_Ss123 : integer = 1_000_123 + 12 + arr[12.23];
                SADasaJJ: function void(inherit out a: auto) inherit sdads_ABC {}
                """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_simple_program9(self):
        input = """SAD_JJJJ: function void(inherit out a: auto) inherit sdads_ABC {
                    for (a = arr[2] + true, 1_0021 + 120.0e-10, arr[0,0,1] :: "\\"hello\\"")
                    {
                        return preventDefault() :: 100_00 :: "HEHI";
                    }
                }
                """
        expect = "Error on line 2 col 51: +"    
        self.assertTrue(TestParser.test(input, expect, 299))
    
    def test_simple_program10(self):
        input = """SAD_JJasJJ: function void(inherit out a: auto) inherit sdads_ABC {
                    for (a = arr[2] + true, true, arr[0,0,1] :: "\\"hello\\"")
                    {
                        return prevendtDefault() :: (100_00 :: "HEHI");
                        break;
                    }
                }
                """
        expect = "successful"    
        self.assertTrue(TestParser.test(input, expect, 300))
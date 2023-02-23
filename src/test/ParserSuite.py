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
        expect = "successful"
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


   

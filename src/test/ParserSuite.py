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

    def last_submisstion_test(self):
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
        self.assertTrue(TestParser.test(input, expect, 204))

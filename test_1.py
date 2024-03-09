import unittest

from main import calc

class TestCalc(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(3, calc("+", 1,2))
        self.assertEqual(1, calc("+", -1,2))
        self.assertEqual(-11, calc("+", -5,-6))
        self.assertEqual(10, calc("+", 0,10))
    def test_minus(self):
        self.assertEqual(-1, calc("-", 1,2))
        self.assertEqual(-3, calc("-", -1,2))
        self.assertEqual(1, calc("-", -5,-6))
        self.assertEqual(10, calc("-", 10,0))
    def test_multiplication(self):
        self.assertEqual(2, calc("*", 1,2))
        self.assertEqual(-2, calc("*", -1,2))
        self.assertEqual(30, calc("*", -5,-6))
        self.assertEqual(0, calc("*", 10,0))
    def test_division(self):
        self.assertEqual(0.5, calc("/", 1,2))
        self.assertEqual(-0.5, calc("/", -1,2))
        self.assertEqual(0.5, calc("/", -5,-10))
        self.assertEqual(ZeroDivisionError, calc("/", 10,0))

if __name__ == '__main__':
    unittest.main()

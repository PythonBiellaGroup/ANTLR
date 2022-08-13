import unittest
from calculator import calculator

class TestSum(unittest.TestCase):
    def test_simple_sum(self):
        self.assertEqual(5,calculator('2+3'))

    def test_mult_sum(self):
        self.assertEqual(9,calculator('2+3+2+2'))

class TestSub(unittest.TestCase):
    def test_simple_sub(self):
        self.assertEqual(3,calculator('6-3'))

    def test_mult_sub(self):
        self.assertEqual(90,calculator('100-2-4-4'))


class TestDiv(unittest.TestCase):
    def test_simple_div(self):
        self.assertEqual(2,calculator('6/3'))

    def test_float_div(self):
        self.assertEqual(2.5,calculator('5/2'))

    def test_div_zero(self):
        self.assertEqual(0,calculator('100/0'))


class TestExpr(unittest.TestCase):
    def test_simple_expr(self):
        self.assertEqual(10,calculator('(12+(6-3))*2/3'))


if __name__ == '__main__':
    unittest.main()   
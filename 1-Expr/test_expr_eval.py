import unittest
from expr_eval import evaluator

class TestSum(unittest.TestCase):
    def test_simple_sum(self):
        self.assertEqual(5,evaluator('2+3'))

    def test_mult_sum(self):
        self.assertEqual(9,evaluator('2+3+2+2'))

    def test_mult2_sum(self):
        self.assertEqual(1353,evaluator('2+3+2+2+1222+0+122'))

if __name__ == '__main__':
    unittest.main()   
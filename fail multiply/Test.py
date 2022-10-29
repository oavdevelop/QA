import unittest
from Calc import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(5,6),11)
    def test_sub(self):
        self.assertEqual(self.calculator.subtruct(8,6),2)
    def test_mul(self):
        self.assertEqual(self.calculator.multipy(0,0),10)
    def test_mul(self):
        self.assertEqual(self.calculator.multipy(5,5),25)
    def test_div(self):
        self.assertEqual(self.calculator.divide(6, 3),2)
    def test_sum(self):
        self.assertEqual(self.calculator.sum(6, 3, ' яблок'), '9 яблок')
if __name__ == '__main__':
    unittest.main()

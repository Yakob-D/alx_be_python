import unittest
from simple_calculator.py import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 4), 7)
        self.assertEqual(self.calc.add(-3, 4), 1)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(-3,-4), 1)
        self.assertEqual(self.calc.subtract(-3,4), 7)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(1, 9), 9)
        self.assertEqual(self.calc.multiply(-2, 10), -20)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(2,0), None)
        self.assertEqual(self.calc.divide(0, 10), 0)
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertEqual(self.calc.divide(22, 2), 11)
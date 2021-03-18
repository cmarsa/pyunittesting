# test/unit/test_calculate.py
import unittest
from calculator.calculate import Calculate

class TestCalculate(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        the addition of the setUp method means you only 
        need to create the instance of Calculate once for it to
        be available to all test cases. 
        """
        self.calc = Calculate()
    
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
    
    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, 'Hello', 'World')
    
    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.subtract(8, 4))
    
    def test_subtract_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.subtract, 'Hello', 'World')
    
    def test_divide_method_raises_zero_division_error(self):
        self.assertRaises(AssertionError, self.calc.divide, 5, 0)
    
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(5/6, self.calc.divide(5, 6))
    
    def test_divide_method_raises_typeerrpr_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.divide, 'Hello', 'World')
    
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
    
    def test_multiply_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.multiply, 'Hello', 'World')
    
    def test_assert_int_params(self):
        self.assertTrue(self.calc._assert_int_params(2, 3))
        self.assertFalse(self.calc._assert_int_params(3, 'm'))


if __name__ == '__main__':
    unittest.main()
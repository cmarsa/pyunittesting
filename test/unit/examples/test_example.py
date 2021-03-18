# test/unit/test_example.py
import unittest

class TestExample(unittest.TestCase):
    """
    """
    def test_assert_equal(self):
        """
        This method checks to see whether argument x equals argument y.
        Under the covers, this method is performing the check using
        the == definition for the objects.
        """
        self.assertEqual(1, 1)

    def test_assert_almost_equal_delta_0_5(self):
        """
        On first glance, this method may seem a little strange but
        in context becomes useful. The method is basically useful
        around testing calculations when you want a result
        to be within a certain amount of places to the expected,
        or within a certain delta.
        """
        self.assertAlmostEqual(1, 1.2, delta=0.5)
    
    def test_assert_almost_equal_places(self):
        self.assertAlmostEqual(1, 1.000_01, places=4)
    
    def test_assert_raises_value_error(self):
        """
        Given a method and set of arguments to that method,
        does it raise the exception?
        Arguments must match the signature of the method or
        syntax error is raised.
        """
        self.assertRaises(ValueError, int, 'a')
    
    def test_assert_raises_type_error(self):
        self.assertRaises(TypeError, int, float)
    
    def test_assert_raises_index_error(self):
        self.assertRaises(IndexError, [].pop)
        with self.assertRaises(IndexError):
            [1, 2, 3][8]
    
    def test_assert_raises_alternative(self):
        with self.assertRaises(AttributeError):
            [].get
    
    def test_assert_dict_contains_subset(self):
        """
        Use this method to check whether actual contains expected.
        It’s useful for checking that part of a dictionary is present
        in the result, when you are expecting other things to be there also.
        For example, a large dictionary may be returned and you need
        to test that only a couple of entries are present.

        NOTE: This method/assertion is deprecated, better use:
            self.assertGreaterEqual
        """
        expected = {
            'a': 'b'
        }
        actual = {
            'a': 'b',
            'c': 'd',
            'e': 'f'
        }
        # self.assertDictContainsSubset(expected, actual)  # deprecated
        # better use
        self.assertGreaterEqual(actual.items(), expected.items())

    def test_assert_dict_equal(self):
        """
        This method asserts that two dictionaries contain exactly the
        same key value pairs. For this  test to pass, the two dictionaries
        must be exactly the same, but not necessarily in the same order.
        """
        expected = {
            'a': 'b',
            'c': 'd'
        }
        actual = {
            'c': 'd',
            'a': 'b'
        }
        self.assertDictEqual(expected, actual)
    
    def test_assert_true(self):
        """
        Use this method to check the truth value of an expression 
        or result. This method can be useful and has a few interesting
        caveats. This is because Python’s implicit truth behavior, 
        such as numeric values like 0 and 1 have truth-value of
        False and True, respectively. 
        """
        self.assertTrue(1)
        self.assertTrue('Hello World')
        self.assertTrue(4 == 4)
    
    def test_assert_false(self):
        """
        This method is the inverse of assertTrue and is used
        for checking whether the expression 
        or result under the test is False.
        """
        self.assertFalse(0)
        self.assertFalse(None)
        self.assertFalse('')
        self.assertFalse(5 > 10)
    
    def test_assert_greater(self):
        """
        This method allows you to check whether one value
        is greater than the other. It is essentially a helper method
        that wraps up the use of assertTrue on the expression a > b.
        It displays a helpful message by default when the
        value is not greater.
        """
        self.assertGreater(2, 1)
    

    def test_assert_greater_equal(self):
        """
        You use this method to check whether one value is
        greater than or equal to another value. Essentially, this
        wrapper is asserting True on a >= b.
        """
        self.assertGreaterEqual(2, 2)
        self.assertGreaterEqual(2, 1)
    

    def test_assert_in(self):
        """
        With this method, you can check whether a value is
        in a container (hashable) such as a list or tuple.
        This method is useful when you don’t care what the
        other values are, you just wish to check that a certain
        value(s) is in the container.
        """
        self.assertIn(1, [1, 2, 3, 4, 5])
        self.assertIn(2, (2, 3, 4, 5, 9))
    
    def test_assert_is(self):
        """
        Use this method to check that expr1 and expr2 are identical.
        That is to say they are the same object. For example,
        the python code [] is [] would return False, as the creation 
        of each list is a separate object.
        """
        self.assertIs('a', 'a')
        self.assertIs(4, 4)
    
    def test_is_instance(self):
        """
        This method asserts that an object is an instance
        of a specified class. This is useful for checking
        that the return type of your method is as expected
        (for instance, if you wish to check that a value is
        a type of int)
        """
        self.assertIsInstance(1, int)
    

    def test_not_is_instance(self):
        """
        This reverse of assertIsInstance provides an
        easy way to assert that the object is not a type
        of the class.
        """
        self.assertNotIsInstance(1, str)
    
    def test_assert_is_none(self):
        """
        Use this to easily check if a value is None.
        This method provides a useful standard message if not None
        """
        self.assertIsNone(None)

    def test_assert_is_not(self):
        """
        Using this method, you can check that expr1
        is not the same as expr2. This is to say that 
        expr1 is not the same object as expr2.
        """
        self.assertIsNot([], [])
    
    def test_assert_is_not_none(self):
        """
        This method checks that the value provided is not None.
        This is useful for checking that your 
        method returns an actual value, rather than nothing.
        """
        self.assertIsNotNone(1)
    
    def test_assert_less(self):
        """
        This method checks that the value a is less than the value b.
        This is a wrapper method for assertTrue on a < b.
        """
        self.assertLess(1, 2)
    
    def test_assert_less_equal(self):
        """
        This method checks that the value a is less than
        or equal to the value b. This is a wrapper method
        for assertTrue on a <= b
        """
        self.assertLessEqual(2, 2)
    
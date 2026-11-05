import unittest
from task1 import define_largest_number

class TestDefineLargestNumberFunction(unittest.TestCase):

    def test_with_valid_ints(self):
        number_1 = 5
        number_2 = 6
        expected = 6
        result = define_largest_number(number_1, number_2)
        self.assertEqual(result, expected)

    def test_with_valid_floats(self):
            number_1 = 5.5
            number_2 = 1.2
            expected = 5.5
            result = define_largest_number(number_1, number_2)
            self.assertEqual(result, expected)

    def test_with_invalid_value_value_error_expected(self):
            number_1 = "a"
            number_2 = 6
            with self.assertRaises(ValueError):
                define_largest_number(number_1, number_2)
    
    def test_with_invalid_second_value_value_error_expected(self):
                number_1 = 1
                number_2 = "1.2.2"
                with self.assertRaises(ValueError):
                    define_largest_number(number_1, number_2)
            
if __name__ == '__main__':
    unittest.main()

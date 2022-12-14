"""
Test file should be named like this. Starting with test then _ then a descriptive name.

Import the module (this is included with python)
"""

"""
Class is the name of test - but it needs to inherit from 'TestCase'

unittest.main() - means you can run the test without specifying the 'unittest' module
"""

import unittest

"""imports the function from the evans.py

the method (if statement) must be named 'test_xxx' otherwise it wont run the test

self - as we are within a class """


from evans import even_number_of_evans


class TestEvans(unittest.TestCase):

    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evans, 3)
    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evans([]), False)
        self.assertEqual(even_number_of_evans([2, 4]), True)
        self.assertEqual(even_number_of_evans([2]), False)
        self.assertEqual(even_number_of_evans([1, 3, 5]), False)
        

if __name__ == '__main__':
    unittest.main()

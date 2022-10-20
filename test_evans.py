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

    def test_function_returns_True(self):
        self.assertTrue(even_number_of_evans([]))

if __name__ == '__main__':
    unittest.main()

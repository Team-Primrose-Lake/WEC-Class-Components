import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self):#WARNING FOR THE TEST CLASS, FUNCTIONS MUST START WITH test_. Otherwise, it will not be recognized as a test function.

        #we have a lot of assert methods with unittest.
        #assertEqual, assertNotEqual, assertTrue, assertFalse, assertRaises

        self.assertEqual(calc.add(10,5), 14)#testing function if output is 14
        self.assertEqual(calc.add(-1,1), 0)#testing edge cases.
        self.assertEqual(calc.add(-1,-1), -2)


    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 14)#testing function if output is 14
        self.assertEqual(calc.subtract(-1,1), 0)#testing edge cases.
        self.assertEqual(calc.subtract(-1,-1), -2)


    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)#testing function if output is 14
        self.assertEqual(calc.multiply(-1,1), -1)#testing edge cases.
        self.assertEqual(calc.multiply(-1,-1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)#testing function if output is 14
        self.assertEqual(calc.divide(-1,1), -1)#testing edge cases.
        self.assertEqual(calc.divide(-1,-1), 1)

        self.assertRaises(ValueError,calc.divide,10,0)#expects error. 10, and 0 are the parameters with an expected error



if __name__ == '__main__':
    unittest.main()
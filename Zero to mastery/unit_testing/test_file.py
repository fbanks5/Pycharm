import unittest
import unit_test

class FileTest(unittest.TestCase):
    def setUp(self):
        print('testing a function')

    def test_do_something(self):
        test_param = 10
        result = unit_test.do_something(test_param)
        self.assertEqual(result, 15)

    def test_do_something2(self):
        test_param = 'test string'
        result = unit_test.do_something(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_something3(self):
        test_param = None
        result = unit_test.do_something(test_param)
        self.assertEqual(result, 'Please enter a number')

    def test_do_something4(self):
        test_param = ''
        result = unit_test.do_something(test_param)
        self.assertEqual(result, 'Please enter a number')

    def tearDown(self):
        print('Cleaning up')


if __name__ == '__main__':
    unittest.main()


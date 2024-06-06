import unittest
import randomgame



class Test_randomgame(unittest.TestCase):
    def test_input(self):
          result = randomgame.run_guess(5, 5)
          self.assertTrue(result)

    def wrong_guess(self):
        result = randomgame.run_guess(5, 0)
        self.assertFalse(result)


    def wrong_numbers(self):
        result = randomgame.run_guess(5, 1)

    def wrong_symbols(self):
        result = randomgame.run_guess(5, '2')

if __name__ == '__main__':
    unittest.main()

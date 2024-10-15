import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_for_integer(self):
        res = calc.divide(12, 3)
        self.assertEqual(res, 4)

    def test_for_string(self):
        with self.assertRaises(TypeError):
            calc.divide(12, "4")

    def test_my_error(self):
        with self.assertRaises(calc.MyError):
            calc.divide(12, 0)


if __name__ == "__main__":
    unittest.main()


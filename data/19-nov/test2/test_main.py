import unittest
import ex_main as main

class TestMain(unittest.TestCase):

    def test_ex1(self):

        self.assertEqual(main.ex1("apology"), "apolXYZogy")
        self.assertEqual(main.ex1("I-dont-know"), "I-dontXYZ-know" )
        self.assertEqual(main.ex1("whatever", subs='so'), "whatsoever")
    
    def test_ex2(self):
        l = [{'a': 4, 'f': 0, 'c': 1}, {'d': 4, 'b': 5}]
        expected = 4154
        self.assertEqual(main.ex2(l), expected)

    def test_ex3(self):
        self.assertEqual(main.ex3([1, 3, 5]), 1)
        self.assertEqual(main.ex3([4, 6, 8]), 3)
        self.assertEqual(main.ex3([1, 2, 4]), 2)
        self.assertEqual(main.ex3([5, 7, 13, 17, 19]), 0)
    
    def test_ex4(self):
        l = ['Monday 24-10-2022 NO CLASS', 'Tuesday 25-10-2022 CLASS', 'Wednesday 26-10-2022 NO CLASS']
        self.assertListEqual(main.ex4(l), ['24-10', '25-10', '26-10'])
        l = ['a  21-10 a', 'b 22-08 b']
        self.assertListEqual(main.ex4(l), ['21-10', '22-08'])


if __name__ == "__main__":
    unittest.main()

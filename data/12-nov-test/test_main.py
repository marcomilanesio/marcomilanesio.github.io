import unittest
import ex_main as main

class TestMain(unittest.TestCase):

    def test_ex1(self):
        self.assertEqual(len(main.ex1("a-simple-text")), 3)
        self.assertEqual(len(main.ex1("asimpletext")), 1)
        self.assertEqual(len(main.ex1("hi+me", '+')), 2)
        self.assertEqual(len(main.ex1("abc", 'b')), 2)
    
    def test_ex2(self):
        l = [{'a': 4, 'f': 0, 'c': 1}, {'d': 4, 'b': 5}]
        expected = 45140
        self.assertEqual(main.ex2(l), expected)

    def test_ex3(self):
        l = [5, 2, 3, 4]
        expected = [4, 3, 2, 5] 
        self.assertListEqual(main.ex3(l), expected)
        self.assertListEqual(main.ex3([]), [])
    
    def test_ex4(self):
        l = ['Monday 24-10-2022 NO CLASS', 'Tuesday 25-10-2022 CLASS', 'Wednesday 26-10-2022 NO CLASS']
        self.assertListEqual(main.ex4(l), ['24-10', '25-10', '26-10'])
        l = ['a  21-10 a', 'b 22-08 b']
        self.assertListEqual(main.ex4(l), ['21-10', '22-08'])

    def test_ex5(self):
        l = ['Monday 24-10-2022 NO CLASS', 'Tuesday 25-10-2022 CLASS', 'Wednesday 26-10-2022 NO CLASS']
        self.assertListEqual(main.ex5(l), [False, True, False])
        l = ['YES', 'YES', 'YES', 'YES']
        self.assertTrue(all(main.ex5(l)))

    def test_ex6(self):
        self.assertEqual(main.ex6(123451), (1, 2))
        self.assertEqual(main.ex6(2233), (2, 2))
        self.assertEqual(main.ex6(1), (1, 1))

    def test_ex7(self):
        self.assertEqual(main.ex7(a=1, b=2.5, c=[]), 1)
        self.assertEqual(main.ex7(a=1, b=2.5), 0)
    
    def test_ex8(self):
        self.assertEqual(main.ex8('my test, my score, my day', 'my'), 9)
        self.assertEqual(main.ex8('another one bites the dust', 'the'), 18)
        self.assertEqual(main.ex8('asdfbasdfbrte', 'f'), 8)
        

if __name__ == "__main__":
    unittest.main()

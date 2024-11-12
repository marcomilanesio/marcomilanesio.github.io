# place additional imports here if needed
import re
from collections import Counter
import csv

def ex1(text, char='-'):
    """
    Given a text of arbitrary length, divide the text on the character given and return the resulting list.
    E.g., ex1('hi-me') = ['hi', 'me']; ex1('hi-me', char='+') = ['hi-me']; ex1('abc', char='b') = ['a', 'c']
    @param text: string
    @return list
    """
    result = []
    result = text.split(char)
    return result


def ex2(arr):
    """
    Given a list of dictionaries with unique string keys and integer values, 
    navigate the keys in alphabetical order and return the integer resulting in the concatenation of the values.

    E.g., ex2([{'a': 4, 'd': 9}, {'e': 6, 'b': 12}]) = 41296;
          ex2([{'c': 1, 'a': 3}, {'b': 2}] = 321
    @param arr: list
    @return int
    """
    result = -1
    tmp = {}
    for dic in arr:
        tmp.update(dic)
    
    number = ""
    for k, v in sorted(tmp.items()):
        number += str(v)

    return int(number)


def ex3(arr):
    """
    Using a `for` loop reverse the list of digits passed as argument.
    E.g., ex3([4, 3, 2, 5]) = [5, 2, 3, 4]; ex3([]) = []
    @param arr: list
    @return list
    """
    result = []
    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])
    return result

def ex4(arr):
    """
    Fill up so that the tests in test_exercises.py pass.
    @param arr: list
    @return list 
    """
    return list(map(lambda x: re.search('\d{2}-\d{2}', x).group(), arr))


def ex5(arr):
    """
    Fill up so that the tests in test_exercises.py pass.
    @param arr: list
    @return list 
    """
    tmp = list(map(lambda x: re.search('NO', x), arr))
    result = [False if x else True for x in tmp]
    return result

def ex6(number):
    """Find the most frequent digit in a given number, and return the number with its occurrence.
       E.g., ex6(123451) = (1, 2); ex6(2244) = (2, 2); ex6(1) = (1, 1)
       @param number: int
       @return tuple(int, int)
    """
    x = [int(d) for d in str(number)]
    c = Counter(x)
    return c.most_common(1)[0]

def ex7(**kwargs):
    """
    Returns the number of non-numerical values passed in the parameters.
    E.g., ex7(a=1, b=2.5, c=[]) = 1; ex7(a={}, b='') = 2
    @param variable keywords
    @return int

    - HINT: you may need some exception handling...
    """
    c = 0
    for k, v in kwargs.items():
        try:
            tmp = float(v)
        except:
            c += 1
    return c


def ex8(text, pattern):
    """
    Look for `pattern` in text. Return the index of the second occurrence of pattern in text.
    E.g., ex9('my test, my score, my day', 'my') = 9; ex9('another one bites the dust', 'the') = 18
    @param text: str
    @return int
    """
    l = len(pattern)
    i1 = text.find(pattern)
    i2 = text[i1 + l:].find(pattern)
    result = l + i1 + i2
    return result



"""
INSTRUCTIONS. READ CAREFULLY

You are given two files: `ex_main.py` and `test_main.py`.
Download them and place them in an empty folder on your laptop.

You have to complete the exercises in `ex_main.py` in one hour. Each function contains
a docstring stating the exercise and the task you need to accomplish.

The goal of this first exam is to evaluate your knowledge of data structures and simple
builtin operations in the python language, as well as your speed in typing and producing
correct python code.


ALLOWED RESOURCES:
    You should be able to complete all the exercises without referring to anything.
    However, in case you want to check something, you're allowed to use the following:

        1 - The Python documentation: https://docs.python.org/3/library/index.html
        2 - The course material and your notes

RULES:
    0 - EDIT ONLY THIS FILE (`ex_main.py`)
    1 - DO NOT MODIFY under any circumstance the file `test_main.py`
    2 - To verify your progress, run the unit tests with the command 
        `python3 -m unittest test_main.py`
        
        or, alternatively:
        `python3 test_main.py`
    3 - At the end of the exam, RENAME `ex_main.py` to `your_name.py` using
        your surname as the name of the file.
    4 - Send ONLY the renamed file to marco.milanesio@univ-cotedazur.fr
    5 - DO NOT SEND the file `test_main.py`
    6 - DEADLINE TO SEND the file: on the whiteboard! (the timestamp on the email message will rule)
    7 - No talking, No peeking. On the contrary your score will be 0.

EVALUATION:
    The exam will be automatically evaluated against the `test_main.py` unit test 
    script.

    Scores will be in the [0-8] range (1 test passed, 1 point).

    Failure to send before the deadline will result in a score = 0.


A NOTE ON ONLINE ASSISTANCE (e.g., chatgpt)
    The proposed solutions to simple exercises like the ones presented here are 
    treated in a very efficient ways by LLM-based tools like chatgpt or gemini.
    As a result, the proposed solutions are highly efficient and predictable.

    Despite we are not in primary school, I encourage you to think about the meaning of
    an exam and the consequences of using such tools on your learning journey.
    
    Given the predictability and the efficiency of the results given by online assistance tools, 
    any substantial overlap found will result in the invalidation of the test (score = 0).
"""


# place additional imports here if needed
import re

def ex1(text, char='-'):
    """
    Given a text of arbitrary length, divide the text on the character given and return the resulting list.
    E.g., ex1('hi-me') = ['hi', 'me']; ex1('hi-me', char='+') = ['hi-me']; ex1('abc', char='b') = ['a', 'c']
    @param text: string
    @return list
    """
    result = []
    
    return result


def ex2(arr):
    """
    Given a list of dictionaries with string keys and integer values, 
    navigate the keys in alphabetical order and return the integer resulting in the concatenation of the values.

    E.g., ex2([{'a': 4, 'd': 9}, {'e': 6, 'b': 12}]) = 41296;
          ex2([{'c': 1, 'a': 3}, {'b': 2}] = 321
    @param arr: list
    @return int
    """
    result = -1
    
    return result


def ex3(arr):
    """
    Using a `for` loop reverse the list of digits passed as argument.
    E.g., ex3([4, 3, 2, 5]) = [5, 2, 3, 4]; ex3([]) = []
    @param arr: list
    @return list
    """
    result = []
    
    return result

def ex4(arr):
    """
    Fill up so that the tests in test_exercises.py pass.
    @param arr: list
    @return list 
    """
    result = []

    return result


def ex5(arr):
    """
    Fill up so that the tests in test_exercises.py pass.
    @param arr: list
    @return list 
    """
    result = []

    return result

def ex6(number):
    """Find the most frequent digit in a given number, and return the number with its occurrence.
       E.g., ex6(123451) = (1, 2); ex6(2244) = (2, 2); ex6(1) = (1, 1)
       @param number: int
       @return tuple(int, int)
    """
    result = tuple()

    return result

def ex7(**kwargs):
    """
    Returns the number of non-numerical values passed in the parameters.
    E.g., ex7(a=1, b=2.5, c=[]) = 1; ex7(a={}, b='') = 2
    @param variable keywords
    @return int

    - HINT: you may need some exception handling
    """
    result = -1

    return result


def ex8(text, pattern):
    """
    Look for `pattern` in text. Return the index of the second occurrence of pattern in text.
    E.g., ex9('my test, my score, my day', 'my') = 9; ex9('another one bites the dust', 'the') = 18
    @param text: str
    @return int
    """
    result = -1

    return result



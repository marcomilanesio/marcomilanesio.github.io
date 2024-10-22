import time
from functools import wraps


def timeit(func):
    @wraps(func)    
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} executed in {end - start}')
        return res

    return wrapper


@timeit
def create_list(n):
    """
    Create a list of size n.
    @param n: int
    @return list
    """
    res = []
    for i in range(int(n)):
        res.append(i)
    return res

@timeit
def create_list_2(n):
    """
    Use list comprehension
    @param n: int
    @return list
    """
    return (i for i in range(int(n)))

x = 1e6

create_list(x)
create_list_2(x)






class MyError(ZeroDivisionError): 
    pass

def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        raise MyError('Module defined error')



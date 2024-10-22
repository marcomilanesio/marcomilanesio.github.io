class A:
    a = 42


class B(A):
    a = 15


class C(B):
    pass

class D(A, C):
    pass

d = D()
print(d.a)


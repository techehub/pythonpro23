class A :
    pass

class B(A):
    pass

class C:
   pass

class D (B,C):
    pass

obj = D ()
obj.test()

print (D.mro())
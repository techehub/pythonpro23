#import files.myfunctions as myf

from files.myfunctions import add,  diff
from files.myfunctions1 import  mul, div, add


def test():
    num1 = int (input ("Num1 :"))
    num2 = int(input("Num2 :"))
    op = input ("Calculation :")
    if (op == "+"):
        result = add(num1, num2)
    elif (op=="-"):
        result = diff (num1, num2)
    elif (op=="*"):
        result = mul(num1, num2)
    elif (op=="/"):
        result = div (num1, num2)
    else :
        print ("You are trying an invalid operator !!!")

    print (result )


test()

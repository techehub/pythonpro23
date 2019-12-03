#import files.myfunctions as myf

from files.myfunctions import add,  diff
from files.myfunctions1 import  mul, div, add


def calculate (logic , n1, n2):
    res = logic(n1, n2)
    return res


def test():
    num1 = int (input ("Num1 :"))
    num2 = int(input("Num2 :"))
    op = input ("Calculation :")


    if (op == "+"):
        logic = add
    elif (op=="-"):
        logic = diff
    elif (op=="*"):
        logic = mul
    elif (op=="/"):
        logic= div
    else :
        print ("You are trying an invalid operator !!!")

    print (type (logic))
    result = calculate(logic, num1, num2)

    print (result)

test()

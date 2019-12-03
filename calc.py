def add (a,b):
    return a+b

def diff (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b


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

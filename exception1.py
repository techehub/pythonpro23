
def div (a,b):
    res= a/b
    return res

def main ():
    try:
        a= int (input ("Num1:"))
        b= int (input ("Num2:"))
        res= div(a,b)
    except ValueError as e:
        print("Please provide numeric values")
        print(e)

    except ZeroDivisionError as e:
        print("Zero is not allowed. Please correct and try again")
        print(e)
    except Exception as e:
        print("Something  went wrong. Please try again")
        print(e)
    else:
        print(res)
    finally:
        print("Done")

main ()


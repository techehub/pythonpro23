class InvalidAccountError (Exception):
    pass

class InsuffientAmountError (Exception) :
    pass

data = {"111":10000, "222":20000 }

def withdraw(accno, amt):
    if ( accno not in data):
        raise InvalidAccountError()

    if data [accno] < amt:
        raise InsuffientAmountError()

    data[accno]= data [accno]- amt

def main():
    try :
        accno = input("Acc No :")
        amount = int(input("Enter Amount :"))
        withdraw(accno, amount)
        print ("Operation successful")
        print ("balance is ", data[accno])
    except InvalidAccountError:
        print ("Please check account number")
    except InsuffientAmountError:
        print ("Please check your balance")
    except :
        print("Could not perform operation. please try again")

main()
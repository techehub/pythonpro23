def mySquare_old(max):
    mylist = []
    i = 1;
    while i < max:
        mylist.append(i*i)
        i= i+1
    return mylist

def mySquare(max):
    i = 1;
    while i < max:
        yield i*i
        i= i+1

x= mySquare(10000000000000)
for val in x:
    print (val)
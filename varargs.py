def sum (a =0,b=0):
    return a+b

def add ( * a):
    sum  = 0
    for x in a :
        sum = sum +x
    return sum

def calc (x, y, *z, **vals):
    print (x)
    print (y)
    print (*z)
    print (vals)
    sum = add (*z) + x+ y + vals['a'] + vals['b']
    return sum


add (10,20,22,33)
#calc (10,100)


r= calc (10,100, 1,2,3 , a=10, b=20, c=100)
print (r)
x=sum (10,20)
print (x)
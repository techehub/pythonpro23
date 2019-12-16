def add (x, y) :
    return x+y

mylogic = lambda x,y,z : (x+y)/z
mylogic1 = lambda p,n,r : add (p,n)+ p + (p* n * r /100)

print (mylogic1 (10000,1,10))
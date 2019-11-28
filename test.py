acno= input ("Account Number")
p = input("Enter amount :")
t = input ("Enter Term :")
i = input ("Enter Rate:")

print (type(p))
print (type(t))
print (type(i))

p = int (p)
t = int (t)
i = int(i)

print (type(p))
print (type(t))
print (type(i))

total= p + p*t*i/100
print ("Total amount in " + acno + "is " +  total)




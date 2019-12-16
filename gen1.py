#for x in range (1,100, 5):
#    print (x)

x = iter (range (1,10, 5))
#print (next (x))
#print (next (x))
#print (next (x))

while True:
   try :
       e= next(x)
       print (e)
   except StopIteration:
       break

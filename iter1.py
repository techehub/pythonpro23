class myclass :
    def __init__ (self, start,end):
        self.start=start
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        self.start= self.start+1
        if (self.start<= self.end):
            return self.start
        else :
            raise StopIteration()

#for x in myclass (10,100):
#    print (x)

x = iter (myclass (10,100))

"""
print (next (x))
print (next (x))
print (next (x))
"""

while True:
   try :
       e= next(x)
       print (e)
   except StopIteration:
       break

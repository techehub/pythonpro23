class MyObject:

   def __init__(self):
       print ("Object created")

   def enter__(self):
      print ("Entered")
      return self

   def __exit__(self ,exc_type, exc_value, tb):
       print ("Exited")

   def mytest1(self):
       print ("111111")


   def mytest2(self):
       print ("22222")



with MyObject () as o:
   o.mytest1()
   o.mytest2()


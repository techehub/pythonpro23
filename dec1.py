import logging
import time

logging.basicConfig(filename="mylog2.txt", level=logging.DEBUG)

def outer (func):
    def inner (*args, **kwargs):
        start = time.time()
        logging.debug("func.__name__" + func.__name__ +
              "*args=" + str (args) + "**kwargs" + str (kwargs))
        try:
            func (*args, **kwargs)
        except Exception as e :
            logging.error(e)

        end = time.time()
        timediff = end - start
        logging.info ("time taken :" + str (timediff))

    return inner

@outer
def add (x, y):
    print ( x+y)

@outer
def div (x,y):
    return x/y

@outer
def hai ():
    print ("Hello")

@outer
def greet (phone, **val):
    print  (phone, val["msg"] + "," + val["name"])

def diff (x,y):
    print ( x-y)


greet ("2132342", name="Kumar", msg="Good morning")
div (10,0)
add(10,20)

'''
add (10,10)
calc1 = outer (add)
calc1(10,10)
'''
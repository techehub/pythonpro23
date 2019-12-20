def totalMark (a, b):
    assert a <= 100 , "Max mark is 100"
    assert b <= 100 , "Max mark is 100"
    return a+b

def calcMark (marks):
    assert len (marks) ==4 , "Invalid number ofmarks"
    total =0
    for x in marks:
        assert x <= 100, "max mark is 100"
        total = total + x
    return total


#total=totalMark(50, 110)
total = calcMark([10,10,30,400])
print (total)

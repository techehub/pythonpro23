start =0
end = 10
evensum = 0
oddsum =0
while start < end:
    num =  int (input ("Enter number :"))

    if num > 100 :
        break

    if (num % 2 ==0):
        evensum  = evensum + num
    else :
        oddsum = oddsum + num
    start = start +1

else :
    print (evensum)
    print (oddsum)

print ("Done!!!")

sum =0
while True:
    val = input ("Enter Value")
    if val == "Q" or val == "q":
        break

    if int(val) % 2 !=0 :
        continue

    sum = sum + int (val)

print (sum)






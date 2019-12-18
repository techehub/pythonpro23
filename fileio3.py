file = open("data.csv", "r")
file1 = open("result1.csv", "w")
file2 = open("result2.csv", "w")
file3 = open("result3.csv", "w")

lines = file.readlines()

result = []
for line in lines:
    vals = line.split(",")
    totalmark = int(vals[2]) + int(vals[3]) + int(vals[4]) + int(vals[5])
    result. append( (vals[0] , vals[1] , totalmark) )

#rank list
result.sort(key = lambda x : x[2], reverse=True)
for x in result :
    line = x[0] + "," + x [1] + "," + str ( x[2] ) + "\n"
    file1.write(line)

#rollno list
result.sort(key = lambda x : x[0])
for x in result :
    line = x[0] + "," + x [1] + "," + str ( x[2] ) + "\n"
    file2.write(line)

#name list
result.sort(key = lambda x : x[1])
for x in result :
    line = x[0] + "," + x [1] + "," + str ( x[2] ) + "\n"
    file3.write(line)
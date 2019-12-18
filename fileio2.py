file =open ("data.csv", "r")
file1 = open ("result.csv","w")

lines = file.readlines()

for line in lines:
    vals = line.split(",")
    totalmark = int ( vals [2]) + int ( vals[3] ) + int ( vals [4]) + int ( vals[5])
    file1.write  (vals [0] +"," + vals [1] +"," + str ( totalmark) + "\n")



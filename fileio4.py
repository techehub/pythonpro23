
def readFile1 (filename):
    file = None
    try :
        file = open (filename)
        print (type(file))
        return file.readlines()
    except Exception as e:
        print (e)
    finally:
        if file != None:
            file.close()

def readFile (filename):
    with open (filename) as file:
        return file.readlines()

def process(lines):
    result = []
    for line in lines:
        vals = line.split(",")
        totalmark = int(vals[2]) + int(vals[3]) + int(vals[4]) + int(vals[5])
        result.append((vals[0], vals[1], totalmark))
    return result

def write(result, filename):
    with  open (filename, "w") as file:
        for x in result:
            line = x[0] + "," + x[1] + "," + str(x[2]) + "\n"
            file.write(line)

def main ():
    try:
        lines = readFile("data.csv")
        result = process(lines)

        # rank list
        result.sort(key=lambda x: x[2], reverse=True)
        write(result, "r1.txt")

        # rollno list
        result.sort(key=lambda x: x[0])
        write(result, "r2.txt")

        # name list
        result.sort(key=lambda x: x[1])
        write(result, "r3.txt")

    except Exception as e:
        print(e)

main ()


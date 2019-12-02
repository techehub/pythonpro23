data = {"name": "Kumar",
        "id": "2323",
        "phone" : 8745873465}

print ( "phone" in data)


stocks = {"TCS" : 1200, "INFOSYS": 3456}
print (stocks)
print (stocks ["TCS"])

stocks ["HCL"] = 567
print (stocks)

print (stocks.get("INFOSY", "NA"))

stocks.update ({"WIPRO": 765, "MARUTHI": 5678, "TCS":1400})

print (stocks)

x= stocks.pop("TCS")

print (x)
print (stocks)

del stocks["WIPRO"]
print (stocks)

print (stocks.keys())
print (stocks.values())
print (stocks.items())


for x in stocks.values():
    print (x)

for x in stocks.keys():
    print (x, stocks[x])


for x,y in stocks.items():
    print (x,y)


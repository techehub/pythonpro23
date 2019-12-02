data = {

        "111": {"name":"Seetha",
                "phone": 76575,
                "mark": [22,33,44]
                },
        "222": {"name":"Kumar",
                "phone": 31212,
                "mark": [22,33,77]
                },
        "333": {"name": "Anand",
            "phone": 31212,
            "mark": [22, 55, 35]
            },
        }

for k,v in data.items ():
    marks= v ["mark"]
    total=0
    for x in marks:
        total = total + x
    print (k, v ["name"], total)



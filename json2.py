import json

with open ("jsondata1") as file:
   data= json.load(file)
   #data= json.loads(file.read())
   print (data["name"])
   print (data['marks'])

total = 0
for x in data['marks']:
   total =total + x

data['total']= total
with open ("jsondata","w") as fp:
   data= json.dump(data,fp)

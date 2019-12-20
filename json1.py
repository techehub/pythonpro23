import json

txt = '{"name" : "kumar", "mark": 170}'
d = json.loads(txt)

print (d)
print (type(d))

d['age']=25

txt1= json.dumps(d)
print (txt1)
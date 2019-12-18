list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,5,6,7,8,9,10]
newlist =[]
for x in list1:
   if x%2==0:
       newlist.append(x)

print (newlist)

# LIST
newlist1 = [x*2 for x in list1]
newlist2 = [x*x for x in list1 if x%2==0]
newlist3 = [x for x in list1 if x%2==0
                    for y in list2 if y%2!=0 ]

print (newlist1)
print (newlist2)
print (newlist3)

# SET

myset = {(x,y) for x in list1 if x%2==0
                    for y in list2 if y%2!=0 }
print (myset)


# GENERATOR

gen = ((x,y) for x in list1 if x%2==0
                    for y in list2 if y%2!=0 )

gen = ((x,y) for x in range(1,1000000) if x%2==0
                    for y in range(20000,300000) if y%2!=0 )

print (gen)
'''
for x in gen:
    print (x)    
'''

# DICT

keys = ["name", "age" ]
values =["Anil", 23, "333"]


z= zip (keys, values)
print (z)
for x in z :
   print (x)


mydic = {   k: v for k,v in zip(keys,values) }
print (mydic)
print (type(mydic))

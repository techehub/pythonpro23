names = {"kumar", "seetha", "tom", "kumar", "tom"}
print (names)

for x in names:
    print (x)

print (len (names))
names.add("kabeer")
names.add("peter")
print (names)
names.update (["tom", "anand"])
print (names)


names.remove ("tom")
print (names)

names.discard("ABC")

name= names.pop ()
print (name)
print (names)

names1 = names.copy()
names1.update(["Somu","Manu"])
print (names1)

print (names1.issuperset(names))

mynames = {"Tinu", "Tomy"}


val = {}

print ("-----")
print (names1)
names1 = names1.union( mynames)
print (mynames)
print (names1)


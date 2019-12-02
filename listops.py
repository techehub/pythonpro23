nums = [22,33,44,55]

print (len (nums))
print (nums [1:3])
nums.append(66)
print (nums)

nums.insert(2,100)
print (nums)

x= nums.pop(2)
print (x)
print (nums)

nums.remove(44)
print (nums)

num1 = [1,2,3,4,"Apple", "Orange"]
nums.extend (num1)
print (nums)

del nums[2]
print (nums)

nums.clear()
print (nums)


nums = (33,44,55,66,55,66)
print (type (nums))
print (nums[2:4])
nums1 = list (nums)
print (nums1)
nums2= tuple(nums1)
print (nums2)

for x in nums2:
    print (x)
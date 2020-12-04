# Task 1
nums1 = [34, 32, 55, 234, 546]
nums2 = [45, 675, 32]
zipped_list = list(zip(nums1, nums2))
print(zipped_list)

# Task 2
nums = [x for x in range(1, 8)]
nums1 = [34, 32, 55, 234, 546, 45, 675, 32]
zipped_list = list(zip(nums, nums1))
print(zipped_list)

# Task 3
print(sorted(nums1))

# Task 4
odd_nums = list(filter(lambda x:x%2!=0, nums1))
print(odd_nums)
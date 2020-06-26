def sort(nums):
    for i in range(5):
        minpos=i
        for j in range (i,6):
            if nums[j] < nums[minpos]:
                minpos=j
        temp = nums[i]
        nums[j] = nums[minpos]
        nums[minpos] = temp


nums = [5, 3, 8, 6, 7, 2]

print(nums)
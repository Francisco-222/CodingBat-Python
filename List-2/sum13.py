def sum13(nums):
    nums.insert(0, 0)
    
    return sum(0 if nums[i - 1] == 13 or n == 13 else n for i, n in enumerate(nums))

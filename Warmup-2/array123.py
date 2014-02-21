def array123(nums):
    searchNums = [1, 2, 3]
    for i in range(1, len(nums)):
        if searchNums == nums[i - 1:i + 2]:
            return True

    return False

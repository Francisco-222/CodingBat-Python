def rotate_left3(nums):
    return [nums[(i + 1) if (i + 1 < len(nums)) else 0] for i in range(len(nums))]

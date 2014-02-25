def sum13(nums):
    after_13 = False
    sum = 0
    for n in nums:
        if n == 13:
           after_13 = True
        elif after_13:
           after_13 = False
        else:
           sum += n

    return sum

def sum67(nums):
    sum = 0
    ignore = False
    for n in nums:
        if n == 6:
            ignore = True
        elif ignore and n == 7:
            ignore = False
        elif not ignore:
            sum += n

    return sum

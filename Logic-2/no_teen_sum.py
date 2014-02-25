def no_teen_sum(a, b, c):
    return sum(map(lambda x: 0 if (13 <= x <= 14 or 17 <= x <= 19) else x, [a, b, c]))

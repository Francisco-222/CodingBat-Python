def no_teen_sum(a, b, c):
    return sum(map(fix_teen, [a, b, c]))

def fix_teen(x):
    return 0 if (13 <= x <= 14 or 17 <= x <= 19) else x

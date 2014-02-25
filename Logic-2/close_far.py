def close_far(a, b, c):
    diff_ab = abs(a - b)
    diff_ac = abs(a - c)
    diff_bc = abs(b - c)
    
    return    (diff_ab <= 1 and diff_ac >= 2 and diff_bc >= 2) \
           or (diff_ac <= 1 and diff_ab >= 2 and diff_bc >= 2)

def lucky_sum(a, b, c):
    xs = [a, b, c]
    for i, x in enumerate(xs):
        if x == 13:
            xs[i:] = [0] * (len(xs) - i)
            break
        
    return sum(xs)

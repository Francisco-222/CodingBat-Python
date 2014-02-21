def last2(str):
    length = len(str)
    if length <= 2:
        return 0

    cnt = 0
    part = str[-2:]
    for i in range(0, length - 2):
        if part == str[i:i+2]:
            cnt += 1

    return cnt

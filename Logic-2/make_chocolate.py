def make_chocolate(small, big, goal):
    need_big   = goal / 5
    need_small = goal % 5

    if need_big < big:
        need_big = 0
    else:
        need_big -= big
        
    need_small += need_big * 5

    if need_small <= small:
        return need_small
    else:
        return -1

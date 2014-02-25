def make_bricks(small, big, goal):
    need_big   = goal / 5
    need_small = goal % 5

    if need_big <= big:
        need_big = 0
    else:
        need_big -= big

    return small >= need_small + need_big * 5

# timeout
#    for s_i in xrange(0, small + 1):
#        for b_i in xrange(0, big + 1):
#            if s_i + b_i * 5 == goal:
#                return True
#    return False

def double_char(str):
    if len(str) == 0:
        return str
    return reduce(lambda x,y: x + y, map(lambda x: x * 2, list(str)))

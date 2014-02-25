def count_hi(str):
    return sum(str[i:i+2] == 'hi' for i in range(len(str) -1))

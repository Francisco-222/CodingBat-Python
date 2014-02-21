def front_back(str):
    length = len(str)
    
    if length <= 1:
        return str

    return str[length-1] + str[1:length -1] + str[0]

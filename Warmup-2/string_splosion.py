def string_splosion(str):
    retStr = ''
    for idx, char in enumerate(str):
        retStr += str[:idx + 1]

    return retStr

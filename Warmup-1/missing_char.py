def missing_char(str, n):
    # :n is not include n
    return str[:n] + str[n+1:]

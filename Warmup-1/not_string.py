# Common problems: code should not use print or import or eval
# not use re(regex)

def not_string(str):
    if str.find('not') == 0:
        return str
    else:
        return 'not ' + str

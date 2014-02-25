def count_code(str):
    a_z_list = range(ord('a'), ord('z') + 1) + range(ord('A'), ord('Z') + 1) 
    coxe_list = ['co%se' % chr(i) for i in a_z_list]

    return sum(map(lambda x: str.count(x), coxe_list))

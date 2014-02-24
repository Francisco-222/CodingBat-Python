def caught_speeding(speed, is_birthday):
    small_start = 61
    big_start = 80
    
    if is_birthday:
        small_start += 5
        big_start += 5
      
    if speed < small_start:
        return 0
    elif small_start <= speed <= big_start:
        return 1
    else:
        return 2

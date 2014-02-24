def squirrel_play(temp, is_summer):
    lower = 60
    upper = 90
    if is_summer:
      upper = 100
      
    return lower <= temp <= upper

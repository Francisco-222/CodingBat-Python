def parrot_trouble(talking, hour):
    if not talking:
        return False
    
    if hour < 7 or hour > 20:
        return True
        
    return False

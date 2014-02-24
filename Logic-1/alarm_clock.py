def alarm_clock(day, vacation):
    weekend = day == 0 or day == 6
    if vacation and weekend:
        return 'off'
    elif vacation and not weekend:
        return '10:00'
    elif not vacation and weekend:
        return '10:00'
    else:
        return '7:00'

def power_of_2(num):
    exp = 1
    while 2**exp < num:
        exp += 2
    if 2**exp >= num:
        return True
    else:
        return False

power_of_2(128)

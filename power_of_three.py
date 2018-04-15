def power_of_3(num):
    exp = 1
    if num% 3 == 0:
        while 3**exp < num:
            exp += 1
    if 3**exp == num:
        return True
    else:
        return False

power_of_3(10)
power_of_3(3)
power_of_3(6)
power_of_3(27)

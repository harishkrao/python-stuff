def perfect_square(num):
    x = 2
    while x < num:
        if x**2 == num:
            break
        else:
            x += 1
    if x*x == num:
        return True
    else:
        return False

perfect_square(121)
perfect_square(49)
perfect_square(12)
perfect_square(25)
perfect_square(30)
perfect_square(2)

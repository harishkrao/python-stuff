def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        first = 0
        second = 1
        i = 1
        while i < position:
            next_val = first + second
            first = second
            second = next_val
            i += 1
        return next_val


print(get_fib(0))
print(get_fib(1))
print(get_fib(2))
print(get_fib(3))
print(get_fib(4))
print(get_fib(5))
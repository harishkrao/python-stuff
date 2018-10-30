def foo(*args):
    for a in args:
        print(a)
    return 'done'


print(foo(1, 2, 3))

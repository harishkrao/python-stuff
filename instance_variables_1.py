class Dog:

    kind = 'canine'
    # tricks = []

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(d.name)
print(e.name)
print(e.kind)

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks)
print(e.tricks)


def f1(self, x, y):
    return min(x, y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


c = C()
print(c.f(1, 2))
print(c.h())


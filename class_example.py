class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)


p = Point(2, 3)
print(p.x, p.y)
print(p.distance_from_origin())
p = Point(4, 5)
print(p)


def midpoint(p1, p2):
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return Point(mx, my)


p = Point(3, 4)
q = Point(5, 12)
r = midpoint(p, q)
print('Mid-point')
print(r)
r = p.halfway(q)
print(r)

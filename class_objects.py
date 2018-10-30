class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    @staticmethod
    def f():
        return 'Hello World'


print(MyClass.i)
print(MyClass.f)
print(MyClass.__doc__)
print(MyClass.__module__)

x = MyClass()

print(x.__module__)
print(x.__doc__)

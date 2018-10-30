class A(object):
    def foo(self, x):
        print "Executing foo(%s, %s)"%(self, x)
    
    @classmethod
    def class_foo(cls, x):
        print "Executing class_foo(%s, %s)"%(cls, x)
    
    @staticmethod
    def static_foo(x):
        print "Executing static_foo(%s)"%x

a=A()

print('Calling foo')
print(a.foo(1))

print('Calling class_foo')
print(a.class_foo(1))

print('Calling static_foo')
print(a.static_foo(1))

# print(A.foo(1))
print(A.class_foo(1))

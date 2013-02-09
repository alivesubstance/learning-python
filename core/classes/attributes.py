from __future__ import print_function

class Parent:
    pass


class Child(Parent):
    def __str__(self):
        return "Child " + self.__dict__


c = Child
c.attr1 = 0

Parent.parentAttr = 1

print(c.parentAttr)
c.parentAttr = 2
print(c.parentAttr)

print(c.__dict__)
print(c.__module__)
print(c)
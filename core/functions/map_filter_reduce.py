__author__ = 'jericho'

m = map(lambda x: x ** 2, range(5))
print(type(m), m)

f = filter(lambda x: x % 2 == 0, range(-10, 3))
print(type(f), f)

r = reduce(lambda x, y: x + y, range(5))
print(type(r), r)


def sum(x, y):
    print("x=", x, "y=", y)
    return y + x

r = reduce(sum, range(1, 5))
print(type(r), r)

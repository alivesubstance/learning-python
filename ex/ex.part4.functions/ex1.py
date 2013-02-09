from __future__ import print_function

def p(arg):
    print(arg)

p("string")
p(1)
p([1, 2])
p({"a": 1, "b": 2})
p((1,2,3))
p((x ** 2 for x in range(3)))
p("-" * 20)
p(1,2)


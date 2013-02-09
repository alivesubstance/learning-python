from __future__ import print_function

def adder(arg1, arg2):
    sum = arg1 + arg2
    print(sum)

adder(1, 2)

try:
    adder(1, "2")
except TypeError:
    print("There is impossible to sum int and str: adder(1, \"2\")")

adder()

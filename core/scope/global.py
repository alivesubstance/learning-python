__author__ = 'jericho'

from module1 import module1_string

print module1_string

def change_global():
    global module1_string
    module1_string = "Change global string"
    print module1_string

change_global()

print module1_string

from __future__ import print_function
from functions import *
from movements import l, r, u, d

magic_num = 15

cube = random_cube()
print_cube(cube)

move_symbol_directly(cube, 5, (1, 1))
print("Move 5 to center:")
print_cube(cube)

analyzed = analyze(cube)

print("Analyzed:")
print_cube(analyzed[0])

print("Magic cube:")
print_cube(analyzed[1])
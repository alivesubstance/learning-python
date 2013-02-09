from __future__ import print_function
from functions import *

#cube = random_cube()
cube = [[1,2,3],[4,5,6],[7,8,9]]
move_symbol_directly(cube, 5, (1,1))
print_cube(cube)

analyze_matrix = analyze(cube)
print_cube(analyze_matrix[0])
print("magic:")
print_cube(analyze_matrix[1])
history = [copy.deepcopy(cube)]

while 1:
    move = raw_input("Enter move:")
    direction = move[0]
    if direction == 'u':
        u(int(move[1]) - 1, cube)
        history.append(copy.deepcopy(cube))
    elif direction == 'd':
        d(int(move[1]) - 1, cube)
        history.append(copy.deepcopy(cube))
    elif direction == 'r':
        r(int(move[1]) - 1, cube)
        history.append(copy.deepcopy(cube))
    elif direction == 'l':
        l(int(move[1]) - 1, cube)
        history.append(copy.deepcopy(cube))
    elif direction == 'a':
        print_cubes_hor(analyze(cube))
    print_cubes_hor(history)


from __future__ import print_function
from random import shuffle
from movements import l, r, u, d

import copy

magic_cube = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

def _create_magic_cubes(magic_cube):
    cubes = []
    cubes.append(magic_cube)
    cubes.append(
        [[magic_cube[row][col] for row in range(len(magic_cube))] for col in range(len(magic_cube) - 1, -1, -1)])

    c = copy.copy(magic_cube)
    transpose = zip(*c)
    cubes.append(transpose)

    tr2 = []
    for col in range(len(transpose)):
        row_ar = []
        for row in range(len(transpose) - 1, -1, -1):
            row_ar.append(transpose[row][col])
        tr2.append(row_ar)
    cubes.append(tr2)

    #create mirrored cubes
    mirrored = []
    for cube in cubes:
        mirrored.append([[cube[row][col] for row in range(len(cube) - 1, -1, -1)] for col in range(len(cube))])

    cubes.extend(mirrored)

    return cubes


magic_cubes = _create_magic_cubes(magic_cube)

class Move:
    def __init__(self, direction, row_col):
        self.direction = direction
        self.row_col = row_col


def print_cube(cube, ):
    for row in range(len(cube)):
        for col in range(len(cube)):
            print(str(cube[row][col]) + " ", end="")
        print()
    print()


def check_rows(s, magic_num):
    for row in range(len(s)):
        if sum(s[row]) != magic_num:
            return False
    return True


def check_cols(s, magic_num):
    for col in range(len(s)):
        sum = 0
        for row in range(len(s)):
            sum += s[row][col]

        if sum != magic_num:
            return False
    return True


def check_diag(s, magic_num):
    sum = 0
    for i in range(len(s)):
        sum += s[i][i]
    if sum != magic_num:
        return False

    sum = 0
    for i in range(len(s)):
        sum += s[i][len(s) - 1 - i]
    if sum != magic_num:
        return False

    return True


def check(s, magic_num):
    return check_rows(s, magic_num) and check_cols(s, magic_num) and check_diag(s, magic_num)


def find_symbol_index(symbol, cube):
    for row in range(len(cube)):
        for col in range(len(cube)):
            if cube[row][col] == symbol:
                return row, col


def create_position_matrix(magic_cube, given_cube):
    return [[1 if magic_cube[row][col] == given_cube[row][col] else 0
             for col in range(len(given_cube))]
            for row in range(len(given_cube))]


def _count_non_zero_elements(position_matrix):
    rez = 0
    for row in position_matrix:
        rez += sum(row)
    return rez


def analyze(given_cube):
    """
    Compare all magic cubes with current and return matrix of comparison results
    (0 - if the elements is different,1 otherwise) and mostly matched magic cube.
    """
    global magic_cubes
    position_matrixes = {}

    for mc in magic_cubes:
        position_matrix = create_position_matrix(mc, given_cube)
        position_matrixes[str(position_matrix)] = position_matrix, mc

    match_elements = 0
    position_matrix_rez = ()
    for key in position_matrixes:
        match_elements_cur = _count_non_zero_elements(position_matrixes[key][0])
        if match_elements_cur > match_elements:
            match_elements = match_elements_cur
            position_matrix_rez = position_matrixes[key]

    return position_matrix_rez


def check_non_zero_symbol_col(col, analyzed_matrix):
    """
    Check that the given column has at least one non zero element
    """
    column_array = [row[col] for row in analyzed_matrix]
    non_zero_elements = filter(lambda x: x > 0, column_array)
    return len(non_zero_elements) == 0


def move_symbol_directly(cube, symbol, target):
    orig = find_symbol_index(symbol, cube)
    row_cur = orig[0]
    col_cur = orig[1]

    row_dif = target[0] - orig[0]
    if row_dif < 0:
        while row_cur != target[0]:
            u(col_cur, cube)
            row_cur = find_symbol_index(symbol, cube)[0]
    elif row_dif > 0:
        while row_cur != target[0]:
            d(col_cur, cube)
            row_cur = find_symbol_index(symbol, cube)[0]

    col_dif = target[1] - orig[1]
    if col_dif < 0:
        while col_cur != target[0]:
            l(row_cur, cube)
            col_cur = find_symbol_index(symbol, cube)[1]
    elif col_dif > 0:
        while col_cur != target[0]:
            r(row_cur, cube)
            col_cur = find_symbol_index(symbol, cube)[1]


def random_cube():
    values = range(1, 10, 1)
    shuffle(values)
    cube_len = 3
    return [[values[cube_len * col + row] for row in range(cube_len)] for col in range(cube_len)]


def print_cubes_hor(history):
    for row in range(len(history[0])):
        for cube in history:
            for col in range(len(history[0])):
                print(cube[row][col], end=' ')
            print(end="\t")
        print(end="\n")
    print(end="\n")


if __name__ == '__main__':
    magic_cubes = _create_magic_cubes(magic_cube)
    print_cubes_hor(magic_cubes)

    cube = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    analyzed = analyze(cube)
    print_cube(analyzed[0])
    print_cube(analyzed[1])
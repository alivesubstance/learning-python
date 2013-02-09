from __future__ import print_function

def d(col, cube):
    print("D" + str(col + 1))
    _du(col, cube, range(-1, len(cube) - 1, 1), 1)


def u(col, cube):
    print("U" + str(col + 1))
    _du(col, cube, range(len(cube) - 1, -1, -1), -1)


def _du(col, cube, range, sign):
    tmp = 0
    for row in range:
        if tmp:
            tmp2 = cube[row + 1 * sign][col]
            cube[row + 1 * sign][col] = tmp
            tmp = tmp2
        else:
            tmp = cube[row + 1 * sign][col]
            cube[row + 1 * sign][col] = cube[row][col]


def r(row, cube):
    print("R" + str(row + 1))
    _rl(row, cube, range(-1, len(cube) - 1, 1), 1)


def l(row, cube):
    print("L" + str(row + 1))
    _rl(row, cube, range(len(cube) - 1, -1, -1), -1)


def _rl(row, cube, range, sign):
    tmp = 0
    row = cube[row]
    for col in range:
        if tmp:
            tmp2 = row[col + 1 * sign]
            row[col + 1 * sign] = tmp
            tmp = tmp2
        else:
            tmp = row[col + 1 * sign]
            row[col + 1 * sign] = row[col]

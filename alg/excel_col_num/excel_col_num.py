from __future__ import print_function

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
size= len(a)

col = 0
for line in open("input.txt", "r"):
    col = line.rstrip()

col_reversed = col[::-1]
sum = 0
for i, c in enumerate(col_reversed):
    idx = a.index(c.upper()) + 1
    if not i:
        sum += idx
    else:
        sum += pow(size, i) * idx

print(sum)
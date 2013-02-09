from __future__ import print_function
import time

__author__ = 'mdzhachvadze'

import timeit

x = 8 ** 9

res = []
def for_func(x):
    for i in range(x):
        res.append(i ** 2)

compreh = timeit.timeit('[x ** 2 for x in range(' + str(x) + ')]', number=1)

start = time.time()
for_func(x)
for_loop = time.time() - start

map = timeit.timeit('map(lambda x: x ** 2, range(' + str(x) + '))', number=1)



print("compreh=", compreh, "map=", map, "for_loop=", for_loop)

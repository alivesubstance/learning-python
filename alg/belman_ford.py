from __future__ import print_function

def create_vertex(i, j, cost=1):
    def vertex(i, j, cost):
        i = i
        j = j
        cost = cost
        print("i=", i, "j=", j, "cost=", cost)

    return vertex

print(create_vertex(1,2))

m = [[create_vertex(i, j)(i, j;) for i in range(5)] for j in range(5)]

print(m[0][0])
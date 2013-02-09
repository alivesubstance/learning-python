from __future__ import print_function

class Adder:
    def add(self, x, y):
        raise NotImplementedError


class ListAdder(Adder):
    def add(self, x, y):
        l = []
        return x.


class MyList():
    listAdder = ListAdder()

    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        MyList.listAdder.add(self.list, other.list)


class DictAdder(Adder):
    def add(self, x, y):
        d = {}
        for key in x.keys():
            d[key] = x[key]

        for key in y.keys():
            d[key] = y[key]
        return d


class MyDict():
    dictAdder = DictAdder()

    def __init__(self, dict):
        self.dict = dict

    def __add__(self, other):
        MyDict.dictAdder.add(self.dict, other)


l1 = MyList([1, 2, 3])
l2 = MyList(["a", "b"])
print(l1 + l2)
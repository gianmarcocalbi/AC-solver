import abc

"""
Constraint Interface Class
"""

CONSTRAINT_NAMES = [""]


class Constraint:
    def __init__(self, x, y, table, name=""):
        global CONSTRAINT_NAMES
        self.x = x
        self.y = y
        self.table = {}
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j]:
                    a = self.x.domain[i]
                    b = self.y.domain[j]
                    if not a in self.table:
                        self.table[a] = {}
                    self.table[a][b] = True
        self.id = id(self)
        if name in CONSTRAINT_NAMES:
            name = id(self)
        self.name = name
        CONSTRAINT_NAMES.append(str(self.name))

    def consistent(self, a, b):
        if a in self.table:
            if b in self.table[a]:
                return True
        return False

    @abc.abstractmethod
    def filter_from(self, var, P):
        pass

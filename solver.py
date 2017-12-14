from inc.variable import *
from inc.propagation import *

"""
exp must be a STRING formatted as an aritmetic valid expression in which:
- "x" stands for the first variable
- "y" stands for the second variable
- all constants are allowed
- all comparison operator are allowed (>, <, >=, <=, =, !=)
- all aritmetic operators are allowed (+, -, *, /, %)
- all python aritmetic function are allowed (e.g. "math.pow()", "math.floor()", etc...)
- other python functions, symbols, variables can potentially break the computation, so they're not allowed 
"""


class Solver:

    def __init__(self, algo):
        self.algo = algo
        self.variables = {}
        self.constraints = {}

    @staticmethod
    def tableFromExp(X, Y, exp):
        table = []
        for i in range(len(X.domain)):
            x = X.domain[i]
            table.append([])
            for j in range(len(Y.domain)):
                y = Y.domain[j]
                table[i].append(eval(exp))
        return table

    @staticmethod
    def tableFromSet(X, Y, allowedValueSet):
        table = []
        for i in range(len(X.domain)):
            x = X.domain[i]
            table.append([])
            for j in range(len(Y.domain)):
                y = Y.domain[j]
                table[i].append((x, y) in allowedValueSet)
        return table

    def addVariable(self, domain, name=""):
        v = Variable(domain, name)
        self.variables[v.name] = v
        return v.name

    def getVariable(self, name):
        if name in self.variables:
            return self.variables[name]
        return None

    def addConstraint(self, x_name, y_name, exp, name=""):
        x = self.variables[x_name]
        y = self.variables[y_name]
        c = self.algo(x, y, self.tableFromExp(x, y, exp), name)
        self.constraints[c.name] = c
        return c.name

    def addCustomConstraint(self, x_name, y_name, allowedValueSet, name=""):
        x = self.variables[x_name]
        y = self.variables[y_name]
        c = self.algo(x, y, self.tableFromSet(x, y, allowedValueSet), name)
        self.constraints[c.name] = c
        return c.name

    def filter(self):
        propagation = Propagation(list(self.constraints.values()))
        propagation.enqueue(list(self.variables.values()))
        propagation.run()

    def solve(self):
        pass
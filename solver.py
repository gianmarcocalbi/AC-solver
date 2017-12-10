import abc, math, numpy as np


class Variable:
    id_counter = 0

    def __init__(self, domain):
        self.domain = domain  # list of allowed values for this variable
        self.type = type(domain[0])
        self.delta = []
        self.propagation = None
        self.id_counter += 1
        self.id = self.id_counter

    def is_in_domain(self, a):
        if a in self.domain:
            return True
        return False

    def delta_is_empty(self):
        return len(self.delta) == 0

    def reset_delta(self):
        self.delta = []


class Propagation:

    def __init__(self, variables, constrains):
        self.queue = []  # contains variables with not-null delta
        self.graph = {}  # constraints' graph i.e. for each variable the set of constraints with regard to it

        for c in constrains:
            x_id = c.x.id_counter
            y_id = c.y.id_counter
            if x_id not in self.graph:
                self.graph[x_id] = []

            if y_id not in self.graph:
                self.graph[y_id] = []

            self.graph[x_id].append(c)
            self.graph[y_id].append(c)

    """
    Add variable x into queue whether not present
    """

    def enqueue(self, x):
        if x not in self.queue:
            self.queue.append(x)

    def dequeue(self):
        return self.queue.pop(0)

    def run(self):
        # // tant que queue_ n'est pas vide
        #     // prendre x dans queue_ avec pick in queue
        #     // pour chaque contrainte c impliquant x
        #         // bool ret=c->filter_from(x);
        #         // if (!ret) // on arrete l'algo: un domaine est vide
        #     // fin pour
        #     // x->reset_delta();
        # // fn tant que

        while len(self.queue) > 0:
            x = self.dequeue()
            for c in self.graph[x.id]:
                if not c.filter_from(x):
                    # stop algorithm
                    pass
                x.reset_delta()


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


# todo: not number variables
def tableFromExp(X, Y, exp):
    table = []
    for i in range(len(Y.domain)):
        y = Y.domain[i]
        table.append([])
        for j in range(len(X.domain)):
            x = X.domain[j]
            table[i].append(eval(exp))

    return table


def tableFromSet(X, Y, allowedValueSet):
    table = []
    for i in range(len(Y.domain)):
        y = Y.domain[i]
        table.append([])
        for j in range(len(X.domain)):
            x = X.domain[j]
            table[i].append((x, y) in allowedValueSet)
    return table


class Constraint:
    def __init__(self, x, y, table):
        self.x = x
        self.y = y
        self.table = table

    @abc.abstractmethod
    def filter_from(self, var):
        pass


class AC3Constraint(Constraint):
    def __init__(self):
        pass

    def filter_from(self, var):
        # Input:
        # A set of variables X
        # A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
        # A set of unary constraints R1(x) on variable x that must be satisfied
        # A set of binary constraints R2(x, y) on variables x and y that must be satisfied
        #
        # Output:
        # Arc consistent domains for each variable.
        #
        # function ac3 (X, D, R1, R2)
        # // Initial domains are made consistent with unary constraints.
        # for each x in X
        #     D(x) := { vx in D(x) | R1(x) }
        # // 'worklist' contains all arcs we wish to prove consistent or not.
        # worklist := { (x, y) | there exists a relation R2(x, y) or a relation R2(y, x) }
        #
        # do
        # select any arc (x, y) from worklist
        # worklist := worklist - (x, y)
        # if arc-reduce (x, y)
        #     if D(x) is empty
        #         return failure
        #     else
        #         worklist := worklist + { (z, x) | z != y and there exists a relation R2(x, z) or a relation R2(z, x) }
        # while worklist not empty
        #
        # function arc-reduce (x, y)
        # bool change = false
        # for each vx in D(x)
        #     find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
        #     if there is no such vy {
        #     D(x) := D(x) - vx
        #     change := true
        #     }
        #     return change


        pass


if __name__ == "__main__":
    a = Variable(list(range(0, 10)))
    b = Variable(list(range(0, 10)))
    c = Variable(list(range(-9, 1)))
    Cab = Constraint(a, b, tableFromExp(a, b, "x+y>5"))
    Cbc = Constraint(b, c, tableFromExp(b, c, "x+y>=0"))
    Cac = Constraint(a, c, tableFromExp(a, c, "x*y < y/4"))
    P = Propagation((a, b, c), (Cab, Cbc, Cac))

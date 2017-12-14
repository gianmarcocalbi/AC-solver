from inc.constraint_interface import *


class AC4Constraint(Constraint):
    def __init__(self, x, y, table):
        Constraint.__init__(self, x, y, table)

        self.S = {
            "x": {},
            "y": {}
        }

        for a in list(self.table.keys()):
            for b in list(self.table[a].keys()):
                self.S["x"][a].append(b)
                self.S["y"][b].append(a)

    """
    Let x be the argument variable.
    Let y be the second variable with regards to the constraint.
    A constraint is a set of pairs (x,y).
    Let C(x,y) : D(x) x D(y) -> {True, False} be a function s.t.
        C(x,y) = True iff (x,y) is an allowed value for the constraint
        C(x,y) = False otherwise
    Then this method returns:
    - True if for all x, exists at least on y s.t. C(x,y) is true
    - False if exists at least one x s.t. for all y, C(x,y) == False
    """

    def filter_from(self, var, P):
        ret = True

        if var.id == self.x.id:
            considered_var = self.x
            considered_var.tag = "x"
            other_var = self.y
            other_var.tag = "y"
        elif var.id == self.y.id:
            considered_var = self.y
            considered_var.tag = "y"
            other_var = self.x
            other_var.tag = "x"
        else:
            raise Exception("Error in filter_from: filtering from a variable that doesn't belong to the constraint")

        domain_index_to_pop = []

        for a in considered_var.delta:
            for b in self.S[considered_var.tag][a]:
                self.S[other_var.tag][b].remove(a)
                if len(self.S[other_var.tag][b]):
                    del self.S[other_var.tag][b]
                    domain_index_to_pop.append(other_var.domain.index(b))

        domain_index_to_pop.sort()
        i = 0
        for index in domain_index_to_pop:
            considered_var.domain.pop(index - i)
            i += 1

        for i in range(len(considered_var.domain)):
            a = considered_var.domain[i]
            found = False
            for j in range(len(other_var.domain)):
                b = other_var.domain[j]
                if self.consistent(a, b):
                    found = True
                    break
            if not found:
                domain_index_to_pop.append(i)
                ret = False
        return ret

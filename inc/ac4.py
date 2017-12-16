from inc.constraint_interface import *


class AC4Constraint(Constraint):
    def __init__(self, x, y, table, name=""):
        Constraint.__init__(self, x, y, table, name)

        # AC4 initialization
        S = {
            x.id: {},
            y.id: {}
        }

        for a in x.domain:
            S[x.id][a] = []
            for b in y.domain:
                if not b in S[y.id]:
                    S[y.id][b] = []
                if self.consistent(a, b):
                    S[x.id][a].append(b)
                    S[y.id][b].append(a)

        self.S = {
            x.id: {},
            y.id: {}
        }

        for a in x.domain[:]:
            if len(S[x.id][a]) > 0:
                self.S[x.id][a] = S[x.id][a]
            else:
                x.remove_value(a)

        for b in y.domain[:]:
            if len(S[y.id][b]) > 0:
                self.S[y.id][b] = S[y.id][b]
            else:
                y.remove_value(b)

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

    def filter_from(self, var):

        if var.id == self.x.id:
            main_var = self.x
            supp_var = self.y
        elif var.id == self.y.id:
            main_var = self.y
            supp_var = self.x
        else:
            raise Exception("Error in filter_from: filtering from a variable that doesn't belong to the constraint")

        for i in range(len(main_var.delta)):
            a = main_var.delta[i]
            if a in self.S[main_var.id]:
                for b in self.S[main_var.id][a]:
                    self.S[supp_var.id][b].remove(a)
                    if len(self.S[supp_var.id][b]) == 0:
                        supp_var.remove_value(b)

        return len(main_var.domain) > 0

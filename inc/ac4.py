from inc.constraint_interface import *


class AC4Constraint(Constraint):
    def __init__(self, x, y, table, name=""):
        Constraint.__init__(self, x, y, table, name)

        # AC4 initialization
        self.S = {
            x.id: {},
            y.id: {}
        }

        for a in x.domain[:]:
            self.S[x.id][a] = []
            for b in y.domain[:]:
                if not b in self.S[y.id]:
                    self.S[y.id][b] = []
                if self.consistent(a, b):
                    self.S[x.id][a].append(b)
                    self.S[y.id][b].append(a)
            if len(self.S[x.id][a]) == 0:
                x.remove_value(a)
                del self.S[x.id][a]

        for b in y.domain[:]:
            if len(self.S[y.id][b]) == 0:
                y.remove_value(b)
                del self.S[y.id][b]


    def filter_from(self, var):
        """
        Let Ci(x,y) be the constraint, let var be x.
        This method filter from x so loop through values of y.
        :param var: Variable which filter from
        :return: False if var.domain got empty during the process, True otherwise.
        """

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

from inc.constraint_interface import *


class AC6Constraint(Constraint):
    def __init__(self, x, y, table, name=""):
        Constraint.__init__(self, x, y, table, name)
        self.S = {
            x.id: {},
            y.id: {}
        }
        # self.initialize()

    def initialize(self):
        x = self.x
        y = self.y

        self.S = {
            x.id: {},
            y.id: {}
        }

        if len(x.domain) == 0 or len(y.domain) == 0:
            return False

        for a in x.domain[:]:
            if not (a in self.S[x.id]):
                self.S[x.id][a] = []
            found = False
            for b in y.domain[:]:
                if not b in self.S[y.id]:
                    self.S[y.id][b] = []
                if self.consistent(a, b):
                    self.S[y.id][b].append(a)
                    found = True
                    break
            if not found:
                x.remove_value(a)

        for b in y.domain[:]:
            if not (b in self.S[y.id]):
                self.S[y.id][b] = []
            found = False
            for a in x.domain[:]:
                if not (a in self.S[x.id]):
                    self.S[x.id][a] = []
                if self.consistent(a, b):
                    self.S[x.id][a].append(b)
                    found = True
                    break
            if not found:
                y.remove_value(b)
                # del self.S[y.id][b]

        return True

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

        """
        for each a in delta(x):
            # a is the value that we have removed from x.domain
            
            for each b in S[x.id][a]
            # for all values of y here we have to find a different support
            # from a because a doesn't belong to x.domain anymore. 
            # we have to assure that 
            
            a' <- alternative value for a for which (a',b) is consistent
            id not exists such a' then:
                # b has no support in x.domain so
                y.remove_value(b)
            else 
                # b has a' as support so
                S[x.id][a'].append(b)
        """

        for i in range(len(main_var.delta)):
            a = main_var.delta[i]
            if a in self.S[main_var.id]:
                for b in self.S[main_var.id][a]:
                    # self.S[supp_var.id][b].remove(a)
                    found = False
                    alt_a = None

                    keys = list(self.S[main_var.id].keys())

                    for j in range(keys.index(a), len(keys)):
                        if main_var.is_in_domain(keys[j]):
                            alt_a = keys[j]
                            if main_var == self.x:
                                found = self.consistent(alt_a, b)
                            else:
                                found = self.consistent(b, alt_a)
                        if found:
                            break

                    if found:
                        self.S[main_var.id][alt_a].append(b)
                    else:
                        supp_var.remove_value(b)
                        # del self.S[supp_var.id][b]
                self.S[main_var.id][a] = []
                #del self.S[main_var.id][a]

        return len(main_var.domain) > 0

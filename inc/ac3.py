from inc.constraint_interface import *


class AC3Constraint(Constraint):
    def __init__(self, x, y, table, name=""):
        Constraint.__init__(self, x, y, table, name)
        # self.initialize()

    def initialize(self):
        self.x.propagation.enqueue(self.x, self.y)
        return True

    def filter_from(self, var):
        """
        Let Ci(x,y) be the constraint, let var be x.
        This method filter from x so loop through values of y.
        :param var: Variable which filter from
        :return: False if var.domain got empty during the process, True otherwise.
        """
        if var.id == self.x.id:
            main_var = self.y
            supp_var = self.x
        elif var.id == self.y.id:
            main_var = self.x
            supp_var = self.y
        else:
            raise Exception("Error in filter_from: filtering from a variable that doesn't belong to the constraint")


        value_to_pop = []

        if main_var.delta_is_empty() and True:
            # if delta is empty is the first time we check this variable
            # so we must check all arcs

            for i in range(len(main_var.domain)):
                a = main_var.domain[i]
                found = False
                for j in range(len(supp_var.domain)):
                    b = supp_var.domain[j]

                    if main_var == self.x:
                        found = self.consistent(a, b)
                    else:
                        found = self.consistent(b, a)

                    if found:
                        break
                if not found:
                    value_to_pop.append(a)

        for val in value_to_pop:
            main_var.remove_value(val)

        return len(main_var.domain) > 0

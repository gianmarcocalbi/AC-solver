from inc.constraint_interface import *


class AC3Constraint(Constraint):
    def __init__(self, x, y, table, name=""):
        Constraint.__init__(self, x, y, table, name)
        x.propagation.enqueue(x)

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
            main_var = self.y
            supp_var = self.x
        elif var.id == self.y.id:
            main_var = self.x
            supp_var = self.y
        else:
            raise Exception("Error in filter_from: filtering from a variable that doesn't belong to the constraint")

        value_to_pop = []

        if main_var.delta_is_empty():
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

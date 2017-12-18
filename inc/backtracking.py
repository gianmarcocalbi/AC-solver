from inc.propagation import *


class Backtracking:
    def __init__(self, variables, propagation):
        self.propagation = propagation
        self.variables = variables
        pass

    def run(self):
        if not self.propagation.run():
            return False

        var_id = []
        var_domain_size = []
        for v in self.variables:
            var_id.append(v.id)
            var_domain_size.append(len(v.domain))

        var_ordering = [x for _, x in sorted(zip(var_domain_size, var_id))]

        return True

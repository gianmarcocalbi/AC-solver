from inc.variable import *
from inc.propagation import *
import math


class Solver:

    def __init__(self, algo):
        self.algo = algo
        self.variables = {}
        self.constraints = {}
        self.propagation = Propagation()

    @staticmethod
    def table_from_exp(X, Y, exp):
        """
        Creates a table for two variables evaluating a boolean expression
        :param X: first variable of the constraint
        :param Y: second variable of the constraint
        :param exp: must be a STRING formatted as valid Python 3 boolean expression.
        Nota Bene:
        - address first variable with "$1"
        - address second variable with "$2"
        - all constants are allowed
        - all comparison operator are allowed (>, <, >=, <=, =, !=)
        - all aritmetic operators are allowed (+, -, *, /, %)
        - all python aritmetic function are allowed (e.g. "math.pow()", "math.floor()", etc...)
        - etc...
        :return: boolean matrix table
        """
        table = []
        if "$1" in exp:
            exp = exp.replace("$1", "x")
        if "$2" in exp:
            exp = exp.replace("$2", "y")
        for i in range(len(X.domain)):
            x = X.domain[i]
            table.append([])
            for j in range(len(Y.domain)):
                y = Y.domain[j]
                table[i].append(eval(exp))
        return table

    @staticmethod
    def table_from_set(X, Y, allowedValueSet):
        """
        Creates a table for two variables starting from pairs of allowed value
        :param X: first variable
        :param Y: second variable
        :param allowedValueSet: list of pairs of values (values must be in domains of variables)
        :return: boolean matrix table
        """
        table = []
        for i in range(len(X.domain)):
            x = X.domain[i]
            table.append([])
            for j in range(len(Y.domain)):
                y = Y.domain[j]
                table[i].append((x, y) in allowedValueSet)
        return table

    def add_variable(self, domain, name=""):
        if not name in self.variables:
            v = Variable(domain, self.propagation, name)
            self.variables[v.name] = v
            return v.name
        else:
            raise Exception("Duplicate variable name is not allowed!")

    def get_variable_by_name(self, name):
        if name in self.variables:
            return self.variables[name]
        return None

    def get_variable_by_id(self, var_id):
        for x in self.variables:
            if var_id == x.id:
                return x
        return None

    def add_constraint(self, x_name, y_name, exp, name=""):
        x = self.variables[x_name]
        y = self.variables[y_name]
        c = self.algo(x, y, self.table_from_exp(x, y, exp), name)
        self.constraints[c.name] = c
        return c.name

    def add_custom_constraint(self, x_name, y_name, allowedValueSet, name=""):
        x = self.variables[x_name]
        y = self.variables[y_name]
        c = self.algo(x, y, self.table_from_set(x, y, allowedValueSet), name)
        self.constraints[c.name] = c
        return c.name

    def initialize_constraints(self):
        for c in self.constraints.values():
            if not c.initialize():
                return False
        return True

    def filter_domains(self):
        # initialize all constraints
        # """
        if not self.initialize_constraints():
            for x in self.variables.values():
                x.domain = []
            return self.get_variables_domains()
        # """

        # build propagation graph, if the graph has already been built
        # then it won't be rebuilt so the following method will be run
        # just one time
        self.propagation.build_graph(self.constraints.values())
        if not self.propagation.run():
            for x in self.variables.values():
                x.domain = []
        return self.get_variables_domains()

    def get_variables_order(self, domains=None):
        if domains is None:
            domains = self.get_variables_domains()
        var_domain_size = [len(val) for val in domains.values()]
        return [k for _, k in sorted(zip(var_domain_size, domains.keys()))]

    def get_variables_domains(self):
        domains = {}
        for x in self.variables.values():
            domains[x.name] = x.domain[:]
        return domains

    def set_variables_domains(self, domains):
        for name, values in domains.items():
            self.variables[name].domain = values[:]
            self.variables[name].reset_delta()

    @staticmethod
    def at_least_one_empty_domain(domains):
        for d in domains.values():
            if len(d) == 0:
                return True
        return False

    @staticmethod
    def each_domain_has_one_value(domains):
        for d in domains.values():
            if len(d) != 1:
                return False
        return True

    def solve(self):
        return self.backtracking(self.get_variables_domains())

    def simple_solve(self):
        return self.simple_bt(self.get_variables_domains())

    def simple_bt(self, domains):
        if self.at_least_one_empty_domain(domains):
            return {}

        self.set_variables_domains(domains)
        filtered_domains = self.filter_domains()

        if self.at_least_one_empty_domain(filtered_domains):
            return {}
        elif self.each_domain_has_one_value(filtered_domains):
            solution = {}
            if self.each_domain_has_one_value(self.filter_domains()):
                # if after filtering no value is removed then we have a good
                # solution for our problem
                for x in self.variables.values():
                    solution[x.name] = x.domain[0]
            return solution
        else:
            # get the name of the first variable x s.t. len(x.domain) > 1
            phi = None
            for x in self.variables.values():
                if len(filtered_domains[x.name]) > 1:
                    phi = x.name
                    break
            if phi is None:
                raise Exception("Very odd error: this should never occur!")

            # now phi is the pivot variable for this calling of backtrack function

            for k in range(len(filtered_domains[phi])):
                new_domains = dict(filtered_domains)
                new_domains[phi] = [filtered_domains[phi][k]]
                solution = self.simple_bt(dict(new_domains))
                if solution != {}:  # and not solution is None
                    return solution

            return {}

    def backtracking(self, domains):
        if self.at_least_one_empty_domain(domains):
            return {}

        self.set_variables_domains(domains)
        filtered_domains = self.filter_domains()

        if self.at_least_one_empty_domain(filtered_domains):
            return {}
        elif self.each_domain_has_one_value(filtered_domains):
            solution = {}
            if self.each_domain_has_one_value(self.filter_domains()):
                # if after filtering no value is removed then we have a good
                # solution for our problem
                for x in self.variables.values():
                    solution[x.name] = x.domain[0]
            return solution
        else:
            variables_order = self.get_variables_order(filtered_domains)
            # get the name of the first variable x s.t. len(x.domain) > 1
            phi = None
            for i in range(len(filtered_domains)):
                name = variables_order[i]
                if len(filtered_domains[name]) > 1:
                    phi = name
                    break
            if phi is None:
                raise Exception("Very odd error: this should never occur!")

            # now phi is the pivot variable for this calling of backtrack function

            for k in range(len(filtered_domains[phi])):
                new_domains = dict(filtered_domains)
                new_domains[phi] = [filtered_domains[phi][k]]
                solution = self.backtracking(dict(new_domains))
                if solution != {}:  # and not solution is None:
                    return solution

            return {}

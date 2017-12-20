from inc.variable import *
from inc.propagation import *


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
        - address each variable with its name, so if the name of the first variable is "x"
            then use "x" inside the expression
        - all constants are allowed
        - all comparison operator are allowed (>, <, >=, <=, =, !=)
        - all aritmetic operators are allowed (+, -, *, /, %)
        - all python aritmetic function are allowed (e.g. "math.pow()", "math.floor()", etc...)
        - etc...
        :return: boolean matrix table
        """
        table = []
        if X.name in exp:
            exp = exp.replace(X.name, "x")
        if Y.name in exp:
            exp = exp.replace(Y.name, "y")
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

    def filter_domains(self):
        # initialize all contraints
        for c in self.constraints.values():
            c.initialize()

        # build propagation graph, if the graph has already been built
        # then it won't be rebuilt so the followin method will be run
        # just one time
        self.propagation.build_graph(self.constraints.values())
        self.propagation.run()
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

    def backtracking(self, domains):
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
                solution = self.backtracking(new_domains)
                if solution != {}:
                    return solution

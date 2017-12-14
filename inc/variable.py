"""
Variable Class:

"""

VARIABLE_NAMES = [""]


class Variable:

    def __init__(self, domain, name=""):
        global VARIABLE_NAMES
        self.domain = domain  # list of allowed values for this variable
        self.type = type(domain[0])
        self.delta = []
        self.id = id(self)
        if name in VARIABLE_NAMES:
            name = id(self)
        self.name = name
        VARIABLE_NAMES.append(str(self.name))

    def getName(self):
        return self.name

    """
    Returns true if a is removed from domain.
    """

    def remove_value(self, a, P):
        if self.is_in_domain(a):
            self.domain.pop(self.domain.index(a))
            self.delta.append(a)
            P.enqueue([self])
            return True
        return False

    def is_in_domain(self, a):
        if a in self.domain:
            return True
        return False

    def delta_is_empty(self):
        return len(self.delta) == 0

    def reset_delta(self):
        self.delta = []

"""
Variable Class:

"""

VARIABLE_NAMES = [""]


class Variable:

    def __init__(self, domain, propagation, name=""):
        global VARIABLE_NAMES
        self.orig_domain = domain[:]
        self.domain = domain  # list of allowed values for this variable
        self.type = type(domain[0])
        self.propagation = propagation
        self.delta = []
        # self.delta_index = []
        self.id = id(self)
        if name in VARIABLE_NAMES:
            name = id(self)
        self.name = name
        VARIABLE_NAMES.append(str(self.name))

    def get_name(self):
        return self.name

    """
    Returns true if a is removed from domain.
    """

    def remove_value(self, a):
        if self.is_in_domain(a):
            index = self.domain.index(a)
            self.domain.pop(index)
            if not a in self.delta:
                self.delta.append(a)
                #self.delta_index.append(index)
            self.propagation.enqueue(self)
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
        #self.delta_index = []

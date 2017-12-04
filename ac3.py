import abc

# Input:
# A set of variables X
# A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
# A set of unary constraints R1(x) on variable x that must be satisfied
# A set of binary constraints R2(x, y) on variables x and y that must be satisfied
#
# Output:
# Arc consistent domains for each variable.
#
# function ac3 (X, D, R1, R2)
# // Initial domains are made consistent with unary constraints.
# for each x in X
#     D(x) := { vx in D(x) | R1(x) }
# // 'worklist' contains all arcs we wish to prove consistent or not.
# worklist := { (x, y) | there exists a relation R2(x, y) or a relation R2(y, x) }
#
# do
# select any arc (x, y) from worklist
# worklist := worklist - (x, y)
# if arc-reduce (x, y)
#     if D(x) is empty
#         return failure
#     else
#         worklist := worklist + { (z, x) | z != y and there exists a relation R2(x, z) or a relation R2(z, x) }
# while worklist not empty
#
# function arc-reduce (x, y)
# bool change = false
# for each vx in D(x)
#     find a value vy in D(y) such that vx and vy satisfy the constraint R2(x, y)
#     if there is no such vy {
#     D(x) := D(x) - vx
#     change := true
#     }
#     return change

class Variable:

    def __init__(self):
        self.domain = ""
        self.delta = ""
        self.propagation = ""

    def is_in_domain(self, a):
        if a in self.domain:
            return True
        False


class Propagation:

    def __init__(self):
        self.queue = [] # contains variables with not-null delta
        self.graph = {} # constraints' graph i.e. for each variable the set of constraints with regard to it
        pass

    """
    Add variable x into queue whether not present
    """
    def enqueue(self, x):
        pass

    def dequeue(self):
        # remove a variable from the queue (which variable? at the moment I don't know)
        pass

    def run(self):
        # // tant que queue_ n'est pas vide
        #     // prendre x dans queue_ avec pick in queue
        #     // pour chaque contrainte c impliquant x
        #         // bool ret=c->filter_from(x);
        #         // if (!ret) // on arrete l'algo: un domaine est vide
        #     // fin pour
        #     // x->reset_delta();
        # // fn tant que
        pass

class Constraint:
    def __init__(self):
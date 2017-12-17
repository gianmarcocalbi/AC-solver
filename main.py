from solver import *
from inc.ac3 import *
from inc.ac4 import *
from inc.ac6 import *
from inc.ac2001 import *

if __name__ == "__main__":
    solver = Solver(AC6Constraint)
    solver.add_variable(list(range(0, 10)), "a")
    solver.add_variable(list(range(0, 10)), "b")
    solver.add_variable(list(range(0, 10)), "c")
    solver.add_constraint("a", "b", "a+b>12", "Cab")
    solver.add_constraint("b", "c", "b+c<7", "Cbc")
    solver.filter()
    print(solver.get_variable("a").domain)
    print(solver.get_variable("b").domain)
    print(solver.get_variable("c").domain)

    """
    solver = Solver(AC3Constraint)
    solver.add_variable(list(range(0, 2)), "a")
    solver.add_variable(list(range(0, 3)), "b")
    solver.add_variable(list(range(0, 3)), "c")
    solver.add_constraint("a", "b", "a == b", "Cab")
    solver.add_constraint("b", "c", "b == c", "Cbc")
    solver.filter()
    print(solver.get_variable("a").domain)
    print(solver.get_variable("b").domain)
    print(solver.get_variable("c").domain)
    """

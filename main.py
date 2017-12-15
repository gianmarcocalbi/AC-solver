from solver import *
from inc.ac3 import *
from inc.ac4 import *
from inc.ac6 import *
from inc.ac2001 import *

if __name__ == "__main__":
    solver = Solver(AC3Constraint)
    solver.addVariable(list(range(0, 10)), "a")
    solver.addVariable(list(range(0, 10)), "b")
    solver.addVariable(list(range(0, 10)), "c")
    solver.addConstraint("a", "b", "a+b>12", "Cab")
    solver.addConstraint("b", "c", "b+c<7", "Cbc")
    solver.filter()
    print(solver.getVariable("a").domain)
    print(solver.getVariable("b").domain)
    print(solver.getVariable("c").domain)

from solver import *
from inc.ac3 import *
from inc.ac4 import *
from inc.ac6 import *
from inc.ac2001 import *

if __name__ == "__main__":

    """
    solver = Solver(AC3Constraint)
    solver.add_variable(list(range(0, 10)), "a")
    solver.add_variable(list(range(0, 10)), "b")
    solver.add_variable(list(range(0, 10)), "c")
    solver.add_constraint("a", "b", "a+b>12", "Cab")
    solver.add_constraint("b", "c", "b+c<7", "Cbc")
    print(solver.solve())
    print(solver.get_variable_by_name("a").domain)
    print(solver.get_variable_by_name("b").domain)
    print(solver.get_variable_by_name("c").domain)
    """
    """
    solver = Solver(AC3Constraint)
    solver.add_variable(list(range(0, 3)), "a")
    solver.add_variable(list(range(0, 3)), "b")
    solver.add_variable(list(range(0, 2)), "c")
    solver.add_constraint("a", "b", "a == b", "Cab")
    solver.add_constraint("b", "c", "b == c", "Cbc")
    print(solver.solve())
    print(solver.get_variable_by_name("a").domain)
    print(solver.get_variable_by_name("b").domain)
    print(solver.get_variable_by_name("c").domain)
    """

    # 8 queens
    solver = Solver(AC3Constraint)
    n = 8
    c = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for i in range(n):
        solver.add_variable(list(range(9)), c[i])

    for i in range(n - 1):
        for j in range(i + 1, n):
            solver.add_constraint(c[i], c[j], c[i] + "!=" + c[j])
            solver.add_constraint(c[i], c[j], c[i] + "!=" + c[j] + "-" + str(j - i))
            solver.add_constraint(c[i], c[j], c[i] + "!=" + c[j] + "+" + str(j - i))

    solution = solver.solve()

    for name in c:
        print("D(" + name + ") = " + str(solver.get_variable_by_name(name).domain))

    print(solution)

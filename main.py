from solver import *
from inc.ac3 import *
from inc.ac4 import *
from inc.ac6 import *
from inc.ac2001 import *

if __name__ == "__main__":

    """
    solver = Solver(AC6Constraint)
    solver.add_variable(list(range(0, 10)), "a")
    solver.add_variable(list(range(0, 10)), "b")
    solver.add_variable(list(range(0, 10)), "c")
    solver.add_constraint("a", "b", "$1+$2>12", "Cab")
    solver.add_constraint("b", "c", "$1+$2<7", "Cbc")
    solver.add_constraint("c", "a", "$1 - $2 > 5", "Cbc")
    print(solver.filter_domains())
    print(solver.get_variable_by_name("a").domain)
    print(solver.get_variable_by_name("b").domain)
    print(solver.get_variable_by_name("c").domain)
    """
    """
    solver = Solver(AC6Constraint)
    solver.add_variable([0,1], "a")
    solver.add_variable([0,1,2], "b")
    solver.add_variable([0,1,2], "c")
    solver.add_constraint("a", "b", "$1 == $2", "Cab")
    solver.add_constraint("b", "c", "$1 == $2", "Cbc")
    print(solver.filter_domains())
    print(solver.get_variable_by_name("a").domain)
    print(solver.get_variable_by_name("b").domain)
    print(solver.get_variable_by_name("c").domain)
    """

    # """
    # 8 queens
    solver = Solver(AC4Constraint)
    n = 4
    c = ["a", "b", "c", "d", "e", "f", "g", "h"]
    # d = {'a': [0], 'b': [4], 'c': [1, 3, 4, 5, 6, 7], 'd': [1, 2, 4, 5, 6, 7], 'e': [1, 2, 3, 5, 6, 7], 'f': [1, 2, 3, 4, 6, 7], 'g': [1, 2, 3, 4, 5, 7], 'h': [1, 2, 3, 4, 5, 6]}
    # d = {'a': [0], 'b': [4], 'c': [1,4], 'd': [5], 'e': [2], 'f': [6], 'g': [1], 'h': [3]}
    d = {'a': [1, 2, 3, 4], 'b': [1, 2, 3, 4], 'c': [0], 'd': [2]}
    for i in range(n):
        # solver.add_variable(list(range(n)), c[i])
        solver.add_variable(d[c[i]], c[i])

    for i in range(n - 1):
        for j in range(i + 1, n):
            solver.add_constraint(c[i], c[j],
                                  "$1 != $2 and $1 != ($2 - " + str(j - i) + ") and $1 != ($2 + " + str(j - i) + ")")

    # solution = solver.simple_solve()
    solution = solver.filter_domains()

    for i in range(n):
        print("D(" + c[i] + ") = " + str(solver.get_variable_by_name(c[i]).domain))

    print(solution)
    # """

import time
from solver import *
from inc.ac3 import *
from inc.ac4 import *
from inc.ac6 import *
from inc.ac2001 import *


def n_queens_problem(algorithm, n):
    solver = Solver(AC2001Constraint)
    n = 24
    v = []
    for i in range(n):
        v.append(solver.add_variable(list(range(n))))

    for i in range(n - 1):
        for j in range(i + 1, n):
            solver.add_constraint(v[i], v[j],
                                  "$1 != $2 and $1 != ($2 - " + str(j - i) + ") and $1 != ($2 + " + str(j - i) + ")")

    return tuple(solver.solve().values())

if __name__ == "__main__":
    t0 = time.time()

    # HERE GOES YOUR CUSTOM CODE

    print(n_queens_problem(AC2001Constraint, 24))  # <- comment this line if you want to use your custom code instead

    print("Elapsed time (sec): " + str(time.time() - t0))

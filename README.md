# AC-solver

# How does it work?
Write your code into `main.py` file 

## 1 - Solver
Create an instance of Solver class passing it a constraint class. This is the moment to choose the Arc Consistency algorithm that the solver will use.
```
solver = Solver(AC3Constraint)
# or
solver = Solver(AC4Constraint)
# or
solver = Solver(AC6Constraint)
# or
solver = Solver(AC2001Constraint)
```

## 2 - Add variables to solver
Add variables using `add_variable` method of solver class described below.

### solver.add_variable(domain, [name])
Takes two arguments:
- **domain**: list of values that the variable can assume
- **name** (optional): a unique name for the variable (_same name for two different variable is not allowed_).

Returns the name assigned to the variable.

#### Example
```
solver.add_variable(list(range(10,20)), "a")
```
creates a variable named "a" whose domain is the list that contains integer values from 10 to 20 (**20 EXCLUDED**).


## 3 - Add constraints to solver
Add binary constraints using on of the following methods:

### solver.add_constraint(x_name, y_name, exp, [name])
Takes three mandatory and one optional arguments:
- **x_name**: unique name of the first variable declared while creating a variable
- **y_name**: unique name of the second variable of the constraint
- **exp**: string expression whose format is described later
- **name** (optional): unique name of the constraint

Returns the name assigned to the constraint.

#### exp format
Must be a STRING formatted as valid Python 3 boolean expression.
Nota Bene:
- address first variable with "$1"
- address second variable with "$2"
- all constants are allowed
- all comparison operator are allowed (>, <, >=, <=, =, !=)
- all arithmetic operators are allowed (+, -, *, /, %)
- all python math function are allowed (e.g. "math.pow()", "math.floor()", etc...)

#### Example
```
solver.add_variable([0,1,2,3,4]), "a")
solver.add_variable([0,1,2,3,4,5,6,7,8]), "b")
solver.add_constraint("a", "b", "$1 == $2", "Cab")

# Cab is the constraint on a and b that is true only 
# when "a" assume a value equal to the value assumed by "b"
```

### solver.add_custom_constraint(x_name, y_name, allowed_values, [name])
Is a second method to create a constraint that differs from the previous one only for an argument: it doesn't take an expression anymore, instead takes a list of pairs of allowed values. For example:
```
solver.add_variable([0,1,2,3,4]), "a")
solver.add_variable([0,1,2,3,4,5,6,7,8]), "b")
solver.add_custom_constraint("a", "b", [(0,0), (1,1)], "Cab")

# Now Cab express a constraint with only two arcs (0,0) and (1,1).
```

## 4 - Solve
There are two different solvers:

### Simple Solver
Solve by calling `solver.simple_solve()`. It returns the first solution found for the problem. An empty object is returned if the problem has no valid solution. Simple solver considers variable in the order in which they are passed to the solver through the `add_variable` method.

Here is a trick to cast the returned object in order to obtain a more human readable output:
```
solution = solver.solve()
print(tuple(solution.values()))
```

### Dynamic Solver
Solve by calling `solver.solve()`. Returns the same as the simple solver. It sort variables considering first the one that has the smallest domain.

### N-Queens problem
There is a method implemented for the N-Queens problem. Use it by calling `n_queens_problem(algorithm, n)` where algorithm is one between the AC classes and n is the integer size of the chessboard.

At the moment, running the `main.py` file as it is, will output the solution for the 24-queens problem with AC2001 algorithm using the Dynamic Solver (it should take about 3 second to find a solution).

### Differences between Simple and Dynamic
Time for computing a solution of 24-Queens Problem with AC2001 and SIMPLE SOLVER is 141 sec, instead using the same algorithm but within the DYNAMIC SOLVER it takes only 3 seconds to solve this problem. Huge improvement.
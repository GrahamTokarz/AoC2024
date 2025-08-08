from ortools.linear_solver import pywraplp

machines = []
cost = 0

#with open('testcase.txt', 'r') as file:
with open('13input.txt', 'r') as file:
    i = 1
    mc = []
    for line in file:
        if (i%4 == 0):
            if i != 0:
                machines.append(mc)
            mc = []
        else:
            ln = line.strip()
            ln = ln.split(", ")
            x = int(ln[0].split("X")[1][1:])
            y = int(ln[1].split("Y")[1][1:])
            mc.append([x, y])
        i += 1

machines.append(mc)
    
def solve_lp(m):
    solver = pywraplp.Solver.CreateSolver('SCIP')

    A = solver.IntVar(0.0, solver.infinity(), 'A')
    B = solver.IntVar(0.0, solver.infinity(), 'B')

    solver.Minimize(3 * A + B)

    offset = 10000000000000 #0 for P1, 10000000000000 for P2

    solver.Add(m[0][0] * A + m[1][0] * B == (offset + m[2][0]))  # Constraint 1
    solver.Add(m[0][1] * A + m[1][1] * B == (offset + m[2][1]))  # Constraint 2

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return int(3*A.solution_value() + B.solution_value())
    else:
        return 0

for m in machines:
    cost += solve_lp(m)

print(f"Number of tokens: {cost}")
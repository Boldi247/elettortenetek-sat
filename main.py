from pysat.formula import CNF
from pysat.solvers import Minisat22

def clauses():
    with open("SAT-test.txt") as f:
        clauses = [line for line in f if not line.startswith('c') and line.strip().endswith('0')]
        print(clauses)
        print(len(clauses) -1)

# Example usage:
if __name__ == "__main__":
    input_str = "5 10 0" 
    clauses()
    cnf = CNF(from_file='SAT-test.txt')
    with Minisat22(bootstrap_with=cnf.clauses) as solver:
        model_count = 0

        while solver.solve():
            model = solver.get_model()
            model_count += 1
            print(f"Model {model_count}: {model}")

            blocking_clause = [-lit if lit > 0 else -lit for lit in model]
            solver.add_clause(blocking_clause)

        if model_count == 0:
            print("No solutions found.")
        else:
            print(f"Total models found: {model_count}")
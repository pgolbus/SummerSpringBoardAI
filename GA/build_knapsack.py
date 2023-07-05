import random
with open("knapsack.txt", "w") as fh:
    fh.write("KNAPSACK = [")
    for _ in range(10):
        fh.write(f"({random.randint(1,9)}, {random.randint(9,99)}),")
    fh.write("]")
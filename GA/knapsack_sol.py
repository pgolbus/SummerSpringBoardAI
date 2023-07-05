import random

from ga import GA

# Genetic Algorithm parameters
POPULATION_SIZE = 10
MUTATION_RATE = 0.01
GENERATIONS = 100
CROSSOVER_RATE = 0.7

MAX_WEIGHT = 15


def generate_knapsack(size=100, minweight=1, maxweight=10, minvalue=9, maxvalue=99):
    knapsack = []
    for _ in range(size):
        weight = random.randint(minweight, maxweight)
        value = random.randint(minvalue, maxvalue)
        knapsack.append((weight, value))
    return knapsack

class KnapsackGA(GA):

    def __init__(self, knapsack):
        self.knapsack = knapsack

    # Function to generate a random bitstring
    def generate(self, **kwargs):
        return [random.choice([0, 1]) for _ in range(len(self.knapsack))]

    # Function to calculate the fitness of a bitstring
    def calculate_fitness(self, bitstring, max_weight=None, **kwargs):
        total_weight = 0
        total_value = 0
        for i in range(len(self.knapsack)):
            if bitstring[i] == 1:
                total_weight += self.knapsack[i][0]
                total_value += self.knapsack[i][1]
        if total_weight > max_weight:
            total_value = 0  # Penalize solutions exceeding the weight limit
        return total_value        

if __name__ == "__main__":
    knapsack = generate_knapsack(10)
    print(knapsack)
    ga_runner = KnapsackGA(knapsack)
    ga_runner.select(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, CROSSOVER_RATE, max_weight=MAX_WEIGHT, print_res=True)

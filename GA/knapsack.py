import random

from ga import GA

# Genetic Algorithm parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000
MAX_WEIGHT = 15

# List of items [weight, value]
KNAPSACK = [
    [2, 6],
    [2, 10],
    [3, 12],
    [4, 15],
    [5, 16]
]

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

    # Function to perform mutation on a bitstring
    def mutate(self, bitstring, mutation_rate, **kwargs):
        for i in range(len(bitstring)):
            if random.random() < mutation_rate:
                bitstring[i] = random.choice([0, 1])

if __name__ == "__main__":
    # Run the genetic algorithm= 
    ga_runner = KnapsackGA(KNAPSACK)
    print(ga_runner.genetic_algorithm(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, max_weight=MAX_WEIGHT, print_res=True))

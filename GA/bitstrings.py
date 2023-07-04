import random

from ga import GA

# Genetic Algorithm parameters
POPULATION_SIZE = 1000
MUTATION_RATE = 0.01
GENERATIONS = 1000
CROSSOVER_RATE = 0.7

LENGTH = 32

class BitstringGA(GA):

    # Function to generate a random bitstring
    def generate(self, length=None, **kwargs):
        return [random.choice([0, 1]) for _ in range(length)]

    # Function to calculate the fitness of a bitstring
    def calculate_fitness(self, bitstring, **kwargs):
        return sum(bitstring)

if __name__ == "__main__":
    # Run the genetic algorithm
    ga_runner = BitstringGA()
    ga_runner.select(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, CROSSOVER_RATE, success_score=LENGTH, print_res=True, length=LENGTH)

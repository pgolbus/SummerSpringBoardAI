import random

from ga import GA

# Genetic Algorithm parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000
LENGTH = 16

class BitstringGA(GA):

    # Function to generate a random bitstring
    def generate(self, length=None, **kwargs):
        return [random.choice([0, 1]) for _ in range(length)]

    # Function to calculate the fitness of a bitstring
    def calculate_fitness(self, bitstring, **kwargs):
        return sum(bitstring)

    # Function to perform mutation on a bitstring
    def mutate(self, bitstring, mutation_rate, **kwargs):
        for i in range(len(bitstring)):
            if random.random() < mutation_rate:
                bitstring[i] = random.choice([0, 1])

if __name__ == "__main__":
    # Run the genetic algorithm
    ga_runner = BitstringGA()
    print(ga_runner.genetic_algorithm(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, success_score=LENGTH, print_res=True, length=LENGTH))

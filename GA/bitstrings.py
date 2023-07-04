import random

# Genetic Algorithm parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000
LENGTH = 16

# Function to generate a random bitstring
def generate_bitstring(length):
    return [random.choice([0, 1]) for _ in range(length)]

# Function to calculate the fitness of a bitstring
def calculate_fitness(bitstring):
    return sum(bitstring)

# Function to perform mutation on a bitstring
def mutate_bitstring(bitstring, mutation_rate):
    for i in range(len(bitstring)):
        if random.random() < mutation_rate:
            bitstring[i] = random.choice([0, 1])

# Function to perform crossover between two parent bitstrings
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to select parents for reproduction using tournament selection
def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

# Genetic Algorithm
def genetic_algorithm(generations, population_size, mutation_rate, length, print_res = False):
    # Create initial population
    population = [generate_bitstring(length) for _ in range(population_size)]
    max_score = float("-inf")
    best_scores = []

    for generation in range(generations):
        # Calculate fitness for each individual in the population
        fitness_scores = [calculate_fitness(bitstring) for bitstring in population]

        best_score = max(fitness_scores)
        max_score = max(max_score, best_score)
        best_scores.append(best_score)
        best = population[fitness_scores.index(best_score)]
        if print_res:
            print(f"Generation {generation + 1}: {best} {best_score}")

        # Check if a solution is found
        if length in fitness_scores:
            if print_res:
                print("Solution found in generation", generation)
            return best_scores

        # Create a new population through selection, crossover, and mutation
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            mutate_bitstring(child1, mutation_rate)
            mutate_bitstring(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    if print_res:
        print(f"Solution not found. Max score: {max_score}")
    return best_scores

if __name__ == "__main__":
    # Run the genetic algorithm
    print(genetic_algorithm(GENERATIONS, POPULATION_SIZE, MUTATION_RATE, LENGTH, True))

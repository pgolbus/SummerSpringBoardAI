import random


class GA:

    def generate(self, **kwargs):
        pass

    def calculate_fitness(self, **kwargs):
        pass

    # Function to perform crossover between two parent bitstrings
    def crossover(self, parent1, parent2, crossover_rate):
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, len(parent1) - 1)
            child1 = parent1[:crossover_point] + parent2[crossover_point:]
            child2 = parent2[:crossover_point] + parent1[crossover_point:]
            return child1, child2
        return parent1, parent2

    # Function to select parents for reproduction using tournament selection
    def select_parents(self, population, fitness_scores):
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]
        return parent1, parent2

    # Function to perform mutation on a bitstring
    def mutate(self, bitstring, mutation_rate):
        for i in range(len(bitstring)):
            if random.random() < mutation_rate:
                bitstring[i] = random.choice([0, 1])

    # Genetic Algorithm
    def genetic_algorithm(self, generations, population_size, mutation_rate, crossover_rate, success_score=None, print_res=False, **kwargs):
        # Create initial population
        population = [self.generate(**kwargs) for _ in range(population_size)]
        max_score = float("-inf")
        best_scores = []

        for generation in range(generations):
            # Calculate fitness for each individual in the population
            fitness_scores = [self.calculate_fitness(individual, **kwargs) for individual in population]

            best_score = max(fitness_scores)
            # if the score went down, we want to keep the old population
            if best_score > max_score:
                max_score = best_score
            else:
                population = old_population
                fitness_scores = [self.calculate_fitness(individual, **kwargs) for individual in population]
            best_scores.append(max_score)
            if print_res:
                print(f"Generation {generation + 1}: {max_score}")

            # Check if a solution is found
            if success_score is not None and success_score in fitness_scores:
                if print_res:
                    print("Solution found in generation", generation)
                return best_scores

            # Create a new population through selection, crossover, and mutation
            new_population = []
            # we're going to select two individuals once per half the size the of the population
            # the strongest are most likely to breed or just move on to the next generation
            for _ in range(population_size // 2):
                parent1, parent2 = self.select_parents(population, fitness_scores)
                child1, child2 = self.crossover(parent1, parent2, crossover_rate)
                self.mutate(child1, mutation_rate)
                self.mutate(child2, mutation_rate)
                new_population.append(child1)
                new_population.append(child2)

            old_population = population
            population = new_population

        if print_res:
            if success_score is not None:
                print(f"Solution not found. Max score: {max_score}")
            else:
                print(f"Max score: {max_score}")
        return best_scores
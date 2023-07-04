import random


class GA:

    def generate(self, **kwargs):
        pass

    def calculate_fitness(self, **kwargs):
        pass

    def crossover(self, **kwargs):
        pass

    def mutate(self, **kwargs):
        pass

    # Function to select parents for reproduction using tournament selection
    def select_parents(self, population):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        return parent1, parent2

    # Genetic Algorithm
    def genetic_algorithm(self, generations, population_size, mutation_rate, success_score, print_res=False, **kwargs):
        # Create initial population
        population = [self.generate(**kwargs) for _ in range(population_size)]
        max_score = float("-inf")
        best_scores = []

        for generation in range(generations):
            # Calculate fitness for each individual in the population
            fitness_scores = [self.calculate_fitness(individual, **kwargs) for individual in population]

            best_score = max(fitness_scores)
            max_score = max(max_score, best_score)
            best_scores.append(best_score)
            best = population[fitness_scores.index(best_score)]
            if print_res:
                print(f"Generation {generation + 1}: {best} {best_score}")

            # Check if a solution is found
            if success_score in fitness_scores:
                if print_res:
                    print("Solution found in generation", generation)
                return best_scores

            # Create a new population through selection, crossover, and mutation
            new_population = []
            for _ in range(population_size // 2):
                parent1, parent2 = self.select_parents(population)
                child1, child2 = self.crossover(parent1, parent2, **kwargs)
                self.mutate(child1, mutation_rate, **kwargs)
                self.mutate(child2, mutation_rate, **kwargs)
                new_population.append(child1)
                new_population.append(child2)

            population = new_population

        if print_res:
            print(f"Solution not found. Max score: {max_score}")
        return best_scores
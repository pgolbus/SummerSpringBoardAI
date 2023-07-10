import random
import sys

import click
import numpy as np

from ga import GA


POPULATION_SIZE = 10
KNAPSACK_SIZE = 100
MINWEIGHT = 1
MAXWEIGHT = 10
MINVALUE = 9
MAXVALUE = 99
MAX_WEIGHT = 500
GENERATIONS = 25
RUNS = 100


def generate_knapsack(knapsack_size, minweight, maxweight, minvalue, maxvalue):
    knapsack = []
    for _ in range(knapsack_size):
        weight = random.randint(minweight, maxweight)
        value = random.randint(minvalue, maxvalue)
        knapsack.append((weight, value))
    return knapsack

class KnapsackGA(GA):

    def __init__(self, population_size, generations, runs, knapsack, max_weight, **kwargs):
        super().__init__(population_size, generations, **kwargs)
        self.runs = runs
        self.knapsack = knapsack
        self.max_weight = max_weight

    # Function to generate a random bitstring
    def generate(self, **kwargs):
        return [random.choice([0, 1]) for _ in range(len(self.knapsack))]

    # Function to calculate the fitness of a bitstring
    def calculate_fitness(self, bitstring, **kwargs):
        total_weight = 0
        total_value = 0
        for i in range(len(self.knapsack)):
            if bitstring[i] == 1:
                total_weight += self.knapsack[i][0]
                total_value += self.knapsack[i][1]
        # remember that if it's too heavy, it cannot "survive"
        if total_weight > self.max_weight:
            total_value = 0  # Exclude solutions exceeding the weight limit
        return total_value

@click.command()
@click.option('--population-size', default=POPULATION_SIZE, help='Population size')
@click.option('--max-weight', default=MAX_WEIGHT, help='Max backpack weight')
@click.option('--generations', default=GENERATIONS, help='Generations')
@click.option('--runs', default=RUNS, help='Runs')
@click.option('--knapsack-size', default=KNAPSACK_SIZE, help='Knapsack size')
@click.option('--min-item-weight', default=MINWEIGHT, help='Min item weight')
@click.option('--max-item-weight', default=MAXWEIGHT, help='Max item weight')
@click.option('--min-item-value', default=MINVALUE, help='Min value')
@click.option('--max-item-value', default=MAXVALUE, help='Max value')
def main(population_size, max_weight, generations, runs, knapsack_size, min_item_weight, max_item_weight, min_item_value, max_item_value):
    knapsack = generate_knapsack(knapsack_size, min_item_weight, max_item_weight, min_item_value, max_item_value)
    runner = KnapsackGA(population_size, generations, runs, knapsack, max_weight)
    while True:
        print('Input "crossover_rate, mutation_rate" separated by comma, "n" for a new backpack or "q" to quit')
        input = sys.stdin.readline().strip()
        if not input or input == 'q':
            break
        if input == 'n':
            knapsack = generate_knapsack(knapsack_size, min_item_weight, max_item_weight, min_item_value, max_item_value)
            print("\n\n")
            continue
        params = input.split(', ')
        if len(params) == 1:
            params = input.split(',')
        params = [float(p) for p in params]
        results = [runner.select(*params) for _ in range(RUNS)]
        print(f"Crossover rate: {params[0]}, Mutation rate: {params[1]}\nScore: {np.mean(results)}\n\n")


if __name__ == '__main__':
    main()
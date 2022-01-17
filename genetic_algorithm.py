import math

from sample import Sample
from chart import Chart
from converters import Converters
import numpy as np
import random
import copy
import math


class GeneticAlgorithm:
    population = []

    def __init__(self, population_size, chromosome_size, scope_range, tournament_size, mutation, if_generate_chart=True):
        self.population_size = population_size
        self.chromosome_size = chromosome_size
        self.scope_range = scope_range
        self.scope = np.linspace(scope_range[0], scope_range[1], 100)
        self.tournament_size = tournament_size
        self.mutation = mutation
        self.generate_population()
        self.generate_chart = if_generate_chart

    def evolve(self, iterations):
        for i in range(iterations):
            parents_count, child_count = (math.floor(self.population_size / 2) - 1, math.ceil(self.population_size / 2))
            new_parents = []
            offspring = []
            best_sample = self.hot_deck(self.population)
            new_parents.append(best_sample)
            self.population.remove(best_sample)
            for _ in range(parents_count):
                winner = self.do_tournament(self.population)
                new_parents.append(winner)

            for _ in range(child_count):
                parent1, parent2 = random.sample(new_parents, 2)
                new_child = self.crossover_one_point(parent1, parent2)
                if "single_bit_mutation" in self.mutation:
                    new_child.single_bit_mutation()
                if "swap_bit_mutation" in self.mutation:
                    new_child.swap_bit_mutation()
                if "reverse_mutation" in self.mutation:
                    new_child.reverse_mutation()
                offspring.append(new_child)
            self.population = new_parents + offspring
            if self.generate_chart:
                self.show_chart(new_parents, offspring, best_sample, i)
        return best_sample.get_value()

    def generate_population(self):
        for i in range(self.population_size):
            max_value = 2 ** self.chromosome_size - 1
            x = random.randrange(0, max_value)
            y = random.randrange(0, max_value)
            new_sample = Sample(self.scope_range, Converters.dec_to_gray(x, self.chromosome_size),
                                Converters.dec_to_gray(y, self.chromosome_size))
            self.population.append(new_sample)

    def do_tournament(self, generation):
        new_tournament = random.choices(generation, k=self.tournament_size)
        winner = self.hot_deck(new_tournament)
        generation.remove(winner)
        return copy.deepcopy(winner)

    def hot_deck(self, population):
        hot_deck = population[0]
        for i in population:
            if i.get_value() < hot_deck.get_value():
                hot_deck = i
        return hot_deck

    def crossover_one_point(self, parent1, parent2):
        bit_size = self.chromosome_size
        cross_point = random.randrange(0, bit_size)
        chromosome_x_1, chromosome_y_1 = parent1.get_chromosomes()
        chromosome_x_2, chromosome_y_2 = parent2.get_chromosomes()
        new_chromosome_x = f"{chromosome_x_1[:cross_point]}{chromosome_x_2[cross_point:]}"
        new_chromosome_y = f"{chromosome_y_1[:cross_point]}{chromosome_y_2[cross_point:]}"

        new_sample = Sample(self.scope_range, new_chromosome_x, new_chromosome_y)
        return new_sample

    def show_chart(self, parents, children, best_sample, generation):
        chart = Chart((1, 1))
        chart.clear_axes()
        chart.title(f"Generation: {generation}")
        x1, x2 = np.meshgrid(self.scope, self.scope)
        y = np.power(x1, 2) + x1 * x2 + 2 * x1 + np.power(x2, 2)
        contour = chart.ax.contour(x1, x2, y)
        chart.ax.clabel(contour, inline=True)
        c1 = []
        c2 = []
        for parent in parents:
            a, b = parent.get_coordinates()
            c1.append(a)
            c2.append(b)
        chart.draw_many_points(c1, c2, color='b', name='parents', size=60)
        c1.clear()
        c2.clear()
        for child in children:
            a, b = child.get_coordinates()
            c1.append(a)
            c2.append(b)
        chart.draw_many_points(c1, c2, color='r', name='children')
        x, y = best_sample.get_coordinates()
        chart.draw_point(x, y, color="g", name='best sample')
        chart.save_frame(generation)
        chart.create_gif(generation)

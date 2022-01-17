import math
import random
from typing import Tuple
from converters import Converters


class Sample:

    def __init__(self, scope_range: Tuple[int, int], x: str, y: str):
        self.x_chromosome = x
        self.y_chromosome = y
        self.scope_range = scope_range


    def calculate_value(self):
        x, y = self.get_coordinates()
        return math.pow(x, 2) + x * y + 2*x + math.pow(y, 2)

    def get_coordinates(self):
        dec_x = Converters.gray_to_dec(self.x_chromosome)
        dec_y = Converters.gray_to_dec(self.y_chromosome)
        max_value = (2 ** len(self.x_chromosome)) -1
        x = (((dec_x - 0) * (self.scope_range[1] - self.scope_range[0])) / (max_value - 0)) + self.scope_range[0]
        y = (((dec_y - 0) * (self.scope_range[1] - self.scope_range[0])) / (max_value - 0)) + self.scope_range[0]
        return x, y

    def get_value(self):
        return self.calculate_value()

    def get_chromosomes(self):
        return self.x_chromosome, self.y_chromosome


    def single_bit_mutation(self):
        random_x_bit = random.randrange(0, len(self.x_chromosome))
        random_y_bit = random.randrange(0, len(self.x_chromosome))
        self.x_chromosome = self.reverse_bit(self.x_chromosome, random_x_bit)
        self.y_chromosome = self.reverse_bit(self.y_chromosome, random_y_bit)

    def swap_bit_mutation(self):
        selected_x = self.choose_bits(self.x_chromosome)
        selected_y = self.choose_bits(self.y_chromosome)
        self.x_chromosome = self.swap_bit(selected_x[0], selected_x[1], self.x_chromosome)
        self.y_chromosome = self.swap_bit(selected_y[0], selected_y[1], self.y_chromosome)

    def swap_bit(self, index1, index2, chromosome):
        bit1 = chromosome[index1]
        bit2 = chromosome[index2]
        selected = [index1, index2]
        selected.sort()
        return f"{chromosome[:selected[0]]}{bit2}{chromosome[selected[0]+1:selected[1]]}{bit1}{chromosome[selected[1]+1:]}"

    def reverse_bit(self, chromosome, bit):
        if chromosome[bit] == 1:
            new_gen = 0
        else:
            new_gen = 1
        return f"{chromosome[:bit]}{new_gen}{chromosome[bit+1:]}"

    def reverse_mutation(self):
        selected_x = self.choose_bits(self.x_chromosome)
        selected_y = self.choose_bits(self.y_chromosome)
        self.x_chromosome = self.reverse_bits(self.x_chromosome, selected_x[0], selected_x[1])
        self.y_chromosome = self.reverse_bits(self.y_chromosome, selected_y[0], selected_y[1])

    def choose_bits(self, chromosome):
        random_x1_bit = 0
        random_x2_bit = 0
        while random_x1_bit == random_x2_bit:
            random_x1_bit = random.randrange(0, len(chromosome))
            random_x2_bit = random.randrange(0, len(chromosome))
        selected = [random_x1_bit, random_x2_bit]
        selected.sort()
        return selected

    def reverse_bits(self, chromosome, index1, index2):
        old_gens = []
        for i in chromosome[index1:index2]:
            old_gens.append(i)
        old_gens.reverse()
        new_gens = ''
        for i in old_gens:
            new_gens += i
        return f"{chromosome[:index1]}{new_gens}{chromosome[index2:]}"

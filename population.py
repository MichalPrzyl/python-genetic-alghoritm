from sample import Sample
import math
import json
import logging
from settings import SIZE_OF_POPULATION, SIZE_OF_BEST_SQUAD,\
    BESTER_MULTIPLIER, LOGGING_AVERAGE_OF_POPULATION, \
    LOGING_CHANGE_NUMBER, FIXED_INITIAL_POPULATION,\
    PRECISION
from utils import show_queryset_values


class Population:
    
    def __init__(self, best_squad=None, iteration=0):
        self.population = []
        self.iteration = iteration

        if best_squad:
            self.__create_next_iteration_generation(best_squad)
        else:
            self.__create_initial_population()

    def __create_initial_population(self):
        if FIXED_INITIAL_POPULATION:
            self.__create_fixed_initial_population()
        else:
            for _ in range(SIZE_OF_POPULATION):
                sample = Sample()
                self.population.append(sample)

    def __create_fixed_initial_population(self):
        with open("fixed_initial_population.json", 'r') as json_file:
            input_data = json.load(json_file)
            for number in input_data:
                sample = Sample(number)
                self.population.append(sample)


    def __create_next_iteration_generation(self, best_squad):
        for bester in best_squad:
            for _ in range(BESTER_MULTIPLIER):
                sample = Sample(bester.number)
                if sample.is_mutation_occured():
                    sample.mutate()
                self.population.append(sample)

    def get_population(self):
        return sorted(list(map(lambda x: x.number, self.population)))

    def show_population(self):
        print(sorted(list(map(lambda x: x.number, self.population))))

    def show_population_set(self):
        print(set(sorted(list(map(lambda x: x.number, self.population)))))

    def get_population_average(self):
        values = list(map(lambda x: x.number, self.population))
        average = sum(values) / len(self.population)
        return round(average, PRECISION)

    def get_best_squad(self):
        values = list(map(lambda x: x.number, self.population))
        best_squad = sorted(
            self.population, key=lambda x: x.points)[:SIZE_OF_BEST_SQUAD]

        return best_squad

    def get_best_squad_values(self):
        best_squad = sorted(
            self.population, key=lambda x: x.points)[:SIZE_OF_BEST_SQUAD]
        values = list(map(lambda x: x.number, best_squad))
        return values

    def get_points(self):
        xd = list(map(lambda x: {'number': x.number, 'points': x.points}, self.population))
        return xd

from settings import *
from population import Population
import logging
from utils import show_queryset_values

def create_generation(best_squad=None, iterator=0):
    iterator += 1
    if iterator > MAX_RECURSION_ITERATIONS:
        raise ValueError("iterion too much")
    population = Population(best_squad or None)
    best_squad = population.get_best_squad()[:]
    handle_logging(population)
    create_generation(best_squad, iterator)


def handle_logging(population):
    if LOGGING_AVERAGE_OF_POPULATION:
        logging.info(population.get_population_average())
    if LOGGING_WHOLE_POPULATION_AFTER_EACH_ITERATION:
        logging.info(population.get_population())
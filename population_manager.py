from settings import *
from population import Population
import logging
from utils import show_queryset_values

def create_generation(best_squad=None, iterator=0):
    iterator += 1
    # print(f"iteration: {iterator}")
    if iterator > MAX_RECURSION_ITERATIONS:
        raise ValueError("iterion too much")
    population = Population(best_squad or None)
    # population.show_population_average()
    best_squad = population.get_best_squad()[:]
    #logging.info(show_queryset_values(best_squad))
    if LOGGING_AVERAGE_OF_POPULATION:
        logging.info(population.get_population_average())
    create_generation(best_squad, iterator)
from settings import *
from population import Population
import logging
from utils import show_queryset_values

def create_generation(best_squad=None, iterator=0):
    iterator += 1
    if iterator > MAX_RECURSION_ITERATIONS:
        logging.info(
            f"LAST AVERAGE OF BEST_SQUAD: {round(sum(list(map(lambda x: x.number, best_squad)))/len(best_squad), PRECISION)}")
        raise ValueError("iterion too much")
    population = Population(best_squad or None, iterator)
    best_squad = population.get_best_squad()[:]
    handle_logging(population)
    create_generation(best_squad, iterator)


def handle_logging(population):
    if LOGGING_AVERAGE_OF_POPULATION:
        logging.info(f"iteration: {population.iteration}, average: {population.get_population_average()}")
    if LOGGING_WHOLE_POPULATION_AFTER_EACH_ITERATION:
        logging.info(population.get_population())
    if LOGGIN_BEST_SQUAD:
        logging.info('best_squad:')
        logging.info(population.get_best_squad_values())
    if LOGGIN_POPULATION_POINTS:
        logging.info('points:')
        logging.info(population.get_points())

    if any([LOGGING_AVERAGE_OF_POPULATION,
            LOGGING_WHOLE_POPULATION_AFTER_EACH_ITERATION,
            LOGGIN_BEST_SQUAD,
            LOGGIN_POPULATION_POINTS]):
        #logging.info('============================')
        pass

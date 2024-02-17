import random
import math

from settings import *

from population import Population 

from utils import show_queryset_values, create_generation

import logging


def main():
    logging.basicConfig(filename='logs.log',level=logging.DEBUG, filemode = 'w', format='%(process)d-%(levelname)s-%(message)s') 

    create_generation(None, 0)
    print(30 * "=")
    # population = Population()
    # print(f"population set:")
    # population.show_population_set()
    # print(f"population average:")
    # population.show_population_average()
    # best_10 = population.get_best_10()[:]

    # print(30*'=')

    # population2 = Population(best_10)
    # print(f"population2 set:")
    # population2.show_population_set()
    # print(f"population2 average:")
    # population2.show_population_average()
    # best_10_2 = population2.get_best_10()[:]

    # print(30*'=')

    # population3 = Population(best_10_2)
    # print(f"population3 set:")
    # population3.show_population_set()
    # print(f"population3 average:")
    # population3.show_population_average()
    # best_10_3 = population3.get_best_10()[:]

    # print(30*'=')

    # population4 = Population(best_10_3)
    # print(f"population4 set:")
    # population4.show_population_set()
    # print(f"population4 average:")
    # population4.show_population_average()
    # best_10_4 = population4.get_best_10()[:]

    # for generation in range(5):

    #     population = Population()
    #     print(f"population set:")
    #     population.show_population_set()
    #     print(f"population average:")
    #     population.show_population_average()
    #     best_10 = population.get_best_10()[:]

    #     population2 = Population(best_10)


    # population2 = Population(best_10)
    # print(f"population2 set:")
    # population2.show_population_set()
    # print(f"population2 average:")
    # population2.show_population_average()
    # best_10_2 = population2.get_best_10()[:]


if __name__ == "__main__":
    main()


from settings import *
from population import Population


def show_queryset_values(objs):
    values = list(map(lambda x: x.number, objs))
    print(values)


def create_generation(best_10=None, iterator=0):
    iterator += 1
    # print(f"iteration: {iterator}")
    if iterator > MAX_RECURSION_ITERATIONS:
        raise ValueError("iterion too much")
    population = Population(best_10 or None)
    # population.show_population_average()
    best_10 = population.get_best_10()[:]
    show_queryset_values(best_10)
    # print(f"best_10: {best_10}")
    create_generation(best_10, iterator)
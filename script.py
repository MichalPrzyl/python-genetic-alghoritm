import random
import math
# ewolution alghoritm
# game dinosaur


# but this stupid test first
WINNER = 69
MIN = 0
MAX = 1000
PROBABILTY_OF_MUTATION = 20  # %
MUTATION_APLITUDE = 2
MAX_RECURSION_ITERATIONS = 100


class Sample:
    def __init__(self, number=None):
        # print(f"number: {number}")
        # assert isinstance(number, int or None), ('Number arg is not a numvber')
        # if number:
        #     if not isinstance(number, float):
        #         raise ValueError('Number arg is not a numvber')
        self.number = number or self.get_random_number()
        self.points = abs(self.number - WINNER)

    def get_random_number(self):
        return random.randrange(MIN, MAX)

    def is_mutation_occured(self):
        if not random.randrange(0, 101) > PROBABILTY_OF_MUTATION:
            # print(f"muttaion occured2")
            return True
        # print("nonono")
        return False

    def mutate(self):
        if random.randrange(0, 101) > 50:
            # self.number -= random.randrange(0, MUTATION_APLITUDE)
            self.number -= random.uniform(0.0, MUTATION_APLITUDE)
        else:
            # self.number += random.randrange(0, MUTATION_APLITUDE)
            self.number += random.uniform(0.0, MUTATION_APLITUDE)


class Population:
    def __init__(self, best_10=None):
        self.population = []

        if best_10:
            for bester in best_10:
                for _ in range(math.floor(100 / len(best_10))):
                    sample = Sample(bester.number)
                    if sample.is_mutation_occured():
                        sample.mutate()
                    self.population.append(sample)
        else:
            for _ in range(100):
                sample = Sample()
                self.population.append(sample)

    def get_population(self):
        return sorted(list(map(lambda x: x.number, self.population)))

    def show_population(self):
        print(sorted(list(map(lambda x: x.number, self.population))))

    def show_population_set(self):
        print(set(sorted(list(map(lambda x: x.number, self.population)))))

    def show_population_average(self):
        values = list(map(lambda x: x.number, self.population))
        average = sum(values) / len(self.population)
        print(f"average: {average}")

    def get_best_10(self):
        values = list(map(lambda x: x.number, self.population))
        # best_10 = list(filter(lambda x: abs(x-WINNER) <= 0.02 * (MAX-MIN), values))
        best_10 = sorted(self.population, key=lambda x: x.points)[:10]
        # print(f"best_10: {list(map(lambda x: x.number, best_10))}")

        return best_10  # I know it's not 10


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


def main():
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

    create_generation(None, 0)
    print(30 * "=")

    # population2 = Population(best_10)
    # print(f"population2 set:")
    # population2.show_population_set()
    # print(f"population2 average:")
    # population2.show_population_average()
    # best_10_2 = population2.get_best_10()[:]


if __name__ == "__main__":
    main()

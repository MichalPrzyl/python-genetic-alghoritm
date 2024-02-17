from sample import Sample
import math


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

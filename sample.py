import random
from settings import *
import logging


class Sample:
    def __init__(self, number=None):
        self.number = number or self.get_random_number()
        self.points = self.calculate_sample_points()

    def get_random_number(self):
        return random.randrange(MIN, MAX)

    def is_mutation_occured(self):
        if not random.randrange(0, 101) > PROBABILTY_OF_MUTATION:
            return True
        return False

    def calculate_sample_points(self):
        return round(abs(self.number - WINNER), PRECISION)

    def set_points_based_on_number(self):
        self.points = self.calculate_sample_points()

    def mutate(self):
        random_value = round(random.uniform(0.0, MUTATION_APLITUDE), PRECISION)
        if LOGING_CHANGE_NUMBER:
            logging.info(random_value)
        if random.randrange(0, 101) > 50:
            self.number = round(self.number - random_value, PRECISION)
        else:
            self.number = round(self.number + random_value, PRECISION)
        
        self.set_points_based_on_number()
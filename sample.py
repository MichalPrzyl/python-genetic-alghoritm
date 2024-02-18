import random

from settings import *

import logging


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
        random_value = random.uniform(0.0, MUTATION_APLITUDE)
        if LOGING_CHANGE_NUMBER:
            logging.info(random_value)
        if random.randrange(0, 101) > 50:
            self.number -= random_value
        else:
            self.number += random_value

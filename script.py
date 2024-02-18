import random
import math

from settings import *
import sys
sys.setrecursionlimit(500000)

from utils import show_queryset_values

import logging

from population_manager import create_generation



def main():
    logging.basicConfig(filename='logs.log',level=logging.DEBUG, filemode = 'w', format='%(process)d-%(levelname)s-%(message)s') 

    create_generation(None, 0)

if __name__ == "__main__":
    main()

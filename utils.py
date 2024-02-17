
from settings import *

import logging


def show_queryset_values(objs):
    values = list(map(lambda x: x.number, objs))
    return values



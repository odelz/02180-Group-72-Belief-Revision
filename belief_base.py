import math
import logging

class belief_base:
    def __init__(self):
        self.beliefs = []
        self.reorder_queue = []


class belief:
    def __init__(self, formula, order=None):
        self.formula = formula
        self.order = order

    def __lessthan__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order and self.formula == other.formula

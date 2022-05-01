from audioop import add
import math
from operator import neg
from pickle import TRUE

from entailment import entails
from utils import associate

from sympy.logic.boolalg import *
from sortedcontainers import SortedList

def validate_order(x):
    #################################
    #   Ensures that the order      #
    #   is betwen 0 and 100         #
    #################################
    if not(0 <= x <= 100):
        raise ValueError


class BeliefBase:
    def __init__(self):
        self.beliefs = SortedList(key=lambda b: neg(b.order))
        self.count = 0

    #Note: Call appropriate method directly
    def __remove_belief__(self, formula):
        self.beliefs.remove(formula)          
            
    def __modify_belief__(self, updated_belief):
        for x in self.beliefs:
            if x.formula == updated_belief.formula:
                self.beliefs.remove(x)
                self.beliefs.add(updated_belief)
        
    def add(self, formula, order):
        #formula = to_cnf(formula)
        validate_order(order)
        
        belief = Belief(formula, order)
        self.beliefs.add(belief)

    def find_max_order(self, formula):
        return self.beliefs(0)

    def print_beliefs(self):
        for x in self.beliefs:
            print(x.formula, x.order)

    def reviseAlternative(self, formula, order):
        form = to_cnf(formula)
        for x in self.beliefs:
            if x.order == order:
                self.beliefs.remove(x)
                temp = form.__or__(x.formula)
                temp = to_cnf(temp)
                self.add(temp.simplify(), order)
            else:
                self.add(form,order)
        if self.beliefs.__len__() == 0:
            self.add(form,order)


class Belief:
    def __init__(self,formula, order = None):
        self.formula = formula
        self.order = order

    def __lessThan__(self, other):
        return self.order < other.order

    def __equals__(self, other):
        return self.order == other.order and self.formula == other.formula

    def __represents__(self):
        return f'Belief({self.formula}, order={self.order})'

    

def isclose(a,b):
    """
    Checks approximate equality of 
    """
    return math.isclose(a,b)

from audioop import add
import math
from operator import neg
from pickle import TRUE

from logic_entailment import entails
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
        for belief in self.beliefs:
            if belief.formula == formula:
                belief.order = 0          
        
    def expand(self, formula, order):
        formula = to_cnf(formula)
        validate_order(order)
        for x in self.beliefs:
            if x.formula == formula:
                return "Formula already exists"
                
        if order > 0:
            belief = Belief(formula, order)
            self.beliefs.add(belief)
            return "Formula added"

    def find_max_order(self, formula):
        return self.beliefs(0)

    def print_beliefs(self):
        for x in self.beliefs:
            print(x.formula, x.order)

    def reviseAlternative(self, formula, order):
        form = to_cnf(formula)
        for x in self.beliefs:
            if x.formula == formula:
                self.beliefs.remove(x)
                #temp = form.__or__(x.formula)
                #temp = to_cnf(temp)
                self.expand(form, order)
                return "Revision complete"
        return "No such formula exists"
                
    def contraction(self,formula):
        for x in self.beliefs:
            if x.formula == formula:
                self.beliefs.remove(x)

       

    def clear(self):
        self.beliefs.clear()
    

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

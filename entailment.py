from sympy.logic.boolalg import to_cnf, Or
from utils import (
    conjuncts, disjuncts,
    unique, removeall,
    associate,
)

def entails (beliefs, formula):
    # begin by converting CNF
    cnf_formula = to_cnf(formula)

    # resolution only works on clauses. 
    # conjunctive normal form(CNF): is a conjunction of clauses

    clauses = []
    for belief in beliefs: 
        clauses += belief
    
    # Recall that both testing for entailment and contradiction
    # boil down to checking satisfiability
    # Resolution can be used to do this very thing. If we ever apply a resolution rule (e.g., to premises A and ¬A)
    # and get false, which is clearly a contradiction, then the set of formulas in the knowledge base is unsatisfiable. 
    # If we are unable to derive false, that means the knowledge base is satisfiable because resolution is complete.
    # However, unlike in model checking, we don’t actually produce a concrete model that satisfies the KB.
    clauses += conjuncts(to_cnf(~formula))

    if False in clauses: 
        return True
    
    #while True:



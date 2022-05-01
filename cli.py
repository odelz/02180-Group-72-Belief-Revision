import argparse
import logging

from sympy import to_cnf, SympifyError

from belief_base1 import BeliefBase



PROMPT = ">>> "

def print_help():
    print(
f"""Available actions:
e: Belief expansion
r: Belief revision
c: Belief contraction
d: Delete Belief base
p: Print belief base
q: Quit
"""
    )


def handle_input(bb):
    print_help()
    print('Select action:')
    action = input(PROMPT)
    action = action.lower()

    if action == 'r':
        print('--- Revision ---')
        print('Enter a formula:')
        frm = input(PROMPT)
        try:
            frm = to_cnf(frm)
            print('Select order (real number from 0 to 100):')
            order = input(PROMPT)
            bb.reviseAlternative(frm, int(order))
        except SympifyError:
            print('Invalid formula')
        except ValueError:
            print('Order has to be a real number from 0 to 100')
        print()

    elif action == 'e':
        print('--- Expansion ---')
        print('Enter a formula:')
        frm = input(PROMPT)
        try:
            frm = to_cnf(frm)
            print('Select order (real number from 0 to 100):')
            order = input(PROMPT)
            print(bb.expand(frm, int(order)))
        except SympifyError:
            print('Invalid formula')
        except ValueError:
            print('Order has to be a real number from 0 to 100')
        print()

    elif action == 'c':
        print('--- Contraction ---')
        print('Enter a formula:')
        frm = input(PROMPT)
        try:
            frm = to_cnf(frm)
            bb.contraction(frm)
        except SympifyError:
            print('Invalid formula')
        print()

    elif action == 'd':
        bb.clear()
        print('--- Deleted belief base ---')
        print()

    elif action == 'p':
        print('--- Printing belief base ---')
        bb.print_beliefs()
        print()

    elif action == 'q':
        exit()

    else:
        print('Sorry, the command was not recognized. Type \'h\' for help.')
        print()

    handle_input(bb)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Belief base revision CLI tool.')
    parser.add_argument('--debug', action='store_true', help='enable debugging')
    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    bb = BeliefBase()
    #print_help()
    handle_input(bb)

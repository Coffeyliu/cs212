# --------------
# User Instructions
# 
# Modify the function compile_formula so that the function 
# it returns, f, does not allow numbers where the first digit
# is zero. So if the formula contained YOU, f would return 
# False anytime that Y was 0 
#===========================
#NOTE: 
# 1. change string.maketrans() to str.makertrans
# 2. correct test() for second assertion
#===========================

import re
import itertools
import string
from collections import OrderedDict


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit 
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""
    
    # modify the code in this function.
    # FB: a `set` is a **not-ordered** collection. `list` is ordered
    # and the docstring above is specifically stating that the order of the
    # letters should be the same as in the original formula string. So this is
    # a bug: your call to set may scramble the order of the letters. Not to mention
    # that this is the source of your non-determinism you are groping with later.

    # letters = ''.join(set(re.findall('[A-Z]', formula)))    # old approach
    letters = ''.join(list(OrderedDict((element, None) for element in re.findall('[A-Z]', formula)))) #new approach

    #NOTE:I use len() because I know in this game length of the formular should be small. 
    # FB: why `ascii_letters`? You have only uppercase letters; apparently,
    # based on the compile_word implementation, word.isupper is the only test needed to qualify as
    # a numeric expression encoding (not operator), so why not do the same? that is already
    # stricter than `c[0] in bag_of_letters` and faster ;-)
    # FB: you called the **same** re.split twice, here and for tokens: it is a waste (regexp are faster than 
    # iterating through the string in python, but they do take time, so...)

    # first_letter = [c[0] for c in re.split('([A-Z]+)', formula) if len(c) > 1 and c[0] in string.ascii_letters] # old approach
    temp =  re.split('([A-Z]+)', formula)
    first_letter = [c[0] for c in temp if len(c) > 1 and c[0].isupper()]    # new approach     
    parms = ', '.join(letters)
    tokens = map(compile_word, temp)
    body = ''.join(tokens)

    if first_letter:
        # FB: nice! you shortcut the body evaluation if a beginning letter is 0
        body = ' and '.join('%s != 0' % (c) for c in first_letter) + ' and ' + body 

    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words uncahanged: compile_word('+') => '+'"""

    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) 
                 for (i, d) in enumerate(word[::-1])]

        return '(' + '+'.join(terms) + ')'
    else:
        return word
    
def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula."""
    f, letters = compile_formula(formula)

    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))

                return formula.translate(table)
        except ArithmeticError:
            pass

def test():
    assert faster_solve('A + B == BA') == None # should NOT return '1 + 0 == 01'
    assert faster_solve('YOU == ME**2') in ['289 == 17**2', '576 == 24**2', '841 == 29**2', '324 == 18**2']
    assert faster_solve('X / X == X') == '1 / 1 == 1'

    return 'tests pass'
print(test())

# CS 212, hw1-2: Jokers Wild
#
# -----------------
# User Instructions
#
# Write a function best_wild_hand(hand) that takes as
# input a 7-card hand and returns the best 5 card hand.
# In this problem, it is possible for a hand to include
# jokers. Jokers will be treated as 'wild cards' which
# can take any rank or suit of the same color. The 
# black joker, '?B', can be used as any spade or club
# and the red joker, '?R', can be used as any heart 
# or diamond.
#
# The itertools library may be helpful. Feel free to 
# define multiple functions if it helps you solve the
# problem. 
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools

card_num = '23456789TJQKA'
red_cards = [n+s for n in card_num for s in 'HD']
black_cards = [n+s for n in card_num for s in 'SC'] 
# shirouto: well, zip would be clearer about intent here; also easier to work with
red_black_com = [[r]+[b] for r in red_cards for b in black_cards]
# print(red_black_com)


def get_possible_hands(hand):
    """replace the joker with all possible card. return a list of possible hands.
    if there is no joker, return list of original hand.
    """
    # shirouto: why the list.index() calls? If you just want to check whether an 
    # element is an in list, you have ``x in xs`` syntax. Much clearer and no need
    # for the try-except block. 
    # Moreover, you know that list search is O(n): why do you do the same search twice
    # for each color, so all together 4 times? And, since we are here? Do you really 
    # need even *two* list scans? Can this function be done with only one?
    # Then a nitpick, really... any particular reason you assign to ``hands`` first
    # before returning? Why not return directly?
    try:
        if hand.index('?B') and hand.index('?R'):
            hand.remove('?B')
            hand.remove('?R')
            hands = [hand+rb_com for rb_com in red_black_com]

            return hands
    except:    
        pass

    try:       
        if hand.index('?B'):
            hand.remove('?B')
            hands = [hand+[jr] for jr in black_cards]   

            return hands
    except:
        pass

    try:
        if hand.index('?R'):
            hand.remove('?R')
            hands = [hand+[jr] for jr in black_cards]  

            return hands
    except:
        pass
    
    return [hand]


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand. -- this is solution from hw1_1.py"
    hands = [ele for ele in itertools.combinations(hand, 5)]

    return max(hands, key=hand_rank)

def best_wild_hand(hand):
    "Try all values for jokers in all 5-card selections."
    # shirouto: Hrm... once again, what is the purpose of ``hands``? Documenting?
    # Don't you think your ``get_possible_hands`` function name is clear already?
    hands = get_possible_hands(hand)
    # shirouto: This list here is a just memory waste really (and CPU clocks, since the list is
    # is allocated on the heap --- yeah, dynamical language and all that --- and time needs spent
    # during allocation and garbage collection): ``max()`` consumes an iterable, so you could 
    # call it directly with your generator expression. And since you are doing that, you could
    # also get rid of that extra list allocation in ``best_hand`` and stick with an iterator-based
    # API, given your use cases here. Yes, you must learn iterators/generators and all that.
    all_best_hands = [best_hand(h) for h in hands]

    return max(all_best_hands, key=hand_rank)

def test_best_wild_hand():
    assert (sorted(best_wild_hand("6C 7C 8C 9C TC 5C ?B".split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand("TD TC 5H 5C 7C ?R ?B".split()))
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])

    return 'test_best_wild_hand passes'

# ------------------
# Provided Functions
# 
# You may want to use some of the functions which
# you have already defined in the unit to write 
# your best_hand function.

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand) 

    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)

    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]

    return len(set(suits)) == 1

def straight(ranks):
    """Return True if the ordered 
    ranks form a 5-card straight."""

    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    """Return the first rank that this hand has 
    exactly n-of-a-kind of. Return None if there 
    is no n-of-a-kind in the hand."""

    for r in ranks:
        if ranks.count(r) == n: return r

    return None

def two_pair(ranks):
    """If there are two pair here, return the two 
    ranks of the two pairs, else None."""
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))

    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None 

print(test_best_wild_hand())

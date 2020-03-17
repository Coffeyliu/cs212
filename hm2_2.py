#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# 1. Hopper does not live on the top floor. 
# 2. Kay does not live on the bottom floor. 
# 3. Liskov does not live on either the top or the bottom floor. 
# 4. Perlis lives on a higher floor than does Kay. 
# 5. Ritchie does not live on a floor adjacent to Liskov's. 
# 6. Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools
def higherthan(floor1, floor2):
    """If floor1 is highter than floor2, then floor1 > floor2"""
    return floor1 - floor2 > 0

def adjancentto(floor1, floor2):
    """if floor1 and floor2 adjancent to each other, return
    floor1 - floor2 == 1 or floor2 - floor1 == 1"""
    return floor1 - floor2 == 1 or floor2 - floor1 == 1

def floor_puzzle():
    # Your code here
    floors = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))

    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
            for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
            if Hopper is not 5   #1
            if Kay is not 1 #2
            if Liskov is not 1 and Liskov is not 5 #3
            if higherthan(Perlis, Kay) #4
            if not adjancentto(Ritchie, Liskov)  #5
            if not adjancentto(Liskov, Kay)  #6
            ) 

print(floor_puzzle())
            

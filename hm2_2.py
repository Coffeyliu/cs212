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

def floor_puzzle():
    # Your code here
    floors = [1, 2, 3, 4, 5]
    # FB: so what is the point of collecting that iterator into a list
    # just to iterate later on through it? This is not only a waste of both CPU
    # and memory (you never need to realize that list into memory), it is first
    # rather an odd usage for generators/iterators: why bother with them at all?
    orderings = list(itertools.permutations(floors))

    return next([Hopper, Kay, Liskov, Perlis, Ritchie]
            for (Hopper, Kay, Liskov, Perlis, Ritchie) in orderings
            if Hopper is not 5   #1
            and Kay is not 1 #2
            and Liskov is not 1 and Liskov is not 5 #3
            and Perlis > Kay #4
            and abs(Ritchie - Liskov) != 1 #5
            and abs(Liskov - Kay) != 1  #6
            ) 

print(floor_puzzle())
            


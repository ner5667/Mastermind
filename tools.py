"""
All functions have the following structure\n
In: \n
    possible_values (list[str]): A list of possible values the list can hold\n
    length_solution (int): The length of the list being looked for\n
    compare (func): The function that is used to compare the guess and the real solution\n
    (Optional) \n
    debug=False (Bool): This prints out different debug values \n
Out: \n
    The number that was being searched for
"""

import itertools

def brute_force(possible_values, length_solution, compare, debug=False):
    if debug:
        print("Calculating permutations...")
    permutations = list(itertools.product(possible_values, repeat=length_solution))
    counter = 0
    guess = permutations[counter]
    print(len(permutations))
    if debug:
        print("Checking Permutations...")
        while 0 in compare(guess) or 1 in compare(guess):
            counter += 1
            guess = permutations[counter]
            print(counter, guess)
    else:
        while 0 in compare(guess) or 1 in compare(guess):
            counter += 1
            guess = permutations[counter]
    return guess


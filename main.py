import tools
import logic
import time

NUM_VALUES = 9
NUM_POSSIBLE_VALUES = 7
NUM_REPEATS = 50

#Permutations: possible_values ^ values

game = logic.Game(NUM_VALUES, NUM_POSSIBLE_VALUES)

start = time.time()
for i in range(NUM_REPEATS):
    proposed_solution = list(tools.brute_force(game.possible_values, len(game.solution), game.compare))
    actual_solution = list(game.solution)
    if proposed_solution != actual_solution:
        print("Error")
    game.generate_new_solution()
    print("Check: ", i+1)

print("Time: ", round(time.time() - start, 3), "s")
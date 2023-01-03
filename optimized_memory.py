import tracemalloc
import time
from solution import Solution
from bruteforce import brute_force
from optimized import knapsack

solution = Solution.bruteforce()

# starting the monitoring
tracemalloc.start()

# function call
solution.best_actions = brute_force(solution.actions)

# displaying the size of used memory
print("  *** Use case of dataset0.csv, the size of used memory :", tracemalloc.get_tracemalloc_memory(), "bytes.")


# stopping the library
tracemalloc.stop()

time.sleep(4)


for i in range(3):
    solution = Solution.optimized(i)

    # starting the monitoring
    tracemalloc.start()

    # function call
    solution.best_actions = knapsack(solution.actions, 500)

    # displaying the size of used memory
    print("  *** Use case of dataset" + str(i) + ".csv, the size of used memory :",
          tracemalloc.get_tracemalloc_memory(), "bytes.")

    # stopping the library
    tracemalloc.stop()

    time.sleep(4)

import time
from solution import Solution
from bruteforce import brute_force
from optimized import knapsack

solution = Solution.bruteforce()

begin = time.time()
# function call
solution.best_actions = brute_force(solution.actions)
end = time.time()
print("  ** Use case of dataset0.csv, the duration of Brute Force program running :",
      round(end - begin, 2), "seconds.")

time.sleep(4)


for i in range(3):
    solution = Solution.optimized(i)

    begin = time.time()
    # function call
    solution.best_actions = knapsack(solution.actions, 500)
    end = time.time()
    print("  ** Use case of dataset" + str(i) + ".csv, the duration of optimized program running :",
          round(end - begin, 2), "seconds.")

    time.sleep(4)

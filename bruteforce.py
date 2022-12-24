import time
from itertools import combinations
from solution import Solution


def brute_force(actions: list, max_cost: int = 500) -> list:
    best_combination = []
    max_profit_euro = 0
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            # get a total cost for each list of combinations
            cost = Solution.total_cost(list(combination))
            # get a total profit in € for each list of combinations
            profit_euro = Solution.total_profit_euro(list(combination))
            if cost <= max_cost and profit_euro > max_profit_euro:
                max_profit_euro = profit_euro
                best_combination = list(combination)
    return best_combination


def brute_force_result(i: int = 0):
    print("\n********** Running of Brute Force program with the use of dataset" + str(i) + ".csv **********")
    solution = Solution.bruteforce()
    start = time.time()
    solution.best_actions = brute_force(solution.actions)
    # Display the data of selected actions to buy
    solution.display_result()
    end = time.time()
    print("  ** Duration of Brute Force program running :", round(end - start, 2), "seconds.")

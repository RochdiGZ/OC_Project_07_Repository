import time
from itertools import combinations
from solution import Solution


def brute_force(actions: list, max_cost: int = 500) -> list:
    best_combination = []
    max_profit = 0
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            # get a total cost for each combination
            cost = Solution.total_cost(list(combination))
            if cost <= max_cost:
                # get a total profit for each combination
                profit = Solution.total_profit(list(combination))
                if profit > max_profit:
                    max_profit = profit
                    best_combination = combination
    return best_combination


def brute_force_result():
    print("\nRunning the Brute Force Algorithm using dataset0.csv")
    solution = Solution.bruteforce()
    start = time.time()
    selected_actions = brute_force(solution.actions)
    # Display the data of selected actions to buy
    solution.display_result(selected_actions)
    end = time.time()
    print("Duration of program running :", round(end - start, 2), "seconds.")

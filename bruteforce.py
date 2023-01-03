import time
from itertools import combinations
from solution import Solution
from tqdm import tqdm


def brute_force(actions: list, max_cost: int = 500) -> list:
    best_combination = []
    max_profit_euro = 0
    n = len(actions)
    for p in tqdm(range(1, n + 1)):
        # Number of possible combinations = {factorial(n) // (factorial(p) * factorial(n - p))}
        for combination in combinations(actions, p):
            # get a total cost for each list of combinations
            cost = Solution.total_cost(list(combination))
            if cost <= max_cost:
                # get a total profit in € for each list of combinations
                profit_sum = Solution.total_profit_euro(list(combination))
                if profit_sum > max_profit_euro:
                    # get the best combination that returns the maximum profit
                    max_profit_euro = profit_sum
                    best_combination = list(combination)
    return best_combination


def brute_force_result(i: int = 0):
    print("\n********** Running of Brute Force program with the use of dataset" + str(i) + ".csv **********")
    solution = Solution.bruteforce()
    start = time.time()
    solution.best_actions = brute_force(solution.actions)
    end = time.time()
    # Display the data of selected actions to buy
    solution.display_result()
    print("  ** Duration of Brute Force program running :", round(end - start, 2), "seconds.")

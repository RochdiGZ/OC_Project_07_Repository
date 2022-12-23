import time
from itertools import combinations
from algorithm import Algorithm


def brute_force(actions: list, max_cost: int = 500) -> list:
    best_combination = []
    max_profit = 0
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            # get a total cost for each combination
            cost = Algorithm.total_cost(list(combination))
            if cost <= max_cost:
                # get a total profit for each combination
                profit = Algorithm.total_profit(list(combination))
                if profit > max_profit:
                    max_profit = profit
                    best_combination = combination
    return best_combination


def brute_force_result():
    print("\nRunning of Brute force algorithm with dataset0")
    algo = Algorithm.bruteforce()
    actions = algo.actions
    start = time.time()
    selected_actions = brute_force(actions)
    # Display the data of selected actions to buy
    algo.display_names(selected_actions)
    algo.display_total_cost(selected_actions)
    algo.display_total_profit(selected_actions)
    end = time.time()
    print("Duration of program running :", round(end - start, 2), "seconds.")

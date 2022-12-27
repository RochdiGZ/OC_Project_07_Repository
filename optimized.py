import time
from solution import Solution


def knapsack(actions: list, max_cost: int) -> list:
    n = len(actions)
    m = [[float(0) for _ in range(max_cost + 1)] for _ in range(n + 1)]

    # Build matrix which contains max profits in € for each combination of n actions
    for r in range(1, n + 1):
        for c in range(1, max_cost + 1):
            action = actions[r - 1]
            if c >= action.price :
                a = m[r - 1][c]
                b = m[r - 1][c - action.price] + action.profit_euro
                m[r][c] = max(a, b)
            else:
                m[r][c] = m[r - 1][c]
    # Best profit = m[n][max_cost] = m[-1][-1]

    # Find the best combinations
    c = max_cost
    r = len(actions)
    selected_actions = []
    while c > 0 and r >= 0:
        action = actions[r - 1]
        if c >= action.price:
            a = m[r][c]
            b = m[r - 1][c - action.price] + action.profit_euro
            if a == b:
                selected_actions.append(action)
                c -= action.price
        r -= 1

    return selected_actions


def knapsack_result(i: int = 0):
    print("\n********** Running of optimized program with the use of dataset" + str(i) + ".csv **********")
    solution = Solution.optimized(i)
    # Update prices and profits of actions (multiply each price per 100 and multiply each profit per 100)
    actions = solution.multiply_per_100(solution.actions)
    start = time.time()
    selected_actions = knapsack(actions, 50000)
    # Update prices and profits of selected actions (divide each price per 100 and divide each profit per 100)
    solution.best_actions = solution.divide_per_100(selected_actions)
    # Display the data of selected actions to buy
    solution.display_result()
    end = time.time()
    print("  ** Duration of optimized program running :", round(end - start, 2), "seconds.")

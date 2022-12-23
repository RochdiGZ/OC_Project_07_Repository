import time
from solution import Solution


def knapsack(actions: list, max_cost: int = 50000) -> list:
    n = len(actions)
    m = [[float(0) for _ in range(max_cost + 1)] for _ in range(n + 1)]

    # Build matrix which contains max profits
    for i in range(1, n + 1):
        for c in range(1, max_cost + 1):
            if actions[i - 1].price <= c:
                a = m[i - 1][c]
                b = m[i - 1][c - actions[i - 1].price] + actions[i - 1].profit
                m[i][c] = max(a, b)
            else:
                m[i][c] = m[i - 1][c]
    # Best profit = m[n][max_cost] = m[-1][-1]

    # Find the best combinations
    c = max_cost
    r = len(actions)
    selected_actions = []
    while c >= 0 and r >= 0:
        action = actions[r - 1]
        a = m[r][c]
        b = m[r - 1][c - action.price] + action.profit
        if a == b:
            selected_actions.append(action)
            c -= action.price
        r -= 1

    return selected_actions


def knapsack_result():
    for i in range(3):
        if i == 0:
            print("\nRunning the Knapsack Algorithm using dataset" + str(i) + ".csv")
        elif i == 1:
            print("\nRunning the Knapsack Algorithm using dataset" + str(i) + ".csv")
        elif i == 2:
            print("\nRunning the Knapsack Algorithm using dataset" + str(i) + ".csv")
        solution = Solution.optimized(i)
        actions = solution.multiply_per_100(solution.actions)
        start = time.time()
        best_actions = knapsack(actions)
        # Update each price of selected actions (divide each price per 100)
        selected_actions = solution.divide_per_100(best_actions)
        # Display the data of selected actions to buy
        solution.display_result(selected_actions)
        end = time.time()
        print("Duration of program running :", round(end - start, 2), "seconds.")

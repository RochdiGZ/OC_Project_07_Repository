import time
from solution import Solution
from tqdm import tqdm


def knapsack(actions: list, max_cost: int) -> list:
    n = len(actions)
    m = [[float(0) for _ in range(max_cost + 1)] for _ in range(n + 1)]

    # Build matrix which contains max profits in € for each combination of n actions
    for r in tqdm(range(1, n + 1), desc="Running of optimized program"):
        for c in range(1, max_cost + 1):
            action = actions[r - 1]
            if c >= action.price:
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
    while c > 0 and r > 0:
        i = r - 1
        if m[r][c] != m[i][c]:
            selected_actions.append(actions[i])
            c -= actions[i].price
        r -= 1

    return selected_actions


def knapsack_result(i: int):
    print("\n****************************** Running of optimized program ******************************")
    print("\n********** Running of optimized program with the use of dataset" + str(i) + ".csv **********")
    solution = Solution.optimized(i)
    start = time.time()
    solution.best_actions = knapsack(solution.actions, 500)
    end = time.time()
    # Display the data of selected actions to buy
    solution.display_result()
    print("  ** Duration of optimized program running :", round(end - start, 2), "seconds.")

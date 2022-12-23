import time
from algorithm import Algorithm


def knapsack(actions: list, max_cost: int = 50000) -> (list, float):
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

    return selected_actions, m[-1][-1]   # m[n][max_cost] = m[-1][-1]


def knapsack_result():
    for i in range(3):
        if i == 0:
            print("\nRunning of knapsack algorithm with dataset" + str(i))
        elif i == 1:
            print("\nRunning of knapsack algorithm with dataset" + str(i))
        elif i == 2:
            print("\nRunning of knapsack algorithm with dataset" + str(i))
        algo = Algorithm.optimized(i)
        actions = algo.actions
        actions = algo.multiply_per_100(actions)
        start = time.time()
        selected_actions, best_profit = knapsack(actions)
        print("Best profit :", round(best_profit/100, 2), "€")
        # Update each price of selected actions (divide each price per 100)
        best_actions = algo.divide_per_100(selected_actions)
        # Display the data of selected actions to buy
        algo.display_names(best_actions)
        algo.display_total_cost(best_actions)
        algo.display_total_profit(best_actions)
        end = time.time()
        print("Duration of program running :", round(end - start, 2), "seconds.")


"""
def choose_file() -> str:
    number = input("Please, enter 0 or 1 or 2 for choosing a csv file : ")
    if number in ["0", "1", "2"]:
        return number
    return choose_file()


def knapsack_result0():
    ok = True
    while ok:
        choice = input("Would do you like testing the program ? (Yes/No) : ")
        if choice.lower() == "yes" or choice.lower() == "y":
            i = int(choose_file())
            algo = Algorithm.optimized(i)
            actions = algo.actions
            actions = multiply_price(actions)
            start = time.time()
            selected_actions = knapsack(actions)
            # Update each price of selected actions (divide each price per 100)
            best_actions = divide_price(selected_actions)
            # Display the data of selected actions to buy
            algo.display_names(best_actions)
            algo.display_total_cost(best_actions)
            algo.display_total_profit(best_actions)
            end = time.time()
            print("\nDuration of program running :", round(end - start, 2), "seconds.")
        else:
            ok = False
"""
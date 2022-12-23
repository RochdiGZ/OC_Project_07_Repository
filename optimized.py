import time
from algorithm import Algorithm


def knapsack(actions: list, max_cost: int = 500000) -> list:
    n = len(actions)
    m = [[float(0) for _ in range(max_cost + 1)] for _ in range(n + 1)]

    # Build matrix which contains max profits
    for i in range(n + 1):
        for c in range(max_cost + 1):
            cost = actions[i - 1].price
            profit = actions[i - 1].profit
            if i == 0 or c == 0:
                m[i][c] = 0
            elif cost <= c:
                m[i][c] = max(profit + m[i - 1][c - cost], m[i - 1][c])
            else:
                m[i][c] = m[i - 1][c]

    # Find the best combinations
    c = max_cost
    r = len(actions)
    selected_actions = []
    while c >= 0 and r >= 0:
        action = actions[r - 1]
        if m[r][c] == m[r - 1][c - action.price] + action.profit:
            selected_actions.append(action)
            c -= action.price
        r -= 1

    return selected_actions   # m[n][max_cost] = m[-1][-1]


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
        actions = algo.multiply_price(actions)
        start = time.time()
        selected_actions = knapsack(actions)
        # Update each price of selected actions (divide each price per 100)
        best_actions = algo.divide_price(selected_actions)
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
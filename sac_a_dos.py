class Action:
    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit
        self.profit_euro = self.price * self.profit / 100

    def __str__(self) -> str:
        return f"        * {self.name}, {round(self.price, 2)} €, {round(self.profit, 2)} %, " \
               f"{round(self.profit_euro, 2)} €"


def matrix_knapsack(actions: list, max_cost: int) -> list:
    n = len(actions)
    m = [[float(0) for _ in range(max_cost + 1)] for _ in range(n + 1)]

    for r in range(0, n + 1):
        for c in range(0, max_cost + 1):
            if r == 0 or c == 0:
                m[r][c] = 0
            else:
                i = r - 1
                if c >= actions[i].price:
                    a = m[i][c]
                    b = m[i][c - actions[i].price] + actions[i].profit_euro
                    m[r][c] = max(a, b)
                else:
                    m[r][c] = m[i][c]
    # Best profit = m[n][max_cost] = m[-1][-1]
    return m


def display_matrix(m: list, n: int, max_cost: int):
    print("   c ->", end=" | ")
    for c in range(0, max_cost + 1):
        if c < 10:
            print(" " + str(c) + " ", end=" | ")
        else:
            print(" " + str(c), end=" | ")

    for r in range(0, n + 1):
        print("\n r -> " + str(r), end=" | ")
        for c in range(0, max_cost + 1):
            print(float(m[r][c]), end=" | ")


def best_actions_knapsack(actions: list, max_cost: int, m: list, ) -> list:
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


def knapsack(actions: list, max_cost: int) -> list:
    # Build matrix which contains max profits in € ; Best profit = m[n][max_cost] = m[-1][-1]
    m = matrix_knapsack(actions, max_cost)
    n = len(actions)
    display_matrix(m, n, max_cost)
    # Find the best combinations
    selected_actions = best_actions_knapsack(actions, max_cost, m)
    return selected_actions


def display_result(selected_actions: list):
    total_cost = 0
    total_profit_euro = 0
    for action in selected_actions:
        print("     ", action)
        total_cost += action.price
        total_profit_euro += action.profit_euro
    print("        * * * * * * * * * * * * * * * * * * * *")
    print("        *    Total cost :", total_cost, "€")
    print("        *    Total profit :", round(total_profit_euro, 2), "€")
    print("        * * * * * * * * * * * * * * * * * * * *")


if __name__ == "__main__":
    action1 = Action("Action-1", 2, 50)
    action2 = Action("Action-2", 5, 30)
    action3 = Action("Action-3", 10, 20)
    action4 = Action("Action-4", 12, 20)
    action5 = Action("Action-5", 8, 25)

    all_actions = [action1, action2, action3, action4, action5]
    print("\n********** Running of optimized program with the use of 5 actions **********")
    display_result(all_actions)
    """
    budget = 10
    best_actions = knapsack(all_actions, budget)
    print("\n  *", len(best_actions), "selected actions to buy with", budget, "€")
    display_result(best_actions)
    budget = 15
    best_actions = knapsack(all_actions, budget)
    print("\n  *", len(best_actions), "selected actions to buy with", budget, "€")
    display_result(best_actions)
    budget = 35
    best_actions = knapsack(all_actions, budget)
    print("\n  *", len(best_actions), "selected actions to buy with", budget, "€")
    display_result(best_actions)
    """
    # budget = sum([a.price for a in all_actions])
    budget = 15
    for cost in range(budget + 1):
        best_actions = knapsack(all_actions, cost)
        print("\n        * ", len(best_actions), " selected actions to buy with", cost, "€")
        display_result(best_actions)

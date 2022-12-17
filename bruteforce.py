import csv
import time
from itertools import combinations


def choose_file() -> str:
    number = input("Please, enter 0 or 1 or 2 for choosing a csv file : ")
    if number in ["0", "1", "2"]:
        return "dataset" + number
    else:
        return choose_file()


def get_data_csv(file_name: str) -> list:
    with open(f"dataset/{file_name}.csv", "r", encoding="utf-8") as f:
        data_csv = csv.reader(f)
        data = []
        for line in data_csv:
            data.append(line)
    return data


def get_actions(data: list) -> list:
    actions = []
    for i in range(1, len(data)):
        actions.append((data[i][0], float(data[i][1]), float(data[i][2])))
    return actions


def actions_price(actions: list) -> float:
    sum_prices = sum([float(price) for _, price, _ in actions])
    return round(sum_prices, 3)


def actions_profit(actions: list) -> float:
    sum_profits = sum([float(price) * float(profit) / 100 for _, price, profit in actions])
    return round(sum_profits, 3)


def first_invest(actions: list) -> list:
    list_actions = []
    price_max = 500
    # sort by profit pourcentage
    actions = sorted(actions, key=lambda d: d[2], reverse=True)
    for action in actions:
        if price_max >= action[1]:
            list_actions.append(action)
            price_max -= action[1]
    return list_actions


def best_invest(actions: list) -> list:
    best_combination = []
    price_max = 500
    profit_max = 0
    # sort by profit pourcentage
    actions = sorted(actions, key=lambda d: d[2], reverse=True)
    number_combinations = len(actions)
    for i in range(1, number_combinations):
        for combination in combinations(actions, i):
            # get a sum of prices for each combination
            price = actions_price(list(combination))
            if price <= price_max:
                # get a sum of profits for each combination
                profit = actions_profit(list(combination))
                if profit > profit_max:
                    profit_max = profit
                    best_combination = list(combination)
    return best_combination


def brute_force(file_name: str):
    print(f"The chosen file is {file_name}.csv")
    start = time.time()
    list_of_actions = get_actions(get_data_csv(file_name))

    print("Price of actions :", actions_price(list_of_actions), "€")

    print("Profit of actions :", actions_profit(list_of_actions), "€")

    # Display all actions to buy with 500 euro for the first combination
    # best_actions_to_buy = first_invest(list_of_actions)
    # Display all actions to buy with 500 euro for the best combination

    best_actions_to_buy = best_invest(list_of_actions)

    print("\nNumber of actions to buy :", len(best_actions_to_buy))
    best_actions_to_buy = sorted(best_actions_to_buy, key=lambda d: d[1], reverse=True)
    for best_action in best_actions_to_buy:
        print(best_action)

    print("\nPrice of actions to buy :", actions_price(best_actions_to_buy), "€")

    print("Profit of actions to buy :", actions_profit(best_actions_to_buy), "€")

    end = time.time()
    print("\nDuration of execution :", end - start, "seconds.")


if __name__ == "__main__":
    csv_file = choose_file()
    brute_force(csv_file)

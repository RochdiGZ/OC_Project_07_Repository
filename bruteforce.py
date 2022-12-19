import csv
import time
from itertools import combinations

PRICE_MAX = 500


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


def display_result(file_name, best_actions: list):
    print(f"The chosen file is {file_name}.csv which contains the all actions data")

    # sort by price the data of best actions to buy
    best_actions = sorted(best_actions, key=lambda d: d[1], reverse=True)
    print("\nThe data of", len(best_actions), "best actions :")
    for action in best_actions:
        print(action)

    print("\nTotal cost :", actions_price(best_actions), "€")

    print("Total profit :", actions_profit(best_actions), "€")


def brute_force(file_name: str) -> list:
    actions = get_actions(get_data_csv(file_name))
    best_combination = []
    profit_max = 0
    for i in range(1, len(actions) + 1):
        for combination in combinations(actions, i):
            # get a sum of prices for each combination
            price = actions_price(list(combination))
            if price <= PRICE_MAX:
                # get a sum of profits for each combination
                profit = actions_profit(list(combination))
                if profit > profit_max:
                    profit_max = profit
                    best_combination = list(combination)
    return best_combination


def brute_force_result():
    csv_file = "dataset0"
    start = time.time()
    result = brute_force(csv_file)
    # Display the data of best actions to buy with 500 € for the best combination
    display_result(csv_file, result)
    end = time.time()
    print("\nDuration of program running :", round(end-start, 2), "seconds.")


if __name__ == "__main__":
    brute_force_result()

import csv
import time

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
        if float(data[i][1]) > 0 and float(data[i][2]) > 0:
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
    print("\nThe", len(best_actions), "best actions to buy:")
    for action in best_actions:
        print(action[0])

    print("\nTotal cost :", actions_price(best_actions), "€")

    print("Total profit :", actions_profit(best_actions), "€")


def best_invest(file_name: str) -> list:
    actions = get_actions(get_data_csv(file_name))
    # sort by profit pourcentage the all data
    actions = sorted(actions, key=lambda d: d[2], reverse=True)
    list_actions = []
    price_max = PRICE_MAX
    for action in actions:
        if price_max >= action[1]:
            list_actions.append(action)
            price_max -= action[1]
    return list_actions


def choose_file() -> str:
    number = input("Please, enter 0 or 1 or 2 for choosing a csv file : ")
    if number in ["0", "1", "2"]:
        return "dataset" + number
    else:
        return choose_file()


def best_invest_result():
    csv_file = choose_file()
    start = time.time()
    result = best_invest(csv_file)
    # Display the data of best actions to buy with 500 €
    display_result(csv_file, result)
    end = time.time()
    print("\nDuration of program running :", round(end-start, 4), "seconds.")


if __name__ == "__main__":
    best_invest_result()

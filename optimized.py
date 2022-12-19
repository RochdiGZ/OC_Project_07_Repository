import csv
import time


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
        if float(data[i][1]) > 0 and float(data[i][2]) > 0 and len(actions) < 21:
            actions.append((data[i][0], float(data[i][1]), float(data[i][2])))
    return actions


def actions_price(actions: list) -> float:
    sum_prices = sum([float(price) for _, price, _ in actions])
    return round(sum_prices, 3)


def actions_profit(actions: list) -> float:
    sum_profits = sum([float(price) * float(profit) / 100 for _, price, profit in actions])
    return round(sum_profits, 3)


def best_invest(actions: list) -> list:
    # sort by profit pourcentage the all data
    actions = sorted(actions, key=lambda d: d[2], reverse=True)
    list_actions = []
    price_max = 500
    for action in actions:
        if price_max >= action[1]:
            list_actions.append(action)
            price_max -= action[1]
    return list_actions


def display_result(best_actions: list):
    print("\nThe number of best actions to buy :", len(best_actions))

    # sort by price the data of best actions to buy
    best_actions = sorted(best_actions, key=lambda d: d[1], reverse=True)
    print("The data of best actions to buy :")
    for action in best_actions:
        print(action)

    print("\nThe price of best actions to buy :", actions_price(best_actions), "€")

    print("The profit of best actions to buy :", actions_profit(best_actions), "€")


def optimized_invest(file_name: str) -> list:
    print(f"The chosen file is {file_name}.csv which contains the all actions data")

    list_of_actions = get_actions(get_data_csv(file_name))
    # print("Actions :\n", list_of_actions)
    print("The price of all actions :", actions_price(list_of_actions), "€")
    print("The profit of all actions :", actions_profit(list_of_actions), "€")
    return best_invest(list_of_actions)


def choose_file() -> str:
    number = input("Please, enter 0 or 1 or 2 for choosing a csv file : ")
    if number in ["0", "1", "2"]:
        return "dataset" + number
    else:
        return choose_file()


if __name__ == "__main__":
    csv_file = choose_file()
    start = time.time()
    result = optimized_invest(csv_file)
    # Display the data of best actions to buy with 500 € for the best combination
    display_result(result)
    end = time.time()
    print("\nDuration of program running :", end - start, "seconds.")

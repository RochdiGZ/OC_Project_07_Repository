import csv


class Action:
    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit

    def __str__(self) -> str:
        return f"{self.name}, {self.price} €, {self.profit} €"


class Solution:
    def __init__(self, file_name: str, max_cost: int):
        self.file_name = file_name
        self.max_cost = max_cost
        self.actions = self.get_data_csv()

    @classmethod
    def bruteforce(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=500)

    @classmethod
    def optimized(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=50000)

    def get_data_csv(self) -> list:
        with open(f"dataset/{self.file_name}.csv", "r", encoding="utf-8") as f:
            data_csv = csv.reader(f)
            # ignore the first row which contains 'name, price, profit'
            next(data_csv)
            actions = []
            for row in data_csv:
                name = row[0]
                price = float(row[1])
                # profit in €
                profit = float(row[1]) * float(row[2]) / 100
                if price > 0 and profit > 0:
                    action = Action(name, price, profit)
                    actions.append(action)
        return actions

    def display_result(self, actions: list):
        print(len(actions), "selected actions to buy :")
        for action in actions:
            print(action.name)
        print("Total cost :", self.total_cost(actions), "€")
        print("Total profit :", self.total_profit(actions), "€")

    @staticmethod
    def total_cost(actions: list) -> float:
        return round(sum([action.price for action in actions]), 2)

    @staticmethod
    def total_profit(actions: list) -> float:
        return round(sum([action.profit for action in actions]), 2)

    @staticmethod
    def multiply_per_100(actions: list) -> list:
        for action in actions:
            action.price = int(action.price * 100)
            action.profit = action.profit * 100
        return actions

    @staticmethod
    def divide_per_100(actions) -> list:
        for action in actions:
            action.price = float(action.price / 100)
            action.profit = round(action.profit / 100, 2)
        return actions

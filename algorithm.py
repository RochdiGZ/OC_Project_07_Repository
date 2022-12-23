import csv


class Action:
    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit

    def __str__(self) -> str:
        return f"{self.name}, {self.price}, {self.profit}"


class Algorithm:
    def __init__(self, file_name: str, max_cost: int):
        self.file_name = file_name
        self.max_cost = max_cost
        self.actions = self.get_data_csv()

    @classmethod
    def bruteforce(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=5000)

    @classmethod
    def optimized(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=500000)

    def get_data_csv(self) -> list:
        with open(f"dataset/{self.file_name}.csv", "r", encoding="utf-8") as f:
            data_csv = csv.reader(f)
            # ignore the first row which contains 'name, price, profit'
            next(data_csv)
            actions = []
            for row in data_csv:
                name = row[0]
                price = float(row[1])
                profit = float(row[2])
                if price > 0 and profit > 0:
                    action = Action(name, price, profit)
                    actions.append(action)
        return actions

    @staticmethod
    def display_names(actions: list):
        print(len(actions), "selected actions to buy :")
        for action in actions:
            print(action.name)

    @staticmethod
    def total_cost(actions: list) -> float:
        return round(sum([action.price for action in actions]), 2)

    def display_total_cost(self, actions: list):
        print("Total cost :", self.total_cost(actions), "€")

    @staticmethod
    def total_profit(actions: list) -> float:
        return round(sum([action.profit * action.price / 100 for action in actions]), 2)

    def display_total_profit(self, actions: list):
        print("Total profit :", self.total_profit(actions), "€")

    @staticmethod
    def multiply_price(actions: list) -> list:
        for action in actions:
            action.price = int(action.price * 100)
        return actions

    @staticmethod
    def divide_price(actions) -> list:
        for action in actions:
            action.price = int(action.price / 100)
        return actions

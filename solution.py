import csv


class Action:
    def __init__(self, name: str, price: float, profit: float):
        self.name = name
        self.price = price
        self.profit = profit
        self.profit_euro = self.price * self.profit / 100

    def __str__(self) -> str:
        return f"        * {self.name}, {round(self.price, 2)} €, {round(self.profit, 2)} %, " \
               f"{round(self.profit_euro, 2)} €"


class Solution:
    def __init__(self, file_name: str, max_cost: int):
        self.file_name = file_name
        self.max_cost = max_cost
        self.actions = self.get_data_csv()
        self.best_actions = []

    def __str__(self):
        return f"""
        * * * * * * * * * * * * * * * * * * * *
        *    Total cost : {self.total_cost(self.best_actions)} €
        *    Total profit : {self.total_profit_euro(self.best_actions)} €
        * * * * * * * * * * * * * * * * * * * *
        """

    def display_result(self):
        print("\n  *", len(self.best_actions), "selected actions to buy :")
        for action in self.best_actions:
            print(action)
        print(self)

    @classmethod
    def bruteforce(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=500)

    @classmethod
    def optimized(cls, i: int = 0):
        return cls(file_name="dataset" + str(i), max_cost=500)

    @classmethod
    def sienna(cls, i: int):
        return cls(file_name="sienna" + str(i), max_cost=500)

    def get_data_csv(self) -> list:
        with open(f"dataset/{self.file_name}.csv", "r", encoding="utf-8") as f:
            data_csv = csv.reader(f)
            # ignore the first row which contains 'name, price, profit'
            next(data_csv)
            actions = []
            for row in data_csv:
                name = row[0]
                price = round(float(row[1]))
                profit = float(row[2])
                profit_euro = price * profit / 100
                if price > 0 and profit_euro > 0:
                    action = Action(name, price, profit)
                    actions.append(action)
        return actions

    """
    @staticmethod
    def get_data(actions: list, n: int = 20) -> list:
        actions_n = []
        for i in range(n):
            actions_n.append(actions[i])
        return actions_n
    """

    @staticmethod
    def total_cost(actions: list) -> float:
        return round(sum([action.price for action in actions]), 2)

    @staticmethod
    def total_profit_euro(actions: list) -> float:
        return round(sum([action.profit_euro for action in actions]), 2)

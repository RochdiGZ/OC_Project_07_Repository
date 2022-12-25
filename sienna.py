from solution import Action, Solution


def get_actions_names(txt_file: str) -> list:
    with open(f"Sienna_Invest/{txt_file}.txt", "r") as ft:
        actions_names = []
        txt = ft.readlines()
        for line in txt:
            if line.startswith("Share-"):
                actions_names.append(line[0:10].rstrip("\n"))
        return actions_names


def get_sienna_result(all_actions: list, actions_names: list) -> list:
    sienna_actions = []
    for name in actions_names:
        i = 0
        while i < len(all_actions) and name != all_actions[i].name:
            i += 1
        if i < len(all_actions) and name == all_actions[i].name:
            price = all_actions[i].price
            profit = all_actions[i].profit
            action = Action(name, price, profit)
            sienna_actions.append(action)
    return sienna_actions


def display_sienna_result(i: int):
    print("\n********** Running of Sienna program with the use of Sienna" + str(i) + ".txt **********")
    solution = Solution.optimized(i)
    all_actions = solution.actions
    actions_names = get_actions_names("sienna" + str(i))
    solution.best_actions = get_sienna_result(all_actions, actions_names)
    solution.display_result()


if __name__ == "__main__":
    display_sienna_result(1)
    display_sienna_result(2)

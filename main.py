from time import sleep
from bruteforce import brute_force_result
from optimized import knapsack_result


if __name__ == "__main__":
    brute_force_result()
    sleep(4)
    for i in range(3):
        knapsack_result(i)
        sleep(4)

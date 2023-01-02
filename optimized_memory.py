import tracemalloc
from optimized import knapsack_result


# starting the monitoring
tracemalloc.start()

# function call
knapsack_result(2)

# displaying the size of used memory
print("Case 2 : The size of used memory in bytes :", tracemalloc.get_tracemalloc_memory(), "bytes.")

# stopping the library
tracemalloc.stop()

import tracemalloc
from bruteforce import brute_force_result


# starting the monitoring
tracemalloc.start()

# function call
brute_force_result()

# displaying the size of used memory
print("The size of used memory in bytes :", tracemalloc.get_tracemalloc_memory(), "bytes.")

# stopping the library
tracemalloc.stop()

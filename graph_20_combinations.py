import math
import matplotlib.pyplot as plt
import numpy as np

NUMBER_ACTIONS = 20

list_p = []
list_comb = []
list_comb_sum = []
comb_sum = 0
for p in range(1, NUMBER_ACTIONS + 1):
    list_p.append(p)
    comb = math.factorial(NUMBER_ACTIONS) // (math.factorial(p) * (math.factorial(NUMBER_ACTIONS - p)))
    list_comb.append(comb)
    comb_sum += comb
    list_comb_sum.append(comb_sum)

plt.title(f"Représentation de {2 ** NUMBER_ACTIONS - 1} possibilités de combinaisons")
print("List of comb :\n", list_comb)
xp = np.array(list_p)
plt.xlabel("Number of actions")
yp = np.array(list_comb)
plt.ylabel("Number of combinations")
plt.plot(xp, yp, "ro")
# plt.axis([0, 25, 0, comb_sum+1])
plt.show()

plt.title(f"Représentation de {comb_sum} possibilités de combinaisons")
print("List of comb sum :\n", list_comb_sum)
plt.plot(list_comb_sum, "bo")
plt.xlabel("Number of actions")
plt.ylabel("Number of possibilities")
# plt.axis([0, 25, 0, comb_sum+1])
plt.show()

print("Fin")

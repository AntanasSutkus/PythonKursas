

""" Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10. Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100."""

import random

num_dict = {}

for i in range(1, 11):
    num_dict[i] = random.randint(1,100)

print("Sugeneruotas dictas:")
print(num_dict)

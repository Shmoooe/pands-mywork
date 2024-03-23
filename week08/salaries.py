# Program makes a list called "salaries", that has about 10 random numbers between 20000 - 80000.
# Author: Joanna Kelly

import numpy as np

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

print(salaries)

salaries_plus = salaries + 5000
print(salaries_plus)

salaries_multiply = salaries * 1.05
print(salaries_multiply)

new_salaries = salaries_multiply.astype(int)
print(new_salaries)
# Program creates a list called "ages" that has the same number random values as salaries
# range: 21 to 65
# Make a scatter plot
# Author: JOanna Kelly

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 10

min_age = 21
max_age = 65


np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(min_age, max_age, number_of_entries)

plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = "red")


plt.title("Random Ages and Salaries")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.legend()

#plt.show()

plt.savefig("prettier_plot.png")


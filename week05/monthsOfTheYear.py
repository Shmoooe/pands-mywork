# Creating a tuple that stores the months of the year
# From that tuple, I will create another tuple with just the summer months (May, June, July)
# Then the program will print out the summer months one at a time.

# Author: Joanna Kelly

months_of_the_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

summer_months = months_of_the_year[4:7]

for month in summer_months:
    print(month)


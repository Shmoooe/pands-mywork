# A list of counties and its piechart
# Author: Joanna Kelly

import numpy as np
import matplotlib.pyplot as plt

possible_counties = ["Waterford", "Cork", "Donegal", "Galway", "Limerick"]

counties = np.random.choice(
    possible_counties,
    p= [0.1, 0.3, 0.2, 0.12, 0.28],
    size= (100)
)

unique, counts = np.unique(counties, return_counts= True)
#plt.pie(counts, labels= unique)
plt.bar(unique, counts)

plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        'Week1': [1000, 2000, 3000, 5000, 7000, 8000, 6700],
        'Week2': [4000, 5000, 2500, 4500, 3500, 5000, 5600],
        'Week3': [5000, 6000, 4500, 3500, 2000, 6000, 4800],
        'Week4': [6000, 5000, 2900, 4500, 3500, 4500, 4500]}
df = pd.DataFrame(data)
print(df)

df.set_index('Day', inplace=True)
print(df)
df.plot(kind='bar', figsize=(10, 6))
plt.title('weekly sale data')
plt.xlabel('day of the week')
plt.ylabel('sales amount')
plt.grid(axis='y')
plt.legend(title='Weeks')
plt.show()
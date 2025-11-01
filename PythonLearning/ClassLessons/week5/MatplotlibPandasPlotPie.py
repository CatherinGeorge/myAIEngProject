import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Module': ['AI', 'ML', 'Python', 'Data Structures'],
        'Teamsize': [135, 125, 125, 115]}
df = pd.DataFrame(data)
print(df)

df.set_index('Module', inplace=True)
print(df)
df.plot(kind='pie', figsize=(10, 6), autopct='%1.1f%%', y='Teamsize', legend=True)
plt.title('Module wise Team size')
plt.legend(title='Modules', loc='upper right', bbox_to_anchor=(1.2,1))
plt.show()

       
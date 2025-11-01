import pandas as pd
import numpy as np

first_series = pd.Series([12, 15, 20, 18, 25, 30, 22])
print(first_series)
print(first_series[2:5])
second_series = pd.Series(np.array([10, 20, 23, 45, 50]))
print(second_series.iloc[1:4])
dictionary_data = {"Alex":500, "Steve":200, "Bob":300, "Raj":1000, "Sarvesh":200}
third_series = pd.Series(dictionary_data)
print(second_series)
print(third_series)
print(third_series.loc['Steve'])#Case sensitive
print(third_series.loc['Steve':'Raj'])

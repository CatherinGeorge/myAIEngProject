import pandas as pd

test = pd.Series([80, 85, 78, 90, 88], index = ['B1', 'B2', 'B3', 'B4', 'B5'])
print("Test data: ", test)
print(test.mean())
print(test.idxmax())
print(test.iloc[-1])
print(test.loc['B5'])
print(test - test.mean())

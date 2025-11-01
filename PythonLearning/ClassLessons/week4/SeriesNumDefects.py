import pandas as pd

defects = pd.Series([5, 8, 3, 6, 10, 2, 7])
print("Pandas Series:\n", defects)
defects = pd.Series([5, 8, 3, 6, 10, 2, 7], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print("pandas series with labels Mon, Tue, Wed, Thur, Fri, Sat, Sun: \n", defects) 
print("Find max defects in a day: \n", defects.max())
print("Find min defects in a day: \n", defects.min())
print("use iloc to print the fects count of Day 5:", defects.iloc[4])
print("use loc to print the fects count of Day wed:", defects.loc['Wed'])
print("total defects in week: ", defects.sum())

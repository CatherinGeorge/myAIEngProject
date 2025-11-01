import pandas as pd
import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([30, 40, 50])
dframe1 = pd.DataFrame([array1, array2], columns = ['A', 'B', 'C'])
print(dframe1) 

seriesA = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
seriesB = pd.Series([400, 500], index=['a', 'b'])

dframe2= pd.DataFrame([seriesA, seriesB])
print(dframe2)

TestSheet = {'Mani': pd.Series([10, 20, 30], index=['maths', 'english', 'science']),
             'Clarke': pd.Series([20, 30], index=['maths', 'english'])}
TestResults = pd.DataFrame(TestSheet)
print(TestResults)

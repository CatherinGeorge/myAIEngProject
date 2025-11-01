import pandas as pd
import numpy as np

df = pd.read_csv("test_results.csv")
#df = pd.read_csv(r"C:\Users\CATHERIN\Desktop\Aut_Project\AI Engineer Test Leaf\myAIEngProject\PythonLearning\ClassLessons\week5\test_results.csv")
df = df.set_index('Test Case')
print(df)

#univariate
df['Duration'].describe()

#bivariate
df.groupby("Status")['Duration'].mean()

#Multivariate
df.groupby(['Module', 'Status'])['Defects'].sum()

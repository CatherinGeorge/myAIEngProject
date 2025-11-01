import pandas as pd

data = {'TestcaseID':['TC1', 'TC2', 'TC3', 'TC4', 'TC5'],
        'Status':['Pass','Fail', 'Fail', 'Pass', 'Pass'],
        'Duration':[12, 15, 20, 18, 25]}
df = pd.DataFrame(data)
print(df)

print("Status:", df['Status'])
print("Failed Test Cases:", df[df['Status']=='Fail'])

df.to_csv('test_result.csv', index=False)

df_r = pd.read_csv('test_result.csv')
print(df_r)

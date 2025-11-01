#1 create a DF: Parameters - TC#, Module, Status, Duration
import pandas as pd
import numpy as np

test_cases = [['TC1', 'Login', 'Passed', 12],
              ['TC2', 'Login', 'Failed', 15],
              ['TC3', 'Payement', 'Passed', 20],
              ['TC4', 'Payment', 'Failed', 18],
              ['TC5', 'Reports', 'Passed', 25],
              ['TC6', 'Reports', 'Passed', 22]]
df3 = pd.DataFrame(test_cases, columns=['Testcase', 'Module', 'Status', 'Duration'])
print(df3)

#2 Groups by status and counts passed vs failed
status_counts = df3.groupby('Status')['Testcase'].count()
module_means = df3.groupby('Module')['Duration'].mean()
print(status_counts)
print(module_means)

#1 Create a DF with Defects Details - parameters : DefectID, Module, Severity, Status

defects = [['D1', 'Login', 'High', 'Open'],
           ['D2', 'Payments', 'Low', 'Closed'],
           ['D3', 'Reports', 'Medium', 'Open'],
           ['D4', 'Login', 'Low', 'Closed'],
           ['D5', 'Payment', 'High', 'Open'],]
df4 = pd.DataFrame(defects, columns=['DefectID', 'Module', 'Severity', 'Status'])
print(df4)
openstatus = df4[df4['Status']=='Open']
print(openstatus)
#print all high severity defects
severitydefects = df4[df4['Severity']=='High']
print(severitydefects)
#count how many defects are open vs closed
defectscounts = df4.groupby("Status")["DefectID"].count()
print(defectscounts)


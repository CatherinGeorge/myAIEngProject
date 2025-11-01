import matplotlib.pyplot as plt

teststatus =['Passed', 'Failed', 'Skipped']
noOfCases = [45,10,5]

plt.bar(teststatus, noOfCases, width=0.7, edgecolor='black', color=['green', 'red', 'blue'])
plt.xlabel("Test Status")
plt.ylabel("Number of Test Cases")
plt.title("Test execution results")
plt.show()

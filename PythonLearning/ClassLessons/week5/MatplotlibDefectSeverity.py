import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
fig.suptitle('Test execution and defects Distribution Charts')
data = [12, 15, 20, 18, 22, 30, 25, 16, 19, 28, 24, 14]
axs[0].hist(data, bins=5, color='skyblue', edgecolor='Black', alpha=0.3)
axs[0].set_title('Distribution of Test Execution Times')
axs[0].set_xlabel("Duration(seconds)")
axs[0].set_ylabel("Number of Test Cases")
#axs[0].grid(True)
x= ['High', 'Medium', 'Low']
y= [10, 15, 5]
axs[1].bar(x, y, color='lightgreen', edgecolor='black', alpha=0.7)
axs[1].set_title("Defect Distribution by severity")
axs[1].set_xlabel("Defect Severity")
axs[1].grid(True)
axs[1].legend(["Defects"], loc='upper right')
plt.show()
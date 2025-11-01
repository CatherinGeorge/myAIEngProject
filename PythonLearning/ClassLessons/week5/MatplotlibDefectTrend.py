import matplotlib.pyplot as plt

#step 1: Store defect data
weeks = [1, 2, 3, 4, 5, 6]
defects = [5, 8, 6, 10, 7, 4]

#step2: Plot line chart with markers
plt.plot(weeks, defects, marker='o', color='blue', linestyle='-')

#step3: Add chart title and lables
plt.title("Defect Trend Over Time")
plt.xlabel("Week Number")
plt.ylabel("Number of Defects")

#Step 4: Add grid for better readibility
plt.grid(True)

#Step 5: Display the chart
plt.show()

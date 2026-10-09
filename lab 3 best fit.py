# matplotlib.pyplot is a sub-base of matplotlib，use plt to represent matplotlib.pyplot
import matplotlib.pyplot as plt
# use np to represent numpy
import numpy as np
# Provided coordinates
# array the coordinates of the two axes
x_values = np.array([20, 30, 10, 5])
y_values = np.array([261.1, 239.1, 270.7, 282.3])
# Calculate best fit line using numpy.polyfit
# find the best values of slope and intercept
slope, intercept = np.polyfit(x_values, y_values, 1)
best_fit_line = slope * x_values + intercept
# Prepare the equation in a readable format
# slope in two decimal places and intercept in one decimal place
equation = f"y = {slope:.2f}x + {intercept:.1f}"
# Plot points and best fit line
# set the size of the figure
plt.figure(figsize=(8, 6))
# plot these points in blue with label "Data Points"
plt.scatter(x_values, y_values, color='blue', label='Data Points')
# draw the best fit line in red with label "Best Fit Line"
plt.plot(x_values, best_fit_line, color='red', label='Best Fit Line')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('M$_{grounds}$ (grams)')
plt.ylabel('M$_{brew}$ (grams)')
plt.title('Scatter Plot of M$_{brew}$ versus M$_{grounds}$ with Best Fit Line')
# to place a legend on the axes
plt.legend()
plt.xlim(left=0)  # set x-axis to start from 0
plt.ylim(bottom=0)  # set y-axis to start from 0
# Display the equation on the plot
plt.text(0.95, 0.05, equation, transform=plt.gca().transAxes, fontsize=12, verticalalignment='bottom', horizontalalignment='right')
# show the entire graph
plt.show()
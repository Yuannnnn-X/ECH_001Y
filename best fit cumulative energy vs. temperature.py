import matplotlib.pyplot as plt
import numpy as np
celsius_symbol = "\u00B0C"

# Provided coordinates for two datasets
x_values1 = np.array([23,29,38,49,56,64,73,74,87,95])
y_values1 = np.array([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.08])

x_values2 = np.array([23,26,29,36,40,44,49,54,58,62,66,74,78,82,87,92,95])
y_values2 = np.array([0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.15])

# Calculate best fit lines for both datasets using numpy.polyfit
slope1, intercept1 = np.polyfit(x_values1, y_values1, 1)
slope2, intercept2 = np.polyfit(x_values2, y_values2, 1)

best_fit_line1 = slope1 * x_values1 + intercept1
best_fit_line2 = slope2 * x_values2 + intercept2

# Plot points and best fit lines for both datasets
plt.figure(figsize=(8, 5))

# Plot first dataset
plt.scatter(x_values1, y_values1, color='blue', label='plot of half full kettle (850g)')
plt.plot(x_values1, best_fit_line1, color='red')

# Plot second dataset
plt.scatter(x_values2, y_values2, color='green', label='plot of almost full kettle (1700g)')
plt.plot(x_values2, best_fit_line2, color='orange')

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel(f'Temperature ({celsius_symbol})')
plt.ylabel(f'Cumulative Energy (kW-hr)')
plt.title(f'Best Fit Lines for Cumulative Energy (kW-hr) versus Temperature ({celsius_symbol})')
plt.legend()
plt.xlim(left=20)  # set x-axis to start from 0
plt.ylim(bottom=0)  # set y-axis to start from 0

plt.show()

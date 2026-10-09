import matplotlib.pyplot as plt

# Data points
points = [
    (3.57, 9.15, '20 grind size'),
    (7.14, 13.66, '20 grind size'),
    (14.29, 16.88, '20 grind size'),
    (7.69, 15.05, '35 grind size'),
    (8.33, 13.85, '6 grind size')
]

# Colors for each point
colors = ['red', 'green', 'blue', 'purple', 'orange']

# Create the plot
plt.figure(figsize=(9, 6))
for i, (x, y, grind_size) in enumerate(points):
    plt.scatter(x, y, color=colors[i])
    plt.text(x, y + 0.25, f'{y:.2f}', color=colors[i], ha='center')  # Value above the point
    plt.text(x, y - 0.4, grind_size, color=colors[i], ha='center')  # Condition below the point

# Set titles and labels
plt.title('Flow Rate versus Pressure Gradient')
plt.xlabel('Pressure Gradient (lb cm$^{-1}$)')
plt.ylabel('Flow Rate (cm$^3$ s$^{-1}$)')

# Set axis limits
plt.xlim(2, 19)  # Adjusted x-axis range to better fit your data points
plt.ylim(8, max(y for _, y, _ in points) + 1.5)  # Adjusted y-axis range to fit labels

# Show the plot
plt.show()

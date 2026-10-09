import matplotlib.pyplot as plt

# Data points
points = [
    (9.15, 1.05, '20 grind size'),
    (13.66, 1.03, '20 grind size'),
    (16.88, 1.01, '20 grind size'),
    (15.05, 0.82, '35 grind size'),
    (13.85, 0.95, '6 grind size')
]

# Colors for each point
colors = ['red', 'green', 'blue', 'purple', 'orange']

# Create the plot
plt.figure(figsize=(10, 6))
for i, (x, y, grind_size) in enumerate(points):
    plt.scatter(x, y, color=colors[i])
    plt.text(x, y + 0.02, f'{y:.2f}', color=colors[i], ha='center')  # Value above the point
    plt.text(x, y - 0.03, grind_size, color=colors[i], ha='center')  # Grind size below the point, even closer distance

# Set titles and labels
plt.title('TDS versus Flow Rate')
plt.xlabel('Flow Rate (cm$^3$ s$^{-1}$)')
plt.ylabel('TDS (%)')

# Set axis limits
plt.xlim(8, 18)  # Set x-axis from 9 to 18
plt.ylim(0.7, max(y for _, y, _ in points) + 0.1)  # Set y-axis to start from 0.7

# Show the plot
plt.show()

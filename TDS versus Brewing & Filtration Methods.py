import matplotlib.pyplot as plt

# Data
methods = ['AeroPress, Paper Filter', 'AeroPress, Metal Filter', 'French Press, Coarse Grind', 'French Press, Fine Grind']
TDS = [0.9, 0.95, 0.84, 0.92]

# Plotting the bar chart
plt.figure(figsize=(8, 5))
plt.bar(methods, TDS, color='violet')

# Adding titles and labels
plt.title('TDS versus Brewing & Filtration Methods')
plt.xlabel('Brewing & Filtration Methods')
plt.ylabel('TDS (%)')
plt.ylim(bottom=0)  # Ensure y-axis starts from 0

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

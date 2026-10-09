import matplotlib.pyplot as plt

# Data
methods = ['AeroPress, Paper Filter', 'AeroPress, Metal Filter', 'French Press, Coarse Grind', 'French Press, Fine Grind']
PE = [11.54, 12.22, 8.27, 9.11]

# Plotting the bar chart
plt.figure(figsize=(8, 5))
plt.bar(methods, PE, color='skyblue')

# Adding titles and labels
plt.title('PE versus Brewing & Filtration Methods')
plt.xlabel('Brewing & Filtration Methods')
plt.ylabel('PE (%)')
plt.ylim(bottom=0)  # Ensure y-axis starts from 0

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

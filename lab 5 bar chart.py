import matplotlib.pyplot as plt

# Data
equipment = ['Half full kettle', 'Almost full kettle', 'Fresh roast', 'Popcorn roaster', 'Grinder']
energy_usage = [9.412e-5, 8.824e-5, 1e-3, 7.692e-4, 9.104e-6]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(equipment, energy_usage, color='skyblue')

# Adding titles and labels
plt.title('Energy Usage for Four Different Pieces of Equipment Per Unit Mass Measured in kW-hr/g')
plt.xlabel('Equipment')
plt.ylabel('Energy usage per unit mass (kW-hr/g)')
plt.ylim(bottom=0)  # Ensure y-axis starts from 0

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

import matplotlib.pyplot as plt

# Your data
time_minutes = [1,2,3,4,5,6,7,8,9,10]
TDS = [0.82,0.85,0.78,0.92,0.88,0.94,0.93,0.91,0.96,1.04]

# Creating the scatter plot
plt.figure(figsize=(6, 4))  # Adjust the size as needed
plt.scatter(time_minutes, TDS, color='red')

# Adding titles and labels
plt.title(f'TDS (%) versus Extraction Time (minutes)')
plt.xlabel(f'Extraction Time (minutes)')
plt.ylabel(f'TDS (%)')

# Set the limits for both axes
plt.xlim(0, max(time_minutes) + 1)  # Adding a bit of space beyond the largest x value for clarity
plt.ylim(0, max(TDS) + 0.25)  # Adding some space beyond the largest y value

# Show the plot
plt.show()

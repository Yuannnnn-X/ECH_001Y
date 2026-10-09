import matplotlib.pyplot as plt

# Your data
time_seconds = [0,5,10,15,20,25,30,35,40,45,50,55,60]
pH = [5.94,5.79,5.74,5.68,5.64,5.58,5.53,5.48,5.44,5.41,5.37,5.36,5.33]

# Creating the scatter plot
plt.figure(figsize=(10, 6))  # Adjust the size as needed
plt.scatter(time_seconds, pH, color='r')

# Adding titles and labels
plt.title('Scatter Plot of the pH versus Time with Dark Roasted Coffee')
plt.xlabel('Time (minutes)')
plt.ylabel('pH (no unit)')

# Set the limits for both axes
plt.xlim(0, max(time_seconds) + 5)  # Adding a bit of space beyond the largest x value for clarity
plt.ylim(4, max(pH) + 2)  # Adding some space beyond the largest y value

# Show the plot
plt.show()

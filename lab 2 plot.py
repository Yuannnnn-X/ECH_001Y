import matplotlib.pyplot as plt

# Your data
time_seconds = [35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185, 200, 215, 230, 245, 260, 275, 290, 305, 320]
temperature_celsius = [76, 88, 85, 90, 87, 84, 88, 86, 89, 101, 101, 101, 101, 95, 92, 89, 87, 85, 83, 81]

# Creating the scatter plot
plt.figure(figsize=(10, 6))  # Adjust the size as needed
plt.scatter(time_seconds, temperature_celsius, color='b')

# Adding titles and labels
plt.title('Temperature in Mr. Coffee Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (Celsius)')

# Set the limits for both axes
plt.xlim(0, max(time_seconds) + 10)  # Adding a bit of space beyond the largest x value for clarity
plt.ylim(0, max(temperature_celsius) + 10)  # Adding some space beyond the largest y value

# Optional: Add a grid for better readability
plt.grid(True)

# Show the plot
plt.show()

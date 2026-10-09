import matplotlib.pyplot as plt

# Data
brews = ['35 Grind Size', '20 Grind Size', '5 Grind Size', '70 Celsius Temperature', '99 Celsius Temperature', '1 Minute Extraction Time']
TDS = [0.48, 0.63, 0.96, 0.82, 0.78, 0.82]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(brews, TDS, color='pink')

# Adding titles and labels
plt.title('TDS Value for Different Brews')
plt.xlabel('Brew Type')
plt.ylabel('TDS (%)')
plt.ylim(bottom=0, top=1.6)  # Ensure y-axis starts from 0

# Display the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# Add text labels at the bottom of each bar within the red portion, lowered slightly
for bar, tds, label in zip(bars, TDS, ["faint, watery", "lighter, neutral", "extremely bitter", "slightly sour", "medicinal", "sour"]):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.05, f'{tds:.2f}', ha='center', va='top')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03, label, ha='center', va='bottom')

plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()

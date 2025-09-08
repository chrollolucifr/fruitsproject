import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("fruits.csv")

# Display the first few rows
print(df.head())

# Plotting the nutritional values
df.plot(x='Fruit', y=['Calories', 'Protein', 'Fat', 'Carbohydrates'], kind='bar')
plt.title('Nutritional Values of Fruits')
plt.xlabel('Fruit')
plt.ylabel('Nutritional Value (g)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


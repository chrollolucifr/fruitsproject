import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv("data.csv") 
print(df.head()) 
df.plot() 
plt.show() 

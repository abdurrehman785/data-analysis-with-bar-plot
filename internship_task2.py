import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv('E:\\ML datasets\\Car_Price_Prediction.csv')

mean = data['Price'].mean()

median = data['Price'].median()

mode = data['Price'].mode()

range = data['Price'].max() - data['Price'].min()

print("Mean:" , mean)
print("Median:" , median)
print("Mode:" , mode)
print("Range: ", range)

year_counts = data['Year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(year_counts.index.astype(str), year_counts.values)

plt.xlabel('Year')
plt.ylabel('Number of Cars')
plt.title('Number of Cars by Year')
plt.xticks(rotation=45)  # rotate labels if overlapping

plt.tight_layout()
plt.show()
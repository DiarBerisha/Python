from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

nobel_prizes_by_continent = df.groupby('Continent')['Nobel Prices'].sum()
no_of_continents = nobel_prizes_by_continent.count()
print(no_of_continents)

colors = ['black', 'yellow', 'blue', 'green', 'pink', 'lightblue']
plt.figure(figsize=(10,10))

nobel_prizes_by_continent.plot(kind='pie',colors=colors, autopct= '%1.1f%%')
plt.title('Distribution of Nobel Prizes by Continent')
plt.axis('equal')
plt.ylabel('')

plt.tight_layout(

)
plt.show()
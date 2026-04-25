import pandas as pd
from numpy.ma.extras import average

data = pd.read_csv('avgIQpercountry.csv')


first_rows = data.head(10)
print(first_rows)

last_rows = data.tail(10)
print(last_rows)

data.sample(n=5)
data.sample(frac=0.5)

country_data = data['Country']
print(country_data)

subset = data[['Country','Average IQ']]
print(subset)

filtered_data = subset[subset['Average IQ'] > 100]
print(filtered_data)

null_mask = data.isnull()
null_count = null_mask.sum()
print('null values:')
print(null_count)

data.dropna(inplace=True)
print('\nDataset after delete:')
print(data.info())

duplicated_count = data.duplicated().sum()
print(' \nCount of dupli: ')
print(duplicated_count)

data.drop_duplicates(keep='last', inplace=True)

data['Population - 2023'] = data['Population - 2023'].apply(lambda x:float(x.replace(',',"")))
print(data.info())

average_iq_per_continent = data.groupby('Continent')['Averaqe IQ'].mean()
print(average_iq_per_continent)

sorted_average_iq_per_continent = average_iq_per_continent.sort_values(ascending =False)
print(sorted_average_iq_per_continent)

total_nobel_by_country = data.groupby('Country')['Nobel Prize'].sum()
sorted_total_nobel_by_country = total_nobel_by_country.sort_values(ascending=False)
print(sorted_total_nobel_by_country)
sorted_total_nobel_nonzero = sorted_total_nobel_by_country[sorted_total_nobel_by_country !=0]
print('total pa shtete me zero qmime',sorted_total_nobel_nonzero)
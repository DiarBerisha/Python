
import pandas as pd

products = ['Apples', 'Oranges', 'Pineapples']

sales = [150,200,180]

sales_series = pd.Series(sales, index=products)

print(sales_series)

print(sales_series['Pineapples'])

total_sales = sales_series.sum()

print(total_sales)

best_selling = sales_series.idxmax()
print(best_selling)

data = {'Name': ['Diar', 'Milot', 'Donart'],
        'Age': [17, 25, 20],
        'City': ['Lipjan','Prishtine','Prishtine']
        }

klasa = pd.DataFrame(data)
print(klasa)

klasa = pd.read_csv('klasa.csv')
print(klasa)
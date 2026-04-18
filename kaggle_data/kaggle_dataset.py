import pandas as pd

data = pd.read_csv('avgIQpercountry.csv')


first_rows = data.head(10)

last_rows = data.tail(10)
print(first_rows)
print(last_rows)
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.stats import linregress

# Wczytanie pliku CSV do ramki danych
df = pd.read_csv('1895-2023.csv')

# Nadanie polskich nazw kolumnom ramki
df = df.rename(columns={'Date': 'Data', 'Value': 'Temperatura', 'Anomaly': 'Odchyłka'})

# Zmiana F na C
df['Temperatura'] = (df['Temperatura'] - 32) * 5/9
df['Odchyłka'] = (df['Odchyłka']) * 5/9
# Zaokraglenie do .00
df = df.round(2)

# Wyświetlenie statystyk opisowych
print(df.describe())

# Obliczenie prognozy na podstawie regresji liniowej
x = df['Data']
y = df['Temperatura']
linear_regression = linregress(x, y)
prognoza = linear_regression.slope * 2023 + linear_regression.intercept
print(f'Prognozowana średnia maksymalna temperatura styczniowa w 2023 roku: {prognoza:.2f}')

# Wizualizacja regresji liniowej w szeregu czasowym
sns.regplot(x='Data', y='Temperatura', data=df)
plt.show()
import pandas as pd
import csv

from matplotlib import pyplot as plt

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
titanic.columns = ['Nazwisko i Imię', 'Ocalały?', 'Płeć', 'Wiek', 'Klasa']

youngest_passenger = titanic['Wiek'].min()
youngest_person = titanic[titanic['Wiek'] == youngest_passenger]
print("Najmłodszy pasażer: \n", youngest_person)

oldest_passenger = titanic['Wiek'].max()
oldest_person = titanic[titanic['Wiek'] == oldest_passenger]
print("\nNajstarszy pasażer: \n", oldest_person)

mean = titanic['Wiek'].mean()
print("\nŚrednia wieku: ", mean)

alive_stats = titanic.groupby('Ocalały?').describe()
print("\nStatystyki pasażerów według kolumny: 'Ocalały?': \n", alive_stats)
# Używam & bo pandas uważa "or, and" jako dwuznaczne, a Znaki "& |" są dla nas overloadowane w tym przypadku i działają jak "or, and"
women_firstClass = titanic[(titanic['Płeć'] == 'female') & (titanic['Klasa'] == '1st')]

youngest_women = women_firstClass['Wiek'].min()
print("\nNajmłodsza kobieta z pierwszej klasy: ", youngest_women)

oldest_women = women_firstClass['Wiek'].max()
print("Najstarsza kobieta z pierwszej klasy: ", oldest_women)

alive_stats_women = women_firstClass.groupby('Ocalały?').describe()
print("Statystyki kobiet z pierwszej klasy według kolumny: 'Ocalały?':\n", alive_stats_women)

titanic.hist()
plt.title("Wiek pasażerów")
plt.xlabel("Wiek [Lata]")
plt.ylabel("Ilość Wystąpień")
plt.show()

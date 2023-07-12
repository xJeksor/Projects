import csv
import statistics as st
import matplotlib.pyplot as plt

with open('Dane.csv', 'r', encoding="utf-8") as csvfile:
    next(csvfile)  # Skipping 1st line
    data = list(csv.reader(csvfile))
names = []
number_str = []
for element in data:
    names.append(element[0])
    number_str.append(element[1])

number = [int(x) for x in number_str if x != '']  # Change str to int and skip empty strings

mean = st.mean(number)
median = st.median(number)
mode = st.mode(number)
pvariance = st.pvariance(number)
pstdev = st.pstdev(number)

print("Średnia:",mean)
print("Mediana:",median)
print("Moda:",mode)
print("Wariancja:",pvariance)
print("Odchylenie standardowe:",pstdev)

plt.hist(number)
plt.title("Histogram of Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()






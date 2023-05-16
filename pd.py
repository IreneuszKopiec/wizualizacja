import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.genfromtxt('kandydaci_utf8.csv', delimiter=";",  dtype=('|U16'), encoding='utf_8')
df = pd.DataFrame(data[1:], columns=data[0])
print(df.columns)
print()
df['"Wiek"'] = df['"Wiek"'].astype(int)
srednia_wiek = df['"Wiek"'].mean()
print("Średnia wieku: ", round(srednia_wiek, 2))
wiek_list = df['"Procent wszystk'].str.replace('"', '').replace(',', '.').tolist()
liczby = [float(element.replace(',', '.')) for element in wiek_list]
max_w = max(liczby)
print(max_w)

# grupowanie
# 1
gr1 = df.groupby('"Wiek"').size()
print(gr1)
# 2
gr2 = df.groupby('"Wiek"').mean()
print(gr2)
# 3
gr3 = df.groupby('"Wykształcenie"').size()
print(gr3)
# 4
gr4 = df.groupby('"Wykształcenie"')['"Wiek"'].mean()
print(gr4)
# 5
gr5 = df.groupby('"Wykształcenie"')['"Wiek"'].max()
print(gr5)

# filtrowanie
# 1
f1 = df[df['"Wiek"'] >= 50]
print(f1)
# 2
f2 = df[df['"Wiek"'] == 48]
print(f2)
# 3
f3 = df[(df['"Wiek"']) >= 40 & (df['"Wiek"'] <= 45)]
print(f3)
# 4
f4 = df[(df['"Wiek"']) >= 50 | (df['"Zawód"'] == '"pracownik samorządowy"')]
print(f4)
# 5
f5 = df[df['"Wiek"'] != 48]
print(f5)

# wiek = df['"Wiek"'].tolist()
# print(wiek)
# plt.hist(liczby, bins=range(min(wiek), max(wiek) +2, 2), color='green')
# plt.title('Rozkład wieku')
# plt.xlabel('Wiek')
# plt.ylabel('Liczba osób')
# plt.xticks(np.arange(min(wiek), max(wiek) + 2, 2))
# plt.show()

data2 = np.genfromtxt('covid.csv', delimiter=";",  dtype=('|U16'), encoding='ISO-8859-1')
df2 = pd.DataFrame(data2[1:], columns=data2[0])
print(df2.columns)
print(df2['"plec"'])
# grupowanie
# 1
gr12 = df2.groupby('"plec"').size()
print(gr12)
# 2
gr22 = df2.groupby('"plec"').max()
print(gr22)
# 3
gr32 = df2.groupby('"plec"').min()
print(gr32)
# 4
gr42 = df2.groupby('"teryt_woj"')['"plec"'].size()
print(gr42)
# 5
gr52 = df2.groupby('"teryt_woj"')['"teryt_pow"'].max()
print(gr52)

# filtrowanie
# 1
f12 = df2[df2['"teryt_woj"'] == '"4"']
print(f12)
# 2
f22 = df2[df2['"kat_wiek"'] == '"65-74"']
print(f22)
# 3
f32 = df2[(df2['"teryt_pow"']) == 4 & (df2['"teryt_pow"'] == 12)]
print(f32)
# 4
f42 = df2[(df2['"teryt_pow"']) == 407 | (df2['"kat_wiek"'] == '65-74')]
print(f42)
# 5
f5 = df2[df2['"teryt_pow"'] != 4]
print(f5)

przedzial = df2['"kat_wiek"'].tolist()
liczby = list(set(przedzial))
print(liczby)
word_counts = {}
for word in przedzial:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
plt.bar(word_counts.keys(), word_counts.values())
plt.xlabel('Słowo')
plt.ylabel('Liczba powtórzeń')
plt.title('Liczba powtórzeń słów')
plt.show()

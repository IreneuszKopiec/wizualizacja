import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.genfromtxt('jajka2023.csv', delimiter=";",  dtype=('|U16'), encoding='utf_8')

listaCen = [[float(el.replace(',', '.')) for el in row[1:] if el != ""] for row in data[1:]]
ceny = []
for row in listaCen:
    for el in row:
        ceny.append(el)
sredniaCena = sum(ceny) / len(ceny)
print(round(sredniaCena, 2))
print()
miasta = data[0][1:]
sklepy = [row[0] for row in data[1:]]
ceny = [[float(el.replace(',', '.')) if el != "" else el for el in row[1:]] for row in data[1:]]

minCena = ceny[0][0]
maxCena = ceny[0][0]

maxIndeksMiasta = miasta[0]
minIndeksMiasta = miasta[0]
maxIndeksSklepu = sklepy[0]
minIndeksSklepu = sklepy[0]

for indeksSklepu, row in enumerate(ceny):
    for indeksMiasta, cena in enumerate(row):
        if cena == "":
            continue
        if minCena > cena:
            minCena = cena
            minIndeksMiasta = indeksMiasta
            minIndeksSklepu = indeksSklepu
        if maxCena < cena:
            maxCena = cena
            maxIndeksMiasta = indeksMiasta
            maxIndeksSklepu = indeksSklepu

print(maxIndeksMiasta)
print(minIndeksMiasta)
print(maxIndeksSklepu)
print(minIndeksSklepu)
print()

miasta = data[0][1:]
ceny = [[cena.replace(',', '.') if cena != "" else 0 for cena in row] for row in data[1:][1:]]
df = pd.DataFrame(ceny)

dicto = {miasto: 'float' for miasto in miasta}
df.columns = data[0]
print(df)
print()

data = pd.read_csv('jajka2023.csv', sep=';', index_col=0, encoding='UTF=8')
data2 = data.stack()
data3 = data2.str.replace(',', '.').astype('float')
srednia = data3.mean()
minCena = data3.min()
maxCena = data3.max()
print(data3[data3 == minCena])
print(data3[data3 == maxCena])
print()

pd.DataFrame.plot(kind='box')
plt.show()

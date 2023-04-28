import numpy as np

# program81
my_array = np.array([x for x in range(10, 40) if x % 2 == 0])
print(my_array)
print(np.shape(my_array))
print(np.reshape(my_array, (5, 3)))
print(np.resize(my_array, (3, 4)))
my_array = [x+3 for x in my_array]
print(my_array)
my_array = [3*x for x in my_array]
print(my_array)
my_array = np.array([x for x in range(10, 40) if x % 2 == 0])
for x in range(len(my_array)):
    if my_array[x] % 6 == 2:
        my_array[x] = 0
print(my_array)


def change(a, x):
    new_array = a
    for i in range(len(new_array)):
        if a[i] == 0:
            a[i] = x
    return new_array


my_array2 = change(my_array, 5)
print(my_array2)


# program82
A = np.array([[1, 1, 2],
              [2, 1, 0],
              [4, 1, 2]])
B = np.array([[2, 5, 7],
              [2, 8, 0],
              [4, 3, 1]])
print(A)
print(B)
print(A+B)
print(A*B)
for x in A:
    print(x)
print(A**5)
C = np.array([[1], [2], [4]])
print(C)
D = np.array([2, 5, 7])
print(D)
print(C*D)
print(C+D)
E = np.array([[1, 5], [2, 1]])
F = np.array([[2, 1], [2, 8]])
print(E/F)
print(F/E)
print(E % F)

# program83
panstwa = np.array(['Chiny', 'Japan', 'Germany', 'USA', 'South Korea',
                    'India', 'Brazil', 'Mexico', 'Spain', 'Russia'])
r1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
r2014 = np.array([19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69])
print(panstwa)
print(r1999)
print(r2014)
wzrost = []
for x in range(len(panstwa)):
    wzrost_kraju = ((r2014[x] - r1999[x]) / r1999[x]) * 100
    wzrost.append(wzrost_kraju)
print("Wzrost produkcji w poszczególnych krajach:")
for x in range(len(panstwa)):
    print(f"{panstwa[x]}: {wzrost[x]:.2f}%")
najmniej_1999 = panstwa[np.argmax(r1999)]
najwiecej_1999 = panstwa[np.argmin(r1999)]
najmniej_2014 = panstwa[np.argmax(r2014)]
najwiecej_2014 = panstwa[np.argmin(r2014)]
print(najmniej_1999)
print(najwiecej_1999)
print(najmniej_2014)
print(najwiecej_2014)
print()
result = []
for x in range(len(panstwa)):
    if r2014[x] < r1999[x]:
        result.append(panstwa[x])
for x in range(len(result)):
    print(f"{result[x]}")
# program84
imiona = np.array(['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary',
                   'Zenon', 'Filip', 'Adrian'])
wiek = np.array([21, 40, 13, 31, 34, 14, 13, 28, 20, 15])
plec = np.array(['K', 'K', 'K', 'K', 'K', 'M', 'M', 'M', 'M', 'M'])
waga = np.array([65, 80, 64, 69, 74, 61, 66, 61, 69, 77])
wzrost2 = np.array([179, 179, 151, 177, 170, 157, 151, 153, 160, 160])
okulary = np.array([False, True, False, True, False, True, False, True, False, True])
print(imiona)
print(wiek)
print(plec)
print(waga)
print(wzrost2)
print(okulary)
print()
print(np.sort(imiona))
print()
print(imiona[okulary])
print()
print(imiona[(20 >= wiek)*(wiek <= 30)*(plec == 'K')])
print(imiona[(20 >= wiek) & (wiek <= 30) & (plec == 'K')])
print()
waga_wzrost_nieokularnicy = []
for x in range(len(imiona)):
    if (waga[x] >= 60 and waga[x] <= 80) and (wzrost2[x] >= 160 and wzrost2[x] <= 180):
        if not okulary[x]:
            waga_wzrost_nieokularnicy.append(imiona[x])
print(waga_wzrost_nieokularnicy)
print()
bmi = []
for x in range(len(imiona)):
    wynik = waga[x]/(wzrost2[x]**2)
    bmi.append(wynik)
print(bmi)
print()
sredni_wiek = np.mean(wiek)
print(sredni_wiek)
indeks = (np.abs(wiek - sredni_wiek)).argmin()
print(imiona[indeks])

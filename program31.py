import math

list1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(15):
    a = i ** 5
    list1[i] = a

print(list1)

list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


def silnia(el):
    wynik = 1
    if el == 1:
        return 1
    for i in range(el):
        wynik = wynik * (i+1)
    return wynik


for i in range(20):
    list2[i] = silnia(i)


print(list2)

list3 = []
for i in range(20):
    if i == 0:
        list3.append(1)
    else:
        list3.append(math.e**i)

print(list3)

list4 = ["Adam","Maciek","Jan"]
list5 = []

for i in range(3):
    list5.append(len(list4[i]))

print(list5)

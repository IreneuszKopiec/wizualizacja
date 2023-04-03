import math

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list3 = list1 + list2
print(list3)
list4 = []

for i in range(10):
    list4.append(list1[i]+list2[i])

print(list4)

list5 = ["marzec", "styczen", "luty", "pazdziernik", "listopad",
         "grudzien", "kwiecien", "maj", "czerwiec", "lipiec", "sierpien", "wrzesien"]
list6 = []


def miesiace(el):
    if el == "styczen":
        return 1
    if el == "luty":
        return 2
    if el == "marzec":
        return 3
    if el == "kwiecien":
        return 4
    if el == "maj":
        return 5
    if el == "czerwiec":
        return 6
    if el == "lipiec":
        return 7
    if el == "sierpien":
        return 8
    if el == "wrzesien":
        return 9
    if el == "pazdziernik":
        return 10
    if el == "listopad":
        return 11
    if el == "grudzien":
        return 12
    if el == 1:
        return "styczen"
    if el == 2:
        return "luty"
    if el == 3:
        return "marzec"
    if el == 4:
        return "kwiecien"
    if el == 5:
        return "maj"
    if el == 6:
        return "czerwiec"
    if el == 7:
        return "lipiec"
    if el == 9:
        return "sierpien"
    if el == 10:
        return "wrzesien"
    if el == 11:
        return "pazdziernik"
    if el == 11:
        return "listopad"
    if el == 12:
        return "grudzien"


list7 = []


for i in range(12):
    list6.append(miesiace(list5[i]))
list6.sort()
for i in range(12):
    list7.append(miesiace(list6[i]))
print(list7)

list8 = ["Nowak", "Kowalski", "Boruc"]
litera = "B"


def func1(lista=[], el=litera):
    wynik = [x for x in lista if x[0] > el]
    return wynik


print(func1(list8, litera))
newlist = [x for x in list8 if len(x) > 6]
print(newlist)


def func2(lista=[]):
    for k in range(len(lista)):
        if k > 0:
            if lista[k] > lista[k-1]:
                return False
    return True


list9 = [1, 2, 3, 4, 5]
list10 = [5, 4, 3, 2, 1]
print("Przypadek 1")
print(func2(list9))
print("Przypadek 2")
print(func2(list10))


def func3(lista=[]):
    newlist2 = [x ** 3 for x in lista]
    return newlist2


print("Przypadek 1")
print(func3(list9))
print("Przypadek 2")
print(func3(list10))
list11 = [1.2, 1.5, 2.9]
n1 = 1.2
n2 = 2.1


def func4(lista=[], x=n1, y=n2):
    newlist3 = []
    for a in range(len(lista)):
        if math.isclose(lista[a], x):
            newlist3.append(y)
        else:
            newlist3.append(lista[a])
    return newlist3


print(func4(list11, n1, n2))

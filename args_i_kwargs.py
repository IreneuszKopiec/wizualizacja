import math

names = ['michal', 'nela', 'ola', 'przemek']
list1 = [x[0].upper()+x[1:] for x in names]
print(list1)
list2 = [x for x in names if x.find('l') >= 0]
print(list2)
list3 = [x for x in list1 if x[-1] == 'a']
list3 = tuple(list3)
print(list3)
list4 = [len(x) for x in names]
suma = sum(list4)
print(suma)


def iloczyn(*num):
    wynik = 1
    for x in num:
        wynik *= x
    return wynik


print("Wynik = ", iloczyn(1, 2, 3, 4, 5))
print("Wynik = ", iloczyn(3, 4, 5))


def suma_entych_poteg(n, *num):
    s = 0
    for x in num:
        s += x**n
    return s


print("Wynik = ", suma_entych_poteg(1, 2, 3, 4, 5))
print("Wynik = ", suma_entych_poteg(3, 4, 5))


def mean(*num):
    result = sum(num)
    srednia = float(result)/len(num)
    return srednia


print("Wynik = ", mean(1, 2, 3, 4, 5, 1))
print("Wynik = ", mean(3, 4, 5, 9))


def gmean(*num):
    r = iloczyn(*num)
    d = len(num)
    srednia = math.pow(r, 1/d)
    return srednia


print("Wynik = ", gmean(1, 2, 3, 4, 5, 1))
print("Wynik = ", gmean(3, 4, 5, 9))


def sumaryczna_dlugosc(*sstr):
    w = 0
    for x in sstr:
        w += len(x)
    return w


print("Wynik = ", sumaryczna_dlugosc("slowo", "klucz"))


def func1(**data):
    for x, y in data.items():
        print("{} ma numer {}".format(x, y))


print("przypadek 1")
func1(Irek=123456789, Jan=987654321)
print("przypadek 1")
func1(Irek=765432189, Jan=975358123, Jacek=321654987)


def func2(**data):
    result1 = 0
    pomoc = []
    result2 = 1
    n = 0
    poprzedni = 0
    for x, y in data.items():
        result1 += y
        n += 1
    for x, y in data.items():
        pomoc.append(y)
    for x in range(len(pomoc)):
        if x == 0:
            poprzedni = pomoc[x]
        else:
            result2 *= (pomoc[x]/poprzedni)
            poprzedni = pomoc[x]
    avg = round(result1/n, 2)
    print(avg)
    avg_g = round(math.pow(result2, 1/(n-1)),5)
    print(avg_g)


print("przypadek 1")
func2(styczen=10000, luty=15000, marzec=18000)
print("przypadek 2")
func2(styczen=100000, luty=130000, marzec=190000, kwiecien=230000,
      maj=260000, czerwiec=310000, lipiec=290000, sierpien=270000,
      wrzesien=280000, pazdziernik=250000, listopad=230000,
      grudzien=190000)

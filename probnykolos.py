def func1(lista):
    newlist = []
    for x in lista:
        if x not in newlist:
            newlist.append(x)
    for y in newlist:
        print(y)


list1 = [1, 2, 3, 4, 4, 3, 8, 1, 2]
func1(list1)

str1 = "Witaj jak moge p omoc"
sort_str = "".join(z for z in str1 if z.isalnum())
new_str = sort_str[::-4]
print(new_str)


def rek1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rek1(n-1)+rek1(n-2)


print(rek1(10))


def rek2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    pp = 0
    p = 1
    t = 0
    for i in range(2, n+1):
        t = pp + p
        pp, p = p, t
    return t


print(rek2(10))


def iloczyn(*num, n):
    wynik = 0
    for a in num:
        wynik += a**n
    return wynik


print(iloczyn(1, 2, 3, 4, 5, n=2))

list2 = ['apple', 'banana',
         'pomergranate', 'plum',
         'orange', 'melon', 'cherry',
         'watermelon']
newlist2 = [len(b) for b in list2 if 'u' in b or 'o' in b]
print(newlist2)


def silnia(n):
    if n == 0 or n == 1:
        return 1
    wynik = 1
    for x in range(2, n+1):
        wynik *= x
    return wynik


def newton(n, k):
    return silnia(n)/(silnia(k)*silnia(n-k))


print(newton(6, 4))


class Polynomial:
    def __init__(self, w):
        self.w = w

    def dodaj(self, w, w2):
        for x in range(len(w)):
            w[x] -= w2[x]
        return w

    def odejmij(self, w, w2):
        for x in range(len(w)):
            w[x] -= w2[x]
        return w

    def pokaz(self):
        a = self.w[0]
        b = self.w[1]
        c = self.w[2]
        print("{}x^2-{}x^1+{}".format(a, b, c))


wielomian = Polynomial([3, 4, 2])
wielomian.pokaz()
kolejny = Polynomial([4, 4, 7])
kolejny.pokaz()

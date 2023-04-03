krotka = (12, 123, 1, 12)


def func1(element, krotk=()):
    x = list(krotk)
    x.append(element)
    nowa = tuple(x)
    return nowa


def func2(element, krotk=()):
    y = list(krotk)
    y.remove(element)
    nowa = tuple(y)
    return nowa


print(func1(2, krotka))
print(func2(2, func1(2, krotka)))


def func3(krot=()):
    z = []
    for x in krot:
        if krot.count(x) == 1:
            print(x)
        else:
            z.append(x)
    for i in range(len(z)):
        b = True
        j = 0
        while j < i:
            if z[i] == z[j]:
                b = False
                break
            j += 1
        if b:
            print(z[i])


func3(krotka)

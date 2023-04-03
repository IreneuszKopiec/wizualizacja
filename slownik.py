slownik = {
    "Irek": 123456789,
    "Mateusz": 987654321
}


def func1(objekt):
    for x, y in objekt.items():
        print(x, "ma numer ", y)


func1(slownik)
slownik["Janusz"] = 333333333
func1(slownik)
slownik.pop("Janusz")
func1(slownik)
slownik["Irek"] = 987656781
func1(slownik)



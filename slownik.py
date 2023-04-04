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

dni = {
    "1": "poniedzialek",
    "2": "wtorek",
    "3": "sroda",
    "4": "czwartek",
    "5": "piatek",
    "6": "sobota",
    "7": "niedziela"
}


def zamien1(objekt):
    objekt["1"] = "Monday"
    objekt["2"] = "Tuesday"
    objekt["3"] = "Wednesday"
    objekt["4"] = "Thursday"
    objekt["5"] = "Friday"
    objekt["6"] = "Saturday"
    objekt["7"] = "Sunday"


def zamien2(objekt):
    objekt["1"] = "poniedzialek"
    objekt["2"] = "wtorek"
    objekt["3"] = "sroda"
    objekt["4"] = "czwartek"
    objekt["5"] = "piatek"
    objekt["6"] = "sobota"
    objekt["7"] = "niedziela"


def wypisz(objekt):
    for x, y in objekt.items():
        print(y)


wypisz(dni)
zamien1(dni)
wypisz(dni)
zamien2(dni)
wypisz(dni)


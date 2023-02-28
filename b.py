import math
a = int(input("Podaj a "))
b = int(input("Podaj b "))
p = math.gcd(a, b)


if p == 1:
    p = a
    q = b
    print(p, q)
else:
    print("Skracalny")

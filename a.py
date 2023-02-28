
n = int(input("Podaj n "))


if 0 < n < 100:
    for i in range(1, n + 1):
        for j in range(1, n+1):
            x = i*j
            print(i, "*", j, "=", x)
else:
    print("n is too large")

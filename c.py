import math
n = 5
e1 = math.pow((1+(1/n)), n)
k = 0
tab = []
for i in range(0, n):
    tab.append(1/(math.factorial(k)))
    k = k+1

e2 = math.fsum(tab)

print(e1, e2)
print(math.e)

w1 = e1-math.e
w2 = e2-math.e
if w1 < 0:
    w3 = w1*(-1)
else:
    w3 = w1
if w2 < 0:
    w4 = w2 * (-1)
else:
    w4 = w2
print(w1, w2, w3, w4)

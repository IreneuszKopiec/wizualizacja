import numpy as np

# program81
my_array = np.array([x for x in range(10, 40) if x % 2 == 0])
print(my_array)
print(np.shape(my_array))
print(np.reshape(my_array, (5, 3)))
print(np.resize(my_array, (3, 4)))
my_array = [x+3 for x in my_array]
print(my_array)
my_array = [3*x for x in my_array]
print(my_array)
my_array = np.array([x for x in range(10, 40) if x % 2 == 0])
for x in range(len(my_array)):
    if my_array[x] % 6 == 2:
        my_array[x] = 0
print(my_array)


def change(a, x):
    new_array = a
    for i in range(len(new_array)):
        if a[i] == 0:
            a[i] = x
    return new_array


my_array2 = change(my_array, 5)
print(my_array2)


# program82
A = np.array([[1, 1, 2],
              [2, 1, 0],
              [4, 1, 2]])
B = np.array([[2, 5, 7],
              [2, 8, 0],
              [4, 3, 1]])
print(A)
print(B)
print(A+B)
print(A*B)
for x in A:
    print(x)
print(A**5)
C = np.array([[1], [2], [4]])
print(C)
D = np.array([2, 5, 7])
print(D)
print(C*D)
print(C+D)
E = np.array([[1, 5], [2, 1]])
F = np.array([[2, 1], [2, 8]])
print(E/F)
print(F/E)
print(E % F)

# program83
panstwa = np.array(['Chiny', 'Japan', 'Germany', 'USA', 'South Korea',
                    'India', 'Brazil', 'Mexico', 'Spain', 'Russia'])
r1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
print(panstwa)

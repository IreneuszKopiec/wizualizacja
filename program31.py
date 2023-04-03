import math

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
newlist1 = [x**5 for x in list1]
print(newlist1)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

newlist2 = [math.factorial(x) for x in list2]


print(newlist2)

list3 = []
for i in range(20):
    list3.append(i)

newlist3 = [math.e**x for x in list3]
print(newlist3)

list4 = ["Adam", "Maciek", "Jan"]
list5 = [len(x) for x in list4]

print(list5)

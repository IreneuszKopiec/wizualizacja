lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
lists

lists = [[] for i in range(15)]
for i in range(15):
    lists[i].append(i)


print(lists)

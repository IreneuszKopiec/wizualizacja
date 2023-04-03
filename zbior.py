zbior = {'Polska', 'Niemcy', 'Ukraina', 'Anglia', 'USA'}
zbior.add('Wlochy')
print(zbior)

if 'Polska' in zbior:
    print("Jest")
else:
    print("Nie ma")

zbior.remove('Wlochy')
print(zbior)

zbior2 = {'Warszawa', 'Berlin', 'Londyn', 'Lwow', 'NYC'}
zbior3 = {'Sochaczew', 'Berlin', 'Liverpool', 'Lwow', 'NYC'}
zbior2.update(zbior3)
print(zbior2)
zbior2 = {'Warszawa', 'Berlin', 'Londyn', 'Lwow', 'NYC'}
zbior3 = {'Sochaczew', 'Berlin', 'Liverpool', 'Lwow', 'NYC'}
print(zbior2.intersection(zbior3))
print(zbior2.difference(zbior3))

if zbior2.issuperset(zbior3):
    print("tak")
else:
    print("nie")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('penguins.csv', delimiter=",", encoding='utf_8', index_col=False)
print(data)
data = data.dropna()
print(data)
print(data.groupby('sex')['body_mass_g'].mean())
print(data.groupby(['sex', 'species'])['body_mass_g'].mean())
max_waga = data['body_mass_g'].max()
min_waga = data['body_mass_g'].min()
print(data[data['body_mass_g'] == max_waga])
print(data[data['body_mass_g'] == min_waga])
print(data.groupby('island').size())
# data.groupby('island').size().plot.bar()
x = data['bill_length_mm']
y = data['bill_depth_mm']
colors = {'MALE': 'b', 'FEMALE': 'r'}
print(data.groupby('species').size())
markers = {'Adelie': "<", 'Chinstrap': ",", 'Gentoo': "o"}
for species in data['species'].unique():
    for gender in data['sex'].unique():
        subset = data[(data['species'] == species) & (data['sex'] == gender)]
        size = subset['body_mass_g']/100
        plt.scatter(subset['bill_length_mm'], subset['bill_depth_mm'], s=size, color=colors[gender], marker=markers[species], label=f'{gender}, {species}')

plt.xlabel('Długość dzioba (mm)')
plt.ylabel('Głębokość dzioba (mm)')
plt.title('Wykres scatter z uwzględnieniem płci i gatunków pingwinów')
plt.legend()
plt.grid(True)
plt.show()

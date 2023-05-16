import pandas as pd
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
markers = {'Adelie': "<", 'Chinstrap': ",", 'Gentoo': "o"}
plt.scatter(x, y, c=data['sex'].map(colors))
plt.show()

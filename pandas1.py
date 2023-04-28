import numpy as np
import pandas as pd

# program91
tab1 = pd.Series([1, 2, 3, 4])
print(tab1)
print()
tab2 = pd.Series(['hej', 'siema', 'witam'])
print(tab2)
print()
list1 = [1, 2, 3, 4]
print(list1)
list1 = pd.Series(list1)
print(list1)
print()
list2 = pd.Series([1, 2, 3, 4, 5, 6])
print(list2)
list2 = list2.to_list()
print(list2)
print()
n1 = np.array([1, 2, 3])
n1 = pd.Series(n1)
print(n1)
print()
n2 = n1.to_numpy(n1)
print(n2)
print()
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
print(s1)
print(s2)
print(s1+s2)
print(s1-s2)
print(s1*s2)
print(s1/s2)
print()
s3 = pd.Series(np.arange(-10, 10.1, 0.1))
print(s3)
s4 = s3[s3 < 0]
print(s4)
print()
print()
my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7],
           'c': [3, 4, 8], 'd': [4, 10, 12]}
my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
my_series = pd.Series([1, 32, -37, 91, 12, 11, -5],
                      index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
df1 = pd.DataFrame(my_list)
print(df1)
print()
df2 = pd.DataFrame(my_dict)
print(df2)
print()
df3 = pd.DataFrame(my_array)
print(df3)
print()
df4 = pd.DataFrame(my_series)
print(df4)
print()
df1 = df1.values.tolist()
print(df1)
df2 = df2.to_dict()
print(df2)
df3 = df3.to_numpy()
print(df3)
df4 = df4.squeeze()
print(df4)
print()
print()
df = pd.DataFrame({'a': [1, 2, 3], 'b': [1, -3, 2],
                   'c': [2, 8, -5], 'd': [4, 0.5, 7],
                   'e': [5, 10, 3]})
print(df)
print()
print(df.iloc[0])
print(df.iloc[1:])
print(df.loc[2, 'b'])
print(df.loc[1, 'e'])
print()
print(df.sort_values('d'))
print()
print()

# program92
df1 = pd.DataFrame([[2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
                    ['Sylwia', 'Katarzyna', 'Teresa', 'Tomasz',
                     'Cezary', 'Zenon', 'Filip', 'Adrian'],
                    [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name', 'Age']
print(df1)
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933],
                    ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa',
                     'Tomasz', 'Cezary', 'Zenon'],
                    weight, height, glasses]).T
df2.columns = ['ID', 'Name', 'W', 'H', 'Gl']
print()
print(df2)
df0 = pd.merge(df1, df2, how='inner')
print()
print(df0)
# df0 = pd.merge(df1, df2, how='outer')
# print()
# print(df0)
print()
print(df0.sort_values('Name'))
print()
df3 = df2[glasses]
print(df3)
print()
df4 = df1[(df1['Age'] >= 20) & (df1['Age'] <= 30)]
print(df4)
print()
bmi = df2['W']*10000/(df2['H']**2)
print(bmi)
df2['bmi'] = bmi
print(df2)
print()
print(df1['Age'].mean())
print()
df0 = pd.merge(df1, df2, how='inner')
print(df0)
print()
df4 = df0[df0['Gl']]
print(df4['bmi'].mean())
df5 = df0[df0['Gl'] == False]
print(df5['bmi'].mean())
print()
df4 = df0[df0['Gl']]
print(df4['Age'].mean())
df5 = df0[df0['Gl'] == False]
print(df5['Age'].mean())

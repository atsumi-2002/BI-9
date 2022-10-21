import pandas  as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_excel('BI_Clientes09.xlsx', sheet_name='Hoja1')
print(data.shape)
print(data.groupby('BikeBuyer').size())
sb.catplot('Gender', data=data, kind="count")
plt.show()
sb.catplot('SpanishOccupation', data=data, kind="count")
plt.show()
sb.catplot('Region', data=data, hue='BikeBuyer', kind="count")
plt.show()
sb.catplot('SpanishEducation', data=data, kind="count")
plt.show()
sb.catplot('YearOfFirstPurchase', data=data, kind="count", aspect=3)
plt.show()
v1 = data['CharDatePurchase'].values
v2 = data['Age'].values
colores = ['red','blue']
tamanos = [60,40]
arreglo1 = []
arreglo2 = []
for index, row in data.iterrows():
    arreglo1.append(colores[row['BikeBuyer']])
    arreglo2.append(tamanos[row['BikeBuyer']])
plt.scatter(v1, v2, c=arreglo1, s=arreglo2)
plt.axis([20080101, 20040101, 0, 300])
plt.show()

import pandas  as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_excel('BI_Postulantes09.xlsx', sheet_name='Hoja1')
print(data.groupby('Nom_Especialidad').size())
data.drop(['Cod_Especialidad','Nivel Organización','Grado Nerviosismo','Dependencia Internet'], 1).hist()
plt.show()
sb.pairplot(data.dropna(), hue='Nom_Especialidad',
            vars=['Apertura Nuevos Conoc.',
                  'Participación Grupo Social',
                  'Grado Empatía'], kind='scatter')
plt.show()


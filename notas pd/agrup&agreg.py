import pandas as pd

data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)

#agregar y agrupar:
grupo = df.groupby('Categoría').agg({'Valor': 'mean'})  #agrupar por una columna y calcular la media

        #otro ejemplo mas explicito:
#Crear un DataFrame de ejemplo
data = {
    'Categoría': ['A', 'B', 'A', 'B', 'A'],
    'Valor': [10, 20, 15, 25, 30]
}
df = pd.DataFrame(data)

grupo = df.groupby('Categoría')     #Agrupar por la columna 'Categoría'

resultado = grupo['Valor'].mean()   #Aplicar una función de agregación, como la media

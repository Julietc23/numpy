import pandas as pd

data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)

#para manipular los chicos:
df.drop('Edad', axis=1)                              #elimina filas o columnas
df.rename(columns={'Nombre': 'Nombre Completo'})     #renombra las columnas o los indices
df.fillna(value=0)                                   #llena los valores nulos con un valor especificado
df.dropna()                                          #elimina filas o columnas con valores nulos


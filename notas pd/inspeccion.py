import pandas as pd

data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)

df.head()   #Muestra las primeras filas del DataFrame.
df.tail()   #Muestra las últimas filas del DataFrame.
df.info()   #Proporciona un resumen del DataFrame, incluyendo el tipo de datos y los valores nulos.



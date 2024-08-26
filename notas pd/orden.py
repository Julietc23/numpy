import pandas as pd

data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)


df.sort_values(by='Edad', ascending=False)  # Ordenar por la columna 'Edad'

df.sort_index()    # Ordenar por índice


import pandas as pd

data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)

#selección y filtrado:

    #por columna:
edades = df['edad']

    #por etiqueta:
fila = df.loc[0]    #primera fila

    #por index:
sub_df = df.iloc[0:2,1:2]   #primera dos filas, segunda columna
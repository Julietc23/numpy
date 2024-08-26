import pandas as pd

#lectura desde csv:
df = pd.read_csv('arch¿hivo.csv')

#escritura a csv:
df.to_csv('salida.csv',index=False)
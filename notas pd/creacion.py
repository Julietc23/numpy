import pandas as pd

#dos objetos:

        #dataframes:
data = {
    'nombre':['Ana','Luis','Carlos'],
    'edad':[25,40,34]
}
df = pd.DataFrame(data)

        #series:
s = pd.Series([1,2,3],['A','B','C'])

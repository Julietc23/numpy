import pandas as pd

s = pd.Series([1,2,3],['A','B','C'])

# Aplicar una función a todas
s = s.apply(lambda x: x ** 2)

# Mapear valores
s = s.map({1: 'uno', 2: 'dos', 3: 'tres'})


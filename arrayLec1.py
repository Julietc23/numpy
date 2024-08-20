import numpy as np
"""
En Numpy:
    - dimension es axis
    - numero de dimensiones es rank
    - tupla de dimension y longitud es shape
    - numero total de elementos es size
"""
    #arrays generado con funciones:

a = np.zeros((2, 4))        #(filas,columnas)
b = np.ones((2, 4))

print(f"a es: {a}")
print(f"\nb es: {b}")   #size de 8 axis: 2 dimensiones una de 2 y otra de 4

    #otro tipo de generacion:
c = np.full((2,3,4),8)
d = np.empty((2,3))  #no es predecible, inicializa el array con lo que hay en la memoria

    #atajos de arrays:
a.shape()   #ver shape
a.ndim()    #ver numero de dimensiones
a.size()    #elementos

#notas:
"""
    -para entender el np.ones((2,3,4)) hace referencia a 2x3x4, el numero de dimensiones:

                Aquí está el desglose de 2x3x4:

            Primera dimensión (2): Esto significa que el array tiene 2 "bloques" o "capas" en la primera dimensión. En otras palabras, el array tiene 2 matrices 2D apiladas.

            Segunda dimensión (3): Dentro de cada uno de esos bloques, hay 3 filas. Cada "capa" o "bloque" de 2D tiene 3 filas.

            Tercera dimensión (4): Dentro de cada fila, hay 4 elementos. Cada fila tiene 4 columnas.
    [
  [  # Primera "capa"
    [1, 2, 3, 4],  # Primera fila de la primera capa
    [5, 6, 7, 8],  # Segunda fila de la primera capa
    [9, 10, 11, 12] # Tercera fila de la primera capa
  ],
  [  # Segunda "capa"
    [13, 14, 15, 16],  # Primera fila de la segunda capa
    [17, 18, 19, 20],  # Segunda fila de la segunda capa
    [21, 22, 23, 24]   # Tercera fila de la segunda capa
  ]
]
"""
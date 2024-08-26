import numpy as np    
    #arrays generado con funciones:
a = np.zeros((2, 4))                      #(filas,columnas) de ceros
b = np.ones((2, 4))                       #de unos
c = np.full((2,3,4),8)                    #shape y con que elementos
d = np.empty((2,3))                       #no es predecible, inicializa el array con lo que hay en la memoria
e = np.array([[1,2,3,4],[5,6,7,8]])       #inicialización con listas
f = np.linspace(0,6,10)                   #basada en rangos:(minimo,maximo,numero de elementos)
g = np.random.rand(2,3,4)                 #inicializa con valores aleatorios
h = np.random.randn(2,4)                  # datos se distribuyen de forma normal(gaussiana)
i = np.arange(4)                          #crea un array de una dimension con valores consecutivos al pasado
j = np.eye()                              #crea un array identidad
import numpy as np

array = np.arange(20)
array1 = np.arange(10)

    #modificar estructura de arrays:
array.reshape((4,5))            #cambiar la dimension y cantidad de elementos en c/u
array.transpose()               #transpone la matriz
array.flatten()                 #aplana un array en una dimension
np.concatenate((array, array1)) #concatena a lo largo dos arrays
np.split(array,3)               #divide el array en 3 subarrays
np.hstack((array, array1))      #apila los arrays horizontalmente
np.vstack((array, array1))      #apila los arrays verticalmente


"""
VER LOS SIGUIENTES:
    numpy.concatenate(): Une arrays a lo largo de un eje.
    numpy.split(): Divide un array en subarrays.
    numpy.hstack(): Apila arrays horizontalmente.
    numpy.vstack(): Apila arrays verticalmente.
"""
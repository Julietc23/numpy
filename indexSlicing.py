import numpy as np

arrayMulti = np.array([[1,2,3,4],[5,6,7,8]])
arrayUni = np.array([1,2,3,4,5])

    #como indexar o hacer slicing:
            #UNIDIMENSIONAL
arrayUni[4]      #indexacion
arrayUni[4:]     #slicing
arrayUni[0::3]   #strip

            #MULTIDIMENSIONAL:

arrayMulti[0, 3]  #[fila,elemento]
arrayMulti[1, :]  #slicing en toda la fila dos
arrayMulti[:, 2]  #mismo que el anterior

            #de forma booleana:
condition = (arrayUni > 2) & (arrayUni < 5)
arrayUni[condition]
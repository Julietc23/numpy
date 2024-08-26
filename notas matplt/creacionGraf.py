import matplotlib
import matplotlib.pyplot as plt

# Muestrar los gráficos integrados dentro de jupyter notebook
#           %matplotlib inline

            #   GRAFICO DE LINEA:

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de línea
plt.plot(x, y, 'o')

#mostrar:
plt.show()

                #GRAFICO DE BARRAS:

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [4, 7, 1, 8]

# Crear gráfico de barras
plt.bar(categorias, valores)

                #GRAFICO DE PASTEL:

# Datos de ejemplo
etiquetas = ['A', 'B', 'C', 'D']
tamaños = [20, 35, 25, 20]

# Crear gráfico de pastel
plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%')

"""
labels: Etiquetas para cada segmento.
autopct: Formato para mostrar porcentajes.
"""

                #HISTOGRAMA:

# Datos de ejemplo
datos = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]

# Crear histograma
plt.hist(datos, bins=5, edgecolor='black')

                #GRAFICO DE DISPERSION:

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear gráfico de dispersión
plt.scatter(x, y)
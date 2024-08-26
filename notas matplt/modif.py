import matplotlib.pyplot as plt

plt.title('Gráfico de Barras')  #añadir título

plt.xlabel('Categorías',fontsize=14)        #añadir etiquetas a cada eje
plt.ylabel('Valores',fontsize=14)       

plt.grid(True)                  #agregar una grilla al fondo

plt.legend(loc="best")          #situa a la leyenda en la mejor localización

    #si tengo que poner dos graficos en una sola linea:
plt.subplot(1, 2, 1) # 1 rows, 1 columns, 1st subplot
plt.subplot(1, 2, 2) # 1 rows, 2 columns, 2nd subplot

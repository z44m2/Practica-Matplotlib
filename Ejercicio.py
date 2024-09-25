import numpy as np
import matplotlib.pyplot as plt

# Crear un vector de tamaño 720 con valores aleatorios
vector = np.random.rand(720)

# Reshape a (120, 6)
matriz = vector.reshape(120, 6)

# Crear un subplot con 6 paneles (2 filas, 3 columnas)
fig, axs = plt.subplots(2, 3, figsize=(14, 8))

# Panel 1 - Gráfico de línea (plot)
axs[0, 0].plot(matriz[:, 0], label='Plot')
axs[0, 0].set_title('Gráfico de Línea')
axs[0, 0].set_xlabel('Índice')
axs[0, 0].set_ylabel('Valor')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Panel 2 - Gráfico de dispersión (scatter)
axs[0, 1].scatter(np.arange(len(matriz[:, 1])), matriz[:, 1], label='Scatter', color='orange')
axs[0, 1].set_title('Gráfico de Dispersión')
axs[0, 1].set_xlabel('Índice')
axs[0, 1].set_ylabel('Valor')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Panel 3 - Gráfico de barras (bar)
axs[0, 2].bar(np.arange(len(matriz[:, 2])), matriz[:, 2], label='Bar', color='green')
axs[0, 2].set_title('Gráfico de Barras')
axs[0, 2].set_xlabel('Índice')
axs[0, 2].set_ylabel('Valor')
axs[0, 2].legend()
axs[0, 2].grid(True)

# Panel 4 - Histograma
axs[1, 0].hist(matriz[:, 3], bins=10, label='Histograma', color='red')
axs[1, 0].set_title('Histograma')
axs[1, 0].set_xlabel('Valor')
axs[1, 0].set_ylabel('Frecuencia')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Panel 5 - Gráfico de torta (pie)
axs[1, 1].pie([np.sum(matriz[:, 4]), np.sum(matriz[:, 5])], labels=['Suma Col 4', 'Suma Col 5'], autopct='%1.1f%%')
axs[1, 1].set_title('Gráfico de Torta')

# Panel 6 - Gráfico de área
axs[1, 2].fill_between(np.arange(len(matriz[:, 5])), matriz[:, 5], color='purple', alpha=0.7, label='Área')
axs[1, 2].set_title('Gráfico de Área')
axs[1, 2].set_xlabel('Índice')
axs[1, 2].set_ylabel('Valor')
axs[1, 2].legend()
axs[1, 2].grid(True)

# Ajustar el espacio entre subplots
plt.show()

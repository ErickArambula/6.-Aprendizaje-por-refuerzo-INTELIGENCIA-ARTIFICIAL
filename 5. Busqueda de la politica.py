import numpy as np

# Definición del entorno de ejemplo
num_estados = 4
num_acciones = 2
recompensas = np.array([[0, 1], [0, 0], [0, 0], [1, 0]])  # Matriz de recompensas
probabilidad_transicion = np.array([
    [[0.9, 0.1], [0.2, 0.8]],
    [[0.7, 0.3], [0.4, 0.6]],
    [[0.8, 0.2], [0.3, 0.7]],
    [[0.0, 1.0], [0.0, 1.0]]
])

# Inicialización de una política arbitraria (por ejemplo, todas las acciones son 0)
politica = np.zeros((num_estados, num_acciones), dtype=int)

# Parámetro de descuento para recompensas futuras
factor_descuento = 0.9

# Iteración de políticas
num_iteraciones = 1000

for _ in range(num_iteraciones):
    valor_estados = np.zeros(num_estados)
    for estado in range(num_estados):
        for accion in range(num_acciones):
            valor_estados[estado] += politica[estado][accion] * np.sum(probabilidad_transicion[estado][accion] * (recompensas[estado][accion] + factor_descuento * valor_estados))
    
    for estado in range(num_estados):
        mejor_accion = np.argmax([np.sum(probabilidad_transicion[estado][accion] * (recompensas[estado][accion] + factor_descuento * valor_estados)) for accion in range(num_acciones)])
        politica[estado] = 0
        politica[estado][mejor_accion] = 1

print("Política óptima encontrada:")
print(politica)

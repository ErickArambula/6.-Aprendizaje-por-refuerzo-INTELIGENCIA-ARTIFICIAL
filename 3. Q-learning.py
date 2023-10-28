import numpy as np

# Definición del laberinto
laberinto = np.array([
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0]
])

# Definición de estados, acciones y matriz Q
estados = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
acciones = [0, 1, 2, 3]  # 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha
Q = np.zeros(len(estados), len(acciones))

# Parámetros de Q-Learning
tasa_aprendizaje = 0.8
factor_descuento = 0.95
num_episodios = 1000

# Función para seleccionar una acción basada en Q
def seleccionar_accion(estado):
    if np.random.uniform(0, 1) < 0.3:  # Exploración con probabilidad 0.3
        return np.random.choice(acciones)
    else:
        return np.argmax(Q[estado, :])

# Entrenamiento del agente con Q-Learning
for episodio in range(num_episodios):
    estado_actual = np.random.choice(estados)
    while estado_actual != 5:  # Objetivo en el estado 5
        accion = seleccionar_accion(estado_actual)
        proximo_estado = estado_actual
        if accion == 0:  # Arriba
            proximo_estado = estado_actual - 6
        elif accion == 1:  # Abajo
            proximo_estado = estado_actual + 6
        elif accion == 2:  # Izquierda
            proximo_estado = estado_actual - 1
        elif accion == 3:  # Derecha
            proximo_estado = estado_actual + 1

        recompensa = -1 if laberinto.flat[proximo_estado] == 0 else 100 if proximo_estado == 5 else -100
        Q[estado_actual, accion] = Q[estado_actual, accion] + tasa_aprendizaje * (recompensa + factor_descuento * np.max(Q[proximo_estado, :]) - Q[estado_actual, accion])
        estado_actual = proximo_estado

print("Matriz Q aprendida:")
print(Q)

import random

# Entorno de ejemplo: Recompensas por acción en un brazo de bandit
recompensas = [0.3, 0.5, 0.7, 0.2, 0.6]

# Número de brazos del bandit
num_brazos = len(recompensas)

# Probabilidades de elegir cada brazo (inicialmente, se exploran todos)
probabilidades_brazos = [1.0] * num_brazos

# Función para seleccionar una acción con el método ε-greedy
def seleccionar_accion(epsilon):
    if random.random() < epsilon:
        # Exploración: elegir un brazo al azar
        accion = random.choice(range(num_brazos))
    else:
        # Explotación: elegir el brazo con la mayor recompensa esperada
        accion = probabilidades_brazos.index(max(probabilidades_brazos))
    return accion

# Función para simular una iteración (selección de acción y obtención de recompensa)
def simular_iteracion(epsilon):
    accion = seleccionar_accion(epsilon)
    recompensa = random.gauss(recompensas[accion], 0.1)  # Simulación de recompensa con ruido
    return accion, recompensa

# Algoritmo de Aprendizaje por Refuerzo Activo
epsilon = 0.1  # Parámetro de exploración
num_iteraciones = 1000

for _ in range(num_iteraciones):
    accion, recompensa = simular_iteracion(epsilon)
    # Actualizar la probabilidad del brazo elegido en función de las recompensas observadas
    probabilidades_brazos[accion] = (probabilidades_brazos[accion] + recompensa) / 2

# Brazo con mayor probabilidad después del aprendizaje
brazo_optimo = probabilidades_brazos.index(max(probabilidades_brazos))

print("Probabilidades de brazos después del aprendizaje:", probabilidades_brazos)
print("Brazo óptimo:", brazo_optimo)

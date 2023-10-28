import random

# Definición del entorno de ejemplo (recompensas por acción)
recompensas = [0.1, 0.3, 0.2, 0.4]

# Parámetro de exploración ε
epsilon = 0.2

# Función para seleccionar una acción con el método ε-greedy
def seleccionar_accion():
    if random.random() < epsilon:
        # Exploración: elige una acción al azar
        accion = random.choice(range(len(recompensas)))
    else:
        # Explotación: elige la acción con la recompensa esperada más alta
        accion = recompensas.index(max(recompensas))
    return accion

# Simulación de episodios
num_episodios = 1000
acciones_seleccionadas = []

for _ in range(num_episodios):
    accion = seleccionar_accion()
    acciones_seleccionadas.append(accion)

# Cálculo de la frecuencia de selección de cada acción
frecuencia_acciones = [acciones_seleccionadas.count(i) / num_episodios for i in range(len(recompensas))]

print("Frecuencia de selección de acciones:", frecuencia_acciones)

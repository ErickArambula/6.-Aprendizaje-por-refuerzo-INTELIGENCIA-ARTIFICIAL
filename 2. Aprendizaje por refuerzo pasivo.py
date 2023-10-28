import random

# Entorno de ejemplo: Recompensas por estado
recompensas = {
    "A": 0,
    "B": 0,
    "Terminado": 1
}

# Política de ejemplo (para evaluar)
politica = {
    "A": 1,  # El agente siempre toma la acción 1 en el estado A
    "B": 0   # El agente siempre toma la acción 0 en el estado B
}

# Función para simular una secuencia de episodios
def simular_episodio():
    estado = "A"
    episodio = []
    while estado != "Terminado":
        accion = politica[estado]
        proximo_estado = "B" if estado == "A" else "Terminado"
        recompensa = recompensas[proximo_estado]
        episodio.append((estado, accion, recompensa))
        estado = proximo_estado
    return episodio

# Evaluación de la política usando el método de Monte Carlo
num_episodios = 10000
valor_estado_A = 0
valor_estado_B = 0

for _ in range(num_episodios):
    episodio = simular_episodio()
    for i, (estado, _, recompensa) in enumerate(episodio[::-1]):
        if estado == "A":
            valor_estado_A += recompensa
        elif estado == "B":
            valor_estado_B += recompensa

# Promedio de los valores de los estados
valor_estado_A /= num_episodios
valor_estado_B /= num_episodios

print("Valor del Estado A:", valor_estado_A)
print("Valor del Estado B:", valor_estado_B)

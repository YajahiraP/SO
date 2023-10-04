from collections import deque

class Proceso:
    def __init__(self, nombre, tiempo_cpu):
        self.nombre = nombre
        self.tiempo_cpu = tiempo_cpu

def round_robin(procesos, quantum):
    cola = deque(procesos)
    tiempo_total = 0

    print("Ejecución de Round Robin con quantum =", quantum)
    
    while cola:
        proceso_actual = cola.popleft()
        tiempo_ejecucion = min(quantum, proceso_actual.tiempo_cpu)
        proceso_actual.tiempo_cpu -= tiempo_ejecucion
        tiempo_total += tiempo_ejecucion

        print(f"Ejecutando {proceso_actual.nombre} durante {tiempo_ejecucion} unidades de tiempo")

        if proceso_actual.tiempo_cpu > 0:
            cola.append(proceso_actual)

    print(f"Tiempo total de ejecución: {tiempo_total} unidades de tiempo")

# Ejemplo de uso
if __name__ == "__main__":
    proceso1 = Proceso("P1", 10)
    proceso2 = Proceso("P2", 5)
    proceso3 = Proceso("P3", 8)
    proceso4 = Proceso("P4", 4)

    procesos = [proceso1, proceso2, proceso3, proceso4]
    quantum = 3

    round_robin(procesos, quantum)








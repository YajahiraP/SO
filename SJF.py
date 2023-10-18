def sjf(processes, burst_time):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = burst_time.copy()
    total_waiting_time = 0
    total_turnaround_time = 0

    for current_time in range(sum(burst_time)):
        min_burst = float('inf')
        shortest_process = None
        for i in range(n):
            if remaining_time[i] > 0 and burst_time[i] < min_burst and current_time >= completion_time[i]:
                min_burst = burst_time[i]
                shortest_process = i

        if shortest_process is None:
            continue

        remaining_time[shortest_process] -= 1
        completion_time[shortest_process] = current_time + 1

        if remaining_time[shortest_process] == 0:
            waiting_time[shortest_process] = current_time + 1 - burst_time[shortest_process]
            turnaround_time[shortest_process] = current_time + 1
            total_waiting_time += waiting_time[shortest_process]
            total_turnaround_time += turnaround_time[shortest_process]

    print("\nProceso\tTiempo de Espera\tTiempo de Retorno")
    for i in range(n):
        print(f"P{i}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print(f"\nTiempo de Espera Promedio = {average_waiting_time}")
    print(f"Tiempo de Retorno Promedio = {average_turnaround_time}")


if __name__ == "__main__":
    n = 5
    processes = []
    burst_time = []

    for i in range(n):
        process_name = input(f"Ingrese el nombre del proceso P{i}: ")
        burst = int(input(f"Ingrese el tiempo de ejecución para {process_name}: "))
        processes.append(process_name)
        burst_time.append(burst)

    sjf(processes, burst_time)
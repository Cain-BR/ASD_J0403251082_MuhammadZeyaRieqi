#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi 2: Algoritma Bellman Ford

def bellman_ford(graph, start):
    #Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    #Jarak node awal = 0
    distances[start] = 0

    #Relaksasi berulang
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances
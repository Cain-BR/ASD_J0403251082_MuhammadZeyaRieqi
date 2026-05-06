#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi 1: Algoritma Dijkstra

import heapq

graph = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 5},
    "C": {"D": 1},
    "D": {}
}

def dijkstra(graph, start):
    #Menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}

    #Jarak node awal = 0
    distances[start] = 0

    #Priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        #Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            #Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
hasil = dijkstra(graph, "A")
print(hasil)
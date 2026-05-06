#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
#Praktikum 12 - Graph II: Shortest Path

#Latihan 5: Studi Kasus dengan Program Shortest Path

import heapq

graph = {
    "Bogor": {"Jakarta": 5, "Depok": 2},
    "Jakarta": {"Bandung": 7},
    "Depok": {"Jakarta": 2, "Bandung": 6},
    "Bandung": {}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'Bogor')

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print("Bogor", "->", kota, "=", jarak)

# Jawaban Analisis:
# 1. Node awal yang digunakan apa? Bogor
# 2. Node mana yang memiliki jarak paling kecil dari node awal? Jakarta (5)
# 3. Node mana yang memiliki jarak paling besar dari node awal? Bandung (12)
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
# Algoritma Dijkstra bekerja dengan memilih node dengan jarak terpendek dari node awal, lalu memperbarui jarak ke node-node tetangga. Proses ini diulangi hingga semua node telah dikunjungi.
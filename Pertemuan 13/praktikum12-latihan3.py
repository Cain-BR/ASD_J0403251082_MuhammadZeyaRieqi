#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
# Praktikum 13 - Graph III: Spanning Tree

#Latihan 3: Implementasi Algoritma Prim

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])

    edges = []
    
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:

            visited.add(v)
            
            mst.append((u, v, weight))
            total_weight += weight

            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan? 'A'
# 2. Edge mana yang dipilih pertama kali? (2, 'A', 'C')
# 3. Bagaimana Prim menentukan edge berikutnya? 
# Dengan memilih edge dengan bobot terkecil yang menghubungkan node yang sudah dikunjungi dengan node yang belum dikunjungi
# 4. Berapa total bobot MST yang dihasilkan? 6
# 5. Apa perbedaan pendekatan Prim dan Kruskal?
# Prim membangun MST dengan menambahkan edge satu per satu berdasarkan node yang sudah dikunjungi, sedangkan Kruskal memilih edge berdasarkan bobot tanpa memperhatikan node yang sudah dikunjungi.
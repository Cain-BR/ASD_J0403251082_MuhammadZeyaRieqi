#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)

from collections import deque

graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS dari Rumah:")
bfs(graph, 'Rumah')

#Pertanyaan Analisis
#1. Node mana yang dikunjungi pertama? 
# Node 'Rumah'
#2. Mengapa BFS cocok untuk mencari jalur terdekat? 
# Karena BFS mengeksplorasi semua node pada level yang sama sebelum melanjutkan ke level berikutnya, sehingga memastikan bahwa jalur terdekat ditemukan terlebih dahulu.
#3. Apa perbedaan urutan BFS jika struktur graph diubah? 
# Visited node akan berubah karena BFS mengikuti urutan antar node dalam graph.
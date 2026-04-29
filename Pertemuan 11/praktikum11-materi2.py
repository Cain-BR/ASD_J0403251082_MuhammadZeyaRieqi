#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Materi 2: Implementasi BFS

#Struktur data untuk membuat antrian
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran graph dengan BFS
    #graph: dictionary
    #start: node awal penelusuran

    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    print("Urutan BFS:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#Menjalankan BFS mulai dari node 'A'
bfs(graph, 'A')

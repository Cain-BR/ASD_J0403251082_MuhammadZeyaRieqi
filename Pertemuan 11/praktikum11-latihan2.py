#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited = set()
print("DFS dari A:")
dfs(graph, 'A', visited)

#Pertanyaan Analisis
#1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# Karena DFS mengikuti satu jalur sejauh mungkin sebelum kembali dan mencoba jalur lain.
#2. Apa yang terjadi jika urutan neighbor diubah?
# DFS akan berubah.
#3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
# DFS: A B D E C F
# BFS: A B C D E F

from collections import deque

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

print("\nBFS dari A:")
bfs(graph, 'A')
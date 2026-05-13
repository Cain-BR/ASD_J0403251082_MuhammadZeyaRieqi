#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
# Praktikum 13 - Graph III: Spanning Tree

#Latihan 5: Tugas Mandiri: Buat Program MST dengan Kasus Baru

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Edge pada graph:\n")
for edge in edges:
    print(edge)

print("\nMinimum Spanning Tree:\n")

for edge in mst:
    print(edge)

print("\nTotal bobot =", total_weight)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih? Jaringan Jalan Antar Kota
# 2. Algoritma apa yang digunakan? Kruskal
# 3. Edge mana saja yang dipilih dalam MST? 
# (2, 'Bogor', 'Depok'), (3, 'Depok', 'Jakarta'), (5, 'Bogor', 'Jakarta'), (6, 'Jakarta', 'Bandung')
# 4. Berapa total bobot MST? 9
# 5. Mengapa edge tertentu tidak dipilih? 
# Karena edge tersebut akan membentuk siklus dalam MST.
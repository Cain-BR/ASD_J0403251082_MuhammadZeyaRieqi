#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
# Praktikum 13 - Graph III: Spanning Tree

#Latihan 4: Studi Kasus: Jaringan Kabel Antar Gedung

edges = [
    (1, 'GedungC', 'GedungD'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (4, 'GedungA', 'GedungB'),
    (5, 'GedungA', 'GedungD')
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
# 1. Algoritma apa yang digunakan? Kruskal
# 2. Edge mana saja yang dipilih? 
# (1, 'GedungC', 'GedungD'), (2, 'GedungA', 'GedungC'), (3, 'GedungB', 'GedungD')
# 3. Berapa total biaya minimum? 6
# 4. Mengapa MST cocok digunakan pada kasus ini? 
# Karena MST meminimalkan total biaya penghubung antar gedung sambil memastikan semua gedung terhubung.
#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
# Praktikum 13 - Graph III: Spanning Tree

#Latihan 2: Implementasi Sederhana Algoritma Kruskal

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali? Edge (1, 'C', 'D')
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
# Agar total bobot MST menjadi minimal
# 3. Berapa total bobot MST yang dihasilkan? 6
# 4. Mengapa edge tertentu tidak dipilih? 
# Karena edge tersebut akan membentuk cycle dengan edge yang sudah dipilih
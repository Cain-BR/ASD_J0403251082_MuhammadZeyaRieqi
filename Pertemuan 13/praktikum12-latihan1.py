#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1
# Praktikum 13 - Graph III: Spanning Tree

#Latihan 1: Memahami Konsep Spanning Tree

# Daftar edge graph
edges = [
 ('A', 'B'),
 ('A', 'C'),
 ('A', 'D'),
 ('C', 'D'),
 ('B', 'D')
]
# Contoh spanning tree
spanning_tree = [
 ('A', 'C'),
 ('C', 'D'),
 ('D', 'B')
]
print("Edge pada graph:")
for edge in edges:
    print(edge)
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
#    Graph awal menggambarkan hubungan antar simpul, sedangkan spanning tree menghubungkan semua simpul dengan jumlah edge yang minimal dan tidak memiliki siklus.
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    Karena jika ada siklus, maka ada lebih dari satu jalur antara dua simpul.
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    Siklus terjadi apabila jumlah edge lebih banyak atau sama dengan jumlah simpul
#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 4: Rotasi Kanan pada BST yang tidak seimbang

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

def rotate_right(x):
    # x adalah root lama
        y = x.left # y adalah child kiri x
        T2 = y.right # subtree kanan milik y disimpan sementara
    # Proses rotasi
        y.right = x # x menjadi child kanan dari y
        x.left = T2 # child kiri x diganti dengan T2
    # y menjadi root baru
        return y

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)
print("Preorder sebelum rotasi kanan:")
preorder(root)
print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)
# Melakukan rotasi kanan pada root
root = rotate_right(root)
print("\nPreorder sesudah rotasi kanan:")
preorder(root)
print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)
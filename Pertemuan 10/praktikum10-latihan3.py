#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 3: Rotasi Kiri pada BST yang tidak seimbang

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

def rotate_left(x):
 # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree kiri milik y disimpan sementara
 # Proses rotasi
    y.left = x # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2
 # y menjadi root baru
    return y

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)
print("Preorder sebelum rotasi kiri:")
preorder(root)
print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)
# Melakukan rotasi kiri pada root
root = rotate_left(root)
print("\nPreorder sesudah rotasi kiri:")
preorder(root)
print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)
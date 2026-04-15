#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 1: Membuat Node Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("A")
print("Data pada root", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

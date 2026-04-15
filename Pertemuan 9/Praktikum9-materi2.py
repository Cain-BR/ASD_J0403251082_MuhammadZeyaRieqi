#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 2: Membuat Binary Search Tree Sederhana

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Data pada root", root.data)
print("Data child kiri root", root.left.data)
print("Data child kanan root", root.right.data)
print("Data child kiri dari B", root.left.left.data)
print("Data child kanan dari B", root.left.right.data)
print("Data child kiri dari C", root.right.left.data)
print("Data child kanan dari C", root.right.right.data)

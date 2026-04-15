#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 3: Membuat Traversal Preorder

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Hasil Traversal Preorder:")
preorder(root)
#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan 6: Membuat Traversal Postorder

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
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
root = Node("Direktur")
root.left = Node("Manajer A")
root.right = Node("Manajer B")
root.left.left = Node("Staf 1")
root.left.right = Node("Staf 2")
root.right.left = Node("Staf 3")
root.right.right = Node("Staf 4")

print("Hasil Traversal Preorder:")
preorder(root)
print("\nHasil Traversal Inorder:")
inorder(root)
print("\nHasil Traversal Postorder:")
postorder(root)
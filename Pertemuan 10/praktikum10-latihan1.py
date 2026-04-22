#Nama: Muhammad Zeya Rieqi
#NIM: J0403251082
#Kelas: TPL B1

#Latihan: BST

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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

root = None
data_list = [50, 30, 70, 20, 40, 50, 80]
for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

print("Hasil Inorder Traversal:")
inorder(root)

key = 40
if search(root, key):
    print("data ditemukan")
else:
    print("data tidak ditemukan")

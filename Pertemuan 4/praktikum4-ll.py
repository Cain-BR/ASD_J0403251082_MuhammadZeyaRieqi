#Nama: Muhammad Zeya Rieqi
#NIM J0403251082

#Implementasi Dasar: Node pada Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

nodeA.next = nodeB
nodeB.next = nodeC

head = nodeA

current = head
while current is not None:
    print(current.data)
    current = current.next

#Implementasi Dasar: Linked List + Insert Awal

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_awal(self, data):
        nodebaru = Node(data)
        nodebaru.next = self.head
        self.head = nodebaru

    def hapus_awal(self):
        data_terhapus = self.head.data
        self.head = self.head.next
        print(f"Data yang dihapus: {data_terhapus}")

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

ll = LinkedList()
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
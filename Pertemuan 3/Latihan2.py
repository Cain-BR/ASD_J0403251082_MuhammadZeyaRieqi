class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    def display(self):
        if not self.head:
            print("List is empty")
            return
        
        print("\nTraversing the circular singly linked list:")
        temp = self.head
        print(temp.data, end=' -> ')
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("back to head")

    def find_node(self, key):
        temp = self.head
        if not temp:
            return f"Circular Linked List kosong. Tidak ada elemen yang dapat dicari."
        while True:
            if temp.data == key:
                return f"Elemen {key} ditemukan dalam Circular Linked List"
            temp = temp.next
            if temp == self.head:
                break
        return f"Elemen {key} tidak ditemukan dalam Circular Linked List"

# Contoh Tampilan 1
csll = CircularSinglyLinkedList()
csll.insert_at_end(3)
csll.insert_at_end(7)
csll.insert_at_end(12)
csll.insert_at_end(19)
csll.insert_at_end(25)
csll.display()

print(csll.find_node(int(input("\nMasukkan elemen yang ingin dicari: "))))

# Contoh Tampilan 2
cll = CircularSinglyLinkedList()
cll.insert_at_end(5)
cll.insert_at_end(10)
cll.insert_at_end(15)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()

print(cll.find_node(int(input("\nMasukkan elemen yang ingin dicari: "))))

# Contoh Tampilan 3
sll = CircularSinglyLinkedList()
sll.display()

print(sll.find_node(int(input("\nMasukkan elemen yang ingin dicari: "))))
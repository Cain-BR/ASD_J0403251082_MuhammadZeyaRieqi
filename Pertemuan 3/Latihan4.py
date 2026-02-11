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
            print("Kosong")
            return
        
        temp = self.head
        print(temp.data, end=' -> ')
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("back to head")

# Menggabungkan dua Circular Singly Linked List
    def concatenate(self, other_list = 0):
        if not self.head:
            self.head = other_list.head
            self.tail = other_list.tail
        elif not other_list.head:
            return "Kosong"
        else:
            self.tail.next = other_list.head
            other_list.tail.next = self.head
            self.tail = other_list.tail

csll = CircularSinglyLinkedList()
sll = CircularSinglyLinkedList()

def insert_elements_to_list1(cll, elements):
    for element in elements:
        cll.insert_at_end(element)
    cll.display()

def insert_elements_to_list2(cll, elements):
    for element in elements:
        cll.insert_at_end(element)
    cll.display()

insert_elements_to_list1(csll, [int(x) for x in input("Masukkan elemen untuk Circular Singly Linked List 1 (pisahkan dengan koma): ").split(",") if x.strip() != ""])
insert_elements_to_list2(sll, [int(x) for x in input("Masukkan elemen untuk Circular Singly Linked List 2 (pisahkan dengan koma): ").split(",") if x.strip() != ""])
csll.concatenate(sll)
print("\nSetelah penggabungan dua Circular Singly Linked List:")
csll.display()
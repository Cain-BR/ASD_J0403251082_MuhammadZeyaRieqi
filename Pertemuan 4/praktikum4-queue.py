#Nama: Muhammad Zeya Rieqi
#NIM J0403251082

#Implementasi Dasar: Queue Berbasis Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, data):
        nodebaru = Node(data)
        if self.rear is None:
            self.front = nodebaru
            self.rear = nodebaru
        else:
            self.rear.next = nodebaru
            self.rear = nodebaru

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        data_terdepan = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Data yang didequeue: {data_terdepan}")
        return data_terdepan

    def tampilkan(self):
        current = self.front
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print("None")

q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            print("List is empty")
            return
        
        print("\nTraversing forward:")
        temp = self.head
        print(temp.data, end=' -> ')
        temp = temp.next
        while temp != self.head:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("back to head")

    def display_backward(self):
        if not self.head:
            print("List is empty")
            return
        
        print("\nTraversing backward:")
        tail = self.head.prev
        temp = tail
        print(temp.data, end=' -> ')
        temp = temp.prev
        while temp != tail:
            print(temp.data, end=' -> ')
            temp = temp.prev
        print("back to tail")
    
    def delete_node(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

# Example usage
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(3)
cdll.insert_at_end(5)
cdll.insert_at_end(13)
cdll.insert_at_end(2)
cdll.display_forward()
cdll.display_backward()
cdll.delete_node(13)
cdll.display_forward()
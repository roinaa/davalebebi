class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:

            current = current.next
        current.next = new_node

    def remove(self, index):
        if self.head is None:
            print("სიაში ელემენტები არ არის.")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        prev = None
        while current and count < index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("მოცემული ინდექსი არ არსებობს.")
            return
        prev.next = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            current = self.head
            while current:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node
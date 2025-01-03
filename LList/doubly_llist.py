class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
    

class DLL:
    def __init__(self, data):
        if data:
            self.head = Node(data)

    def push(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        current = self.head
        while current:
            current = current.next
        
        current.next = new_node
        new_node.prev = current
        


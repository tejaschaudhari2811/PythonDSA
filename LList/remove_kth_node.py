class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next
        current.next = node
    
    def traverse_llist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def remove_kth_node(self, k):
        current = self.head
        i = 0
        while current:
            if i % k == 1:
                current.next = current.next.next
            else:
                current = current.next
        self.head = current
        
linked_list = LList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert(6)
linked_list.remove_kth_node(2)
linked_list.traverse_llist()
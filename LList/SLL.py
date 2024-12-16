# Create a singly linkedlist 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_llist(head):
    current = head
    while current:
        print(current.data)
        current = current.next

def search_llist(head, key):
    current = head
    while current:
        if current.data == key:
            print(current.data)
            return
        else:
            current = current.next
    return -1

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

traverse_llist(head)
search_llist(head, 3)
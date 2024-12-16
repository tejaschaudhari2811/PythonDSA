class node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None

def check_circular(head):
    current = head
    while True:
        print(current.data)
        current = current.next
        if current == head:
            break

head = node(1)
head.next = node(2)
head.next.next = node(3)
head.next.next.next = node(4)
head.next.next.next.next = node(5)
head.next.next.next.next.next = head

check_circular(head)


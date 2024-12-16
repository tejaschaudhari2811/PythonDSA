class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("STack underflow ")
        temp = self.head
        self.head = self.head.next
        del temp

    def is_empty(self):
        return self.head is None

    def peek(self):
        print(self.head.data)

st = Stack()
st.push(11)
st.push(22)
st.push(33)
st.push(44)

st.peek()
st.pop()
st.pop()
st.peek()

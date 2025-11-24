class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(11)
n2 = Node(12)
n3 = Node(13)
n4 = Node(14)
n5 = Node(15)
n6 = Node(16)

n1.next = n2
n2.next = n3
n3.next = n4 
n4.next = n5
n5.next = n6

head = n1

current = head
while current:
    print(current.data, end="->")
    current= current.next
print("None")


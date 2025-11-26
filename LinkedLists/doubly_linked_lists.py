class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class doublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current

    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode

    def deleteValue(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
        
        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is None:
            return
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
                current.prev.next = current.next

    def displayList(self):
        if self.head is None:
            print("The list is empty")
            return
        current = self.head
        print("The linked list is: ")
        while current:
            print(current.data, end="<->")
            current = current.next
        print("NULL")
    
    def displayreverse(self):
        if self.head is None:
            print("The list is empty")
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        print("The linked list in reverse is: ")
        while current:
            print(current.data, end="<->")
            current = current.prev
        print("NULL")
        
    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current= current.next
        return False
    
if __name__ == "__main__":
    double1 = doublyLinkedList()

    double1.append(1)
    double1.append(2)
    double1.append(3)
    double1.append(4)
    double1.append(5)
    double1.append(6)
    double1.append(7)
    double1.append(8)
    double1.append(9)
    double1.append(10)
    double1.append(11)

    double1.displayList()
    double1.displayreverse()
    print(double1.search(2))
    print(double1.search(15))
    double1.prepend(0)
    double1.displayList()
    double1.deleteValue(5)
    double1.displayList()
        

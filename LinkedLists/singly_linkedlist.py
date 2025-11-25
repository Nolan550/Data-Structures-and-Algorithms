class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class singlyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
    
    def prepend(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def deleteValue(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is not None:

            current.next = current.next.next

    def displayList(self):
        if self.head is None:
            print("The list is empty")
            return
        current = self.head
        print("The linked list is: ")
        while current:
            print(current.data, end="_>")
            current = current.next
        print("NULL")

    def search(self,data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


if __name__ == "__main__":
    list = singlyLinkedList()
    list.append(11)
    list.append(12)
    list.append(13)
    list.append(14)
    list.append(15)
    list.append(16)

    list.displayList()

    print(list.search(13))
    print(list.search(25))

    list.prepend(10)
    list.displayList()
    list.deleteValue(14)
    print("After deleting 14:")
    list.displayList()

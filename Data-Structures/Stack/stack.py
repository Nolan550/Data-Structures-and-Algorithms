class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.size += 1

    def pop(self):
        if self.top is  None:
            raise IndexError("Stack is empty")
        poppedNode = self.top
        self.top = self.top.next
        self.size -= 1
        return poppedNode.data
    
    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.data
    
    def is_empty(self):
        return self.size == 0
    
    def getSize(self):
        return self.size

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top
        print("\nSTACK (top → bottom):")
        print("----------------------")

        while current:
            print(f"|  {current.data}  |")
            print("   ↓")
            current = current.next

        print(" None")

if __name__ == "__main__":
        s1 = Stack()

        print(s1.is_empty())
        print("The size of the stack is:", s1.getSize() , " elements")
        s1.push(12)
        s1.push(13)
        s1.push(14)
        s1.push(15)
        s1.push(16)
        s1.push(17)
        s1.display()
        print("The top element is:", s1.peek())
        print("Popped element:", s1.pop())
        s1.display()
        print("The size of the stack is:", s1.getSize() , " elements")

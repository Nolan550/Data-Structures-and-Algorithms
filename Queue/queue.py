class Node:

    def __init__(self, data):
        self.data  = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, data):
        newNode = Node(data)

        if self.front is None:
            self.front = newNode
            self.rear = newNode
            self.size +=1
        else:
            self.rear.next = newNode
            self.rear = newNode
            self.size +=1

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            

            if self.front is None:
                self.rear = None

            return data
        size -=1
        
    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data
    
    def isEmpty(self):
        return self.size == 0

        
if __name__ == "__main__":
    q1 = Queue()

    q1.peek()
    print(q1.size)
    q1.push("A")
    q1.push("B")
    q1.push("C")
    q1.push("D")
    q1.push("E")
    q1.push("F")
    q1.push("G")
    q1.push("H")
    q1.push("I")
    print(q1.size)
    print(q1.isEmpty())
    print(q1.dequeue())
    print(q1.size)
    print(q1.peek())

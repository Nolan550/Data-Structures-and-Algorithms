class customArray:
    def __init__(self, capacity):
        self.data = [0] * capacity
        self.size = 0
    
    def add(self, value):
        if self.size == len(self.data):
            self.resize()
        self.data[self.size] = value
        self.size += 1
    
    def resize(self):

        newData = len(self.data) * 2
        newdata = [0] * newData
        for i in range(self.size):
            newdata[i] = self.data[i]
        self.data = newdata

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of bounds")
        return self.data[index]
    
    def removeAt(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of Bounds")
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
            self.size -= 1

    def display(self):
        for i in range(self.size):
            print(self.data[i])

    def get_size(self):
        return self.size
    
if __name__ == "__main__":
    array = customArray(12)
    array.add(23)
    array.add(34)
    array.add(56)
    array.add(21)
    array.add(29)
    array.add(87)
    array.add(65)
    array.add(54)
    array.add(26)
    array.add(66)
    array.add(58)

    #array.display()
    print(array.get_size())
    array.removeAt(10)
    array.display()
    print(array.get_size())
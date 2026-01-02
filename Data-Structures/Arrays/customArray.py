class CustomArray:
    def __init__(self, capacity):
        self.data = [0] * capacity
        self.size = 0
    
    def add(self, value):
        if self.size == len(self.data):
            self.resize()
        self.data[self.size] = value
        self.size += 1
    
    def resize(self):
        new_capacity = len(self.data) * 2
        new_data = [0] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of bounds")
        return self.data[index]
    
    def removeAt(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of bounds")

        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1   

    def display(self):
        for i in range(self.size):
            print(self.data[i])

    def get_size(self):
        return self.size
    

if __name__ == "__main__":
    array = CustomArray(12)
    array.add(23)
    array.add(34)
    array.add(56)
    array.add(21)
    array.add(29)
    array.add(87)
    array.add(43)


    print("Initial size:", array.get_size())
    array.removeAt(6)
    print("\nArray after removing index 6:")
    array.display()
    print("\nFinal size:", array.get_size())

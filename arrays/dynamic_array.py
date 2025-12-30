# Implement a Dynamic Array from scratch:
# 	•	append(value)
# 	•	insert(index, value)
# 	•	delete(index)
# 	•	get(index), set(index, value)
# 	•	length()

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    # --- Helper ---
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    # --- Operations ---
    def append(self, value):
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        
        i = self.size
        while i > index:
            self.data[i] = self.data[i-1]
            i -= 1
        
        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]

        self.data[self.size - 1] = None
        self.size -= 1

        if self.capacity > 1 and self.size <= self.capacity // 4:
            self._resize(max(1, self.capacity // 2))

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value

    def length(self):
        return self.size
    
    def __str__(self):
        return str(self.data[:self.size])


if __name__ == '__main__':
    arr = DynamicArray()

    arr.append(1)
    arr.insert(0, 100)
    print(arr)

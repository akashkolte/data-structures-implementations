class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  

    def __repr__(self):
        if self.head == None:
            return "[]"
        
        prev = self.head

        return_string = f"[{prev.val}"

        while prev.next:
            prev = prev.next
            return_string += f", {prev.val}"
        
        return_string += "]"

        return return_string

    # length of the list
    def __len__(self):
        length = 0

        prev = self.head
        while prev:
            length += 1
            prev = prev.next
        
        return length
    
    # Check if value exists in the list.
    def __contains__(self, value):
        prev = self.head

        while prev:
            if prev.val == value:
                return True
            prev = prev.next

        return False
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            prev = self.head

            while prev.next != None:
                prev = prev.next
            
            prev.next = Node(value)
    
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            prev = self.head

            for _ in range(index-1):
                if prev is None:
                    raise IndexError("Index out of bounds")
                prev = prev.next
            
            newNode = Node(value)
            newNode.next = prev.next
            prev.next = newNode

    def delete(self, value):
        prev = self.head
        if prev == None:
            raise ValueError("No such value exists")
        
        if prev.val == value:
            self.head = prev.next
            return

        while prev.next:
            if prev.next.val == value:
                prev.next = prev.next.next
                return
            prev = prev.next
        
        raise ValueError("No such value exists")
    
    def pop(self, index):
        if self.head == None:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            return

        prev = self.head
        for _ in range(index-1):
            if prev.next is None:
                raise IndexError("Index out of bounds")
            prev = prev.next
        
        if prev.next == None:
            raise IndexError("Index out of bounds")

        prev.next = prev.next.next
    
    def get(self, index):
        if self.head == None:
            raise IndexError("Index out of bounds")
        
        prev = self.head
        for i in range(index):
            if prev.next != None:
                prev = prev.next
            else:
                raise IndexError("Index out of bounds")
        
        return prev.val

if __name__ == '__main__':
    ll = LinkedList()

    ll.append(5)
    ll.append(10)
    ll.append(20)
    ll.append(-1)
    ll.append(7)

    print("1", ll)

    ll.prepend(100)

    print("2", ll)

    ll.insert(200, 1)

    print("3", ll)

    ll.delete(10)

    print("4", ll)

    ll.pop(1)

    print(ll)

    print(ll.get(1))
    print(20 in ll)
    print(800 in ll)
    print(len(ll))
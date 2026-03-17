# TODO: Doubly Linked List Implementation

# Core Operations:
# • insert_at_head(value)
# • insert_at_tail(value)
# • insert_at_index(value, index)
# • delete(value)                     → delete first occurrence
# • delete_all(value)                 → delete all occurrences
# • delete_at_index(index)

# Search & Access:
# • contains(value)
# • get(index)
# • size()
# • is_empty()

# Traversal:
# • print_forward()
# • print_backward()

# Transformations:
# • reverse()

# Utility:
# • clear()

# Advanced:
# • middle()                          → using fast/slow pointers

# Pythonic Representations:
# • __str__()                         → 1 <-> 2 <-> None
# • __repr__()                        → DoublyLinkedList([1, 2])

class DoublyListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # important for O(1) tail ops

    # Insert a new node at the beginning of the list.
    def insert_at_head(self, value):
        pass

    # Insert a new node at the end of the list.
    def insert_at_tail(self, value):
        pass

    # Insert a new node at a given index in the list.
    def insert_at_index(self, value, index):
        pass

    # Delete the first occurrence of a node with the given value.
    def delete(self, value):
        pass

    # Delete all nodes that match the given value.
    def delete_all(self, value):
        pass

    # Delete the node at a specific index.
    def delete_at_index(self, index):
        pass

    # Check if value exists in the list.
    def contains(self, value):
        pass

    # Return the value at a specific index.
    def get(self, index):
        pass

    # Return the number of nodes in the list.
    def size(self):
        pass

    # Check if the list is empty.
    def is_empty(self):
        pass

    # Print the list from head to tail.
    def print_forward(self):
        pass

    # Print the list from tail to head.
    def print_backward(self):
        pass

    # Reverse the doubly linked list in-place by swapping prev and next pointers of each node and updating head and tail.
    def reverse(self):
        pass

    # Find and return the middle node using fast and slow pointers.
    def middle(self):
        pass

    # Clear the list by removing all nodes.
    def clear(self):
        self.head = None
        self.tail = None

    # Return a human-readable string representation of the list (e.g., 1 <-> 2 <-> None).
    def __str__(self):
        pass

    # Return a developer-friendly representation of the list (e.g., DoublyLinkedList([1, 2])).
    def __repr__(self):
        pass

    # Remove and return the head node.    
    def pop_head(self):
        pass
    
    # Remove and return the tail node.
    def pop_tail(self):
        pass
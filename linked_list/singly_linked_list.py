# TODO: Singly Linked List Implementation
# Core Operations:
# • insert_at_head(value)
# • insert_at_tail(value)
# • insert_at_index(value, index)
# • delete(value)                     → delete first occurrence
# • delete_all(value)                 → delete all occurrences
# • delete_at_index(index)

# Search & Access:
# • search(value)
# • get(index)
# • size()
# • is_empty()

# Transformations:
# • reverse()

# Cycle Operations (Floyd’s Algorithm):
# • detect_cycle()
# • has_cycle_length()
# • find_cycle_start()

# Utility Functions:
# • print_list()
# • clear()

# Advanced:
# • middle()                          → using fast/slow pointers

# Pythonic Representations:
# • __str__()                         → human-readable (e.g., 1 -> 2 -> None)
# • __repr__()                        → developer-friendly (e.g., LinkedList([1, 2]))

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, value):
        if not value:
            return

        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, value):
        if not value:
            return
        
        new_node = ListNode(value)
        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
    
    def delete(self, value):
        if not value:
            return
        
        curr = self.head
        prev = ListNode(0)
        while curr:
            if curr.val == value:
                prev.next = curr.next
            prev = prev.next
            curr = curr.next

    def delete_at_index(self, index):
        if not index:
            return
        
        curr = self.head
        prev = ListNode(0)
        i = 0
        while i < index:
            i += 1
            curr = curr.next
            prev = prev.next
        
        prev = curr.next
    
    def search(self, value):
        if not value:
            return

        curr = self.head
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        
        return False
    
    def reverse(self):
        pass

    def detect_cycle(self):
        pass

    def print_list(self):
        pass

    def is_empty(self):
        pass

    # size of the list
    def size(self):
        pass

    # delete all occurence of a particular value
    def delete_all(self, value):
        pass

    def insert_at_index(self, value, index):
        pass

    # get value at index
    def get(self, index):
        pass

    # find middle of the list
    def middle(self):
        pass

    # check if cycle exists, if yes then find length
    def has_cycle_length(self):
        pass

    # if cycle exists then return starting node of cycle
    def find_cycle_start(self):
        pass
    
    # reset the list
    def clear(self):
        self.head = None

    # Returns a human-readable string representation of the linked list (used by print()).
    # Ex: 20 -> 10 -> 5 -> None    
    def __str__(self):
        pass

    # Returns an unambiguous, developer-friendly string representation of the object (used for debugging and in interpreter).
    # Ex: LinkedList([20, 10, 5])
    def __repr__(self):
        pass
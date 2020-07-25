from singly_linked_list import LinkedList, Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length()

    def __repr__(self):
        return str(self.storage)

    def push(self, value):
        self.storage.add_to_tail(Node(value))

    def pop(self):
        if self.__len__() is 0:
            return None
        else:
            return self.storage.remove_tail().value

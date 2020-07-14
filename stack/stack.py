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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?

#     def __len__(self):
#         pass

#     def push(self, value):
#         pass

#     def pop(self):
#         pass


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def isEmpty(self):
        return self.storage == []

    def __len__(self):
        return len(self.storage)

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return int(self.storage.pop())

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.storage[len(self.storage)-1]

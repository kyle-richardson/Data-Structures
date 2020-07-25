# from ..queue.queue import Queue
# from ..stack.stack import Stack

class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def isEmpty(self):
        return self.storage.length() is 0

    def __len__(self):
        return self.storage.length()

    def __repr__(self):
        return str(self.storage)

    def push(self, item):
        self.storage.add_to_tail(item)

    def pop(self):
        if self.storage.length() is 0:
            return None
        else:
            return self.storage.remove_tail()
    # def peek(self):
    #     if self.isEmpty():
    #         return None
    #     else:
    #         return self.storage[len(self.storage)-1]


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def isEmpty(self):
        return self.storage.length() == 0

    def __len__(self):
        return self.storage.length()

    def __repr__(self):
        return str(self.storage)

    def __str__(self):
        return str(self.storage)

    def enqueue(self, value):
        self.storage.add_to_head(value)

    def dequeue(self):
        if self.storage.length() is 0:
            return None
        else:
            return self.storage.remove_tail()


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def __repr__(self):
        lst = ""
        if self.head is None:
            return lst  # do nothing
        else:
            p = self.head
            while p is not None:
                lst += str(p.value) + ", "
                p = p.get_next()
        return lst

    def __str__(self):
        lst = ""
        if self.head is None:
            return lst  # do nothing
        else:
            p = self.head
            while p is not None:
                lst += str(p.value) + ", "
                p = p.get_next()
        return lst

    def add_to_tail(self, new_node):
        new_tail = new_node
        if self.tail is not None:
            self.tail.set_next(new_tail)
        else:
            self.head = new_tail
            self.head.set_next(None)
        new_tail.set_next(None)
        self.tail = new_tail

    def add_to_head(self, new_node):
        new_head = new_node
        if self.head is not None:
            new_head.set_next(self.head)
        else:
            new_head.set_next(None)
            self.tail = new_head
        self.head = new_head

    def remove_tail(self):
        if self.tail is None:
            return None
        if self.length() is 1:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail
        else:
            current = self.head
            prev = current
            while current.get_next() is not None:
                prev = current
                current = current.get_next()
            prev.set_next(None)
            self.tail = prev
            return current

    def remove_head(self):
        if self.head is None:
            return None
        toRemove = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return toRemove

    def isEmpty(self):
        return self.head == None and self.tail == None

    def contains(self, data):
        if self.head == None:
            return False
        else:
            p = self.head
            while p is not None:
                if p.value == data:
                    return True
                p = p.get_next()
            return False

    def get_max(self):
        max = float("-inf")
        if self.head == None:
            return None
        else:
            p = self.head
            while p is not None:
                if p.value > max:
                    max = p.value
                p = p.get_next()
            return max

    def length(self):
        count = 0
        if self.head == None:
            return 0
        else:
            p = self.head
            while p is not None:
                count += 1
                p = p.get_next()
            # print(f'count:{count}')
            return count

    def get_tail(self):
        if self.head is None:
            return None
        else:
            p = self.head
            while p is not None:
                last = p
                p = p.get_next()
            return last


"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_data(self):
        return self.value

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    # Insert the given value into the tree
    def insert(self, value):
        # if value == self.value:
        # print(f'{value} is equal to {self.value}')
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node is None:
            return
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    def bft_print(self, node):
        qu = Queue()
        qu.enqueue(node)
        while len(qu) > 0:
            lastNode = qu.storage.get_tail()
            if lastNode.right:
                qu.enqueue(lastNode.right)
            if lastNode.left:
                qu.enqueue(lastNode.left)
            qu.dequeue()
            print(lastNode)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        st = Stack()
        st.push(node)
        while len(st) > 0:
            lastNode = st.storage.get_tail()
            print(lastNode)
            st.pop()
            if lastNode.right:
                st.push(lastNode.right)
            if lastNode.left:
                st.push(lastNode.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

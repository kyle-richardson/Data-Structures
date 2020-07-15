"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def set_next(self, item):
        self.next = item

    def set_prev(self, item):
        self.prev = item

    def __str__(self):
        return str(self.value)

    def get_data(self):
        return self.value


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __repr__(self):
        s = ""
        p = self.head
        while p is not None:
            s += str(p)
            p = p.get_next()
        return s

    def isEmpty(self):
        return self.tail == None and self.head == None

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        newNext = None
        if self.head is None:
            self.tail = new_node
        else:
            newNext = self.head
        self.head = new_node
        self.head.set_prev(None)
        self.head.set_next(newNext)
        if self.head is not self.tail:
            self.head.next.set_prev(self.head)
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.head is None:
            return None
        data = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
            self.head.set_prev(None)
        self.length -= 1
        return data

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        newPrev = None
        if self.tail is None:
            self.head = new_node
        else:
            newPrev = self.tail
        self.tail = new_node
        self.tail.set_prev(newPrev)
        self.tail.set_next(None)
        if self.head is not self.tail:
            self.tail.prev.set_next(self.tail)
        self.length += 1

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_data()
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        self.length -= 1
        return data

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        if self.isEmpty():
            return
        elif node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.next.set_prev(node.prev)
            node.prev.set_next(node.prev)
            node.set_next(None)
            node.set_prev(None)
            self.length -= 1

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

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

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

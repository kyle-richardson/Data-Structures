class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self

    def set_next(self, item):
        self.next = item

    def get_next(self):
        return self.next

    def get_data(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.set_next(new_node)
            self.tail = new_node
        elif self.head is not None:
            self.tail = new_node
            self.tail.set_next(None)
        else:
            self.head = new_node
            self.head.set_next(None)
            self.tail = new_node
            self.tail.set_next(None)

    def add_to_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.set_next(new_node)
            self.head = new_node
        elif self.tail is not None:
            self.head = new_node
            self.head.set_next(None)
        else:
            self.head = new_node
            self.head.set_next(None)
            self.tail = new_node
            self.tail.set_next(None)

    def remove_tail(self):
        if self.tail is None:
            return None
        data = self.tail.get_data()
        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.get_next()

        return data

    def remove_head(self):
        if self.head is None:
            return None
        data = self.head.get_data()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()

        return data

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

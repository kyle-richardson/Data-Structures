class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def set_next(self, item):
        self.next = item

    def get_next(self):
        return self.next

    def get_data(self):
        return self.value


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

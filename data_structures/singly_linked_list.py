class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = None

    def insert(self, val):
        if self.head.val == None:
            self.head.next = Node(val)
            self.head = self.head.next
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def contains(self, val):
        curr_node = self.head
        while curr_node:
            if curr_node.val == val:
                return True
            curr_node = curr_node.next
        return False

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, node):
        self._head = node

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, node):
        self._tail = node

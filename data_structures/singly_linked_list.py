# Pros vs. Arrays:
# 1) Simple to add and delete nodes. You simply change the pointer.
# Alternatively in arrays, you need to shift all items over to fill the space of the deleted item.
# 2) Overflows can't occur unless memory is actually full

# Cons vs. Arrays:
# 1) Don't have fast random access. Arrays have indexes for this.
# 2) Must allocate more space for pointer fields.
# 3) Arrays have better memory locality since they are continguous which can improve
# cache performance.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def search(self, val):
        curr_node = self.head
        while curr_node:
            if curr_node.val == val:
                return curr_node
            curr_node = curr_node.next
        return False

    def remove_head(self):
        self.head = self.head.next or Node()

    def remove_node(self, val):
        curr_node, prev_node = self.head, Node()
        while curr_node:
            if curr_node.val == val:
                if self.is_head(prev_node):
                    self.head = self.head.next or Node()
                else:
                    prev_node.next = curr_node.next
                    return True
            curr_node, prev_node = curr_node.next, curr_node
        return False

    def is_head(self, node):
        return node.val is None

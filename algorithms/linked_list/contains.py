from .linked_list import SinglyLinkedList as Node


def contains(head, val):
    if head is None:
        return False
    elif head.val == val:
        return True
    else:
        return contains(head.next, val)

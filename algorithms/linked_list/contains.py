def contains(head, val):
    """Checks if a linked list contains a given value"""
    if head is None:
        return False
    return head.val == val or contains(head.next, val)

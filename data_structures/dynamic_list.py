INDEX_ERROR = "Can't pop an empty list!"


class DynamicList:
    def __init__(self):
        self.store = []
        self.count = 0

    def append(self, val):
        self.store.append(val)
        self.count += 1

    def appendleft(self, val):
        # O(n) - not time efficient.
        # Could use a heap, but you would also be mutating the list directly
        # instead of creating a new one in memory
        self.store = [val] + self.store
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError(INDEX_ERROR)

        self.count -= 1
        return self.store.pop()

    def popleft(self):
        if self.count == 0:
            raise IndexError(INDEX_ERROR)

        first_val, *rest = self.store
        self.store = rest
        self.count -= 1
        return first_val

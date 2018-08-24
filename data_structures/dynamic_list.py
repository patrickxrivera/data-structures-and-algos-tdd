# Pros:
# 1) O(1) lookup time when you know the index
# 2) Efficient itertion due to memory locality and caching
# 3) Space efficiency b/c array indices don't store extra information (like pointers)

# Cons:
# 1) O(n) lookup time when searching for value

# Notes:
# Instead of allocating a fixed slab of memory, many programming languages
# implement a "dynamic array/list". It works like this: A number of memory addresses are reserved for
# an array (let's say two). Once the array reaches the capacity, it doubles in size by copying
# all of the current elements to a new memory location that has four contiguous blocks of memory.
# That's it. The process is repeated until no more items are added. The copying may seem inefficient but
# it turns out to be only O(n) because by using some math we figure out that each item is copied on
# average 2 times (half the items are copied once, a quarter are copied twice, an eight are copied three times, ...)


POP_ERROR = "Can't pop an empty list!"
DELETE_AT_ERROR = "Can't delete an item at this index."


class DynamicList:
    def __init__(self, capacity=3):
        self.store = [None for _ in range(capacity)]
        self.capacity = capacity
        self.count = 0

    def append(self, val):
        if self.count == self.capacity:
            self.resize()

        self.store[self.count] = val
        self.count += 1

    def appendleft(self, val):
        # O(n) lookup... booo :(
        # Can use a heap instead which would be O(logn) lookup.
        self.store = [val] + self.store
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IndexError(POP_ERROR)

        popped_item = self.store[self.count - 1]

        self.store[self.count - 1] = None
        self.count -= 1

        return popped_item

    def popleft(self):
        if self.count == 0:
            raise IndexError(POP_ERROR)

        first_val, *rest = self.store
        self.store = [*rest, None]
        self.count -= 1
        return first_val

    def resize(self):
        self.capacity *= 2

        self.store = [
            self.store[idx] if idx < self.capacity / 2 else None
            for idx in range(self.capacity)
        ]

    def delete_at(self, idx):
        if idx < 0 or idx >= self.capacity:
            raise IndexError(DELETE_AT_ERROR)

        is_deleted = False

        for curr_idx, item in enumerate(self.store):
            if curr_idx == idx:
                is_deleted = True

            if is_deleted:
                try:
                    self.store[curr_idx] = self.store[curr_idx + 1]
                except:
                    self.store[curr_idx] = None

    @property
    def last(self):
        return self.store[self.count - 1]

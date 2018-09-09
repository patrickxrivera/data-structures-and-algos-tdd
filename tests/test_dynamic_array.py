from data_structures import DynamicArray
from unittest import TestCase


class TestDynamicArray(TestCase):
    def setUp(self):
        self.dyn_arr = DynamicArray()
        self.dyn_arr.append(1)
        self.dyn_arr.append(2)
        self.dyn_arr.append(3)

    def test_append(self):
        """Appends items onto list"""
        self.assertEqual(self.dyn_arr.store[0], 1)
        self.assertEqual(self.dyn_arr.store[1], 2)
        self.assertEqual(self.dyn_arr.store[2], 3)

    def test_appendleft(self):
        """Appends item to beginning of list"""
        self.dyn_arr.appendleft(0)

        self.assertEqual(self.dyn_arr.store[0], 0)

    def test_pop(self):
        """Pop last item off list"""
        self.dyn_arr.pop()

        self.assertEqual(self.dyn_arr.last, 2)
        self.assertEqual(self.dyn_arr.pop(), 2)

    def test_popleft(self):
        """Pops first item in list"""
        self.dyn_arr.popleft()

        self.assertEqual(self.dyn_arr.store[0], 2)
        self.assertEqual(self.dyn_arr.popleft(), 2)

    def test_over_indexing_error(self):
        """Raises IndexError when trying to pop an empty list"""
        self.dyn_arr.pop()
        self.dyn_arr.pop()
        self.dyn_arr.pop()

        with self.assertRaises(IndexError):
            self.dyn_arr.pop()
            self.dyn_arr.popleft()

    def test_mix_of_append_pop(self):
        """Tests append and pop together"""
        self.dyn_arr.popleft()
        self.dyn_arr.append(10)
        self.dyn_arr.appendleft(15)

        self.assertEqual(self.dyn_arr.store[0], 15)
        self.assertEqual(self.dyn_arr.store[1], 2)
        self.assertEqual(self.dyn_arr.store[-1], 10)

    def test_resize(self):
        """Ensures list resizes when it hits capacity"""
        self.assertEqual(self.dyn_arr.capacity, 3)

        self.dyn_arr.append(4)

        self.assertEqual(self.dyn_arr.capacity, 6)

    def test_delete_at(self):
        """Deletes an item at a given index"""
        self.dyn_arr.delete_at(1)

        self.assertEqual(self.dyn_arr.store[0], 1)
        self.assertEqual(self.dyn_arr.store[1], 3)
        self.assertEqual(self.dyn_arr.store[2], None)

    def test_delete_at_error(self):
        """Raises an exception when trying to delete at an invalid index"""
        with self.assertRaises(IndexError):
            self.dyn_arr.delete_at(3)
            self.dyn_arr.delete_at(-2)

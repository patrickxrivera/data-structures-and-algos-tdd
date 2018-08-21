from data_structures import DynamicList
from unittest import TestCase


class TestDynamicArray(TestCase):
    def setUp(self):
        self.dyn_list = DynamicList()
        self.dyn_list.append(1)
        self.dyn_list.append(2)
        self.dyn_list.append(3)

    def test_append(self):
        """Appends items onto list"""
        self.assertEqual(self.dyn_list.store[0], 1)
        self.assertEqual(self.dyn_list.store[1], 2)
        self.assertEqual(self.dyn_list.store[2], 3)

    def test_appendleft(self):
        """Appends item to beginning of list"""
        self.dyn_list.appendleft(0)
        self.assertEqual(self.dyn_list.store[0], 0)

    def test_pop(self):
        """Pop last item off list"""
        self.dyn_list.pop()
        self.assertEqual(self.dyn_list.store[-1], 2)
        self.assertEqual(self.dyn_list.pop(), 2)

    def test_popleft(self):
        """Pops first item in list"""
        self.dyn_list.popleft()
        self.assertEqual(self.dyn_list.store[0], 2)
        self.assertEqual(self.dyn_list.popleft(), 2)

    def test_over_indexing_error(self):
        """Raises IndexError when trying to pop an empty list"""
        self.dyn_list.pop()
        self.dyn_list.pop()
        self.dyn_list.pop()
        self.assertRaises(IndexError, self.dyn_list.pop)
        self.assertRaises(IndexError, self.dyn_list.popleft)

    def test_mix_of_append_pop(self):
        """Tests append and pop at together"""
        self.dyn_list.popleft()
        self.dyn_list.append(10)
        self.dyn_list.appendleft(15)
        self.assertEqual(self.dyn_list.store[0], 15)
        self.assertEqual(self.dyn_list.store[1], 2)
        self.assertEqual(self.dyn_list.store[-1], 10)


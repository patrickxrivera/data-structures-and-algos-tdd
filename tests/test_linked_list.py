from algorithms.linked_list import *
from algorithms.linked_list import SinglyLinkedList as Node

from unittest import TestCase


class TestLinkedList(TestCase):
    def test_contains_true(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three

        self.assertTrue(contains(one, 3))

    def test_contains_false(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three

        self.assertFalse(contains(one, 4))


if __name__ == "__main__":
    unittest.main()

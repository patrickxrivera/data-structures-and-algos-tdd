from data_structures import SinglyLinkedList

from unittest import TestCase


class TestSinglyLinkedList(TestCase):
    def setUp(self):
        self.sll = SinglyLinkedList()
        self.sll.insert(1)
        self.sll.insert(2)
        self.sll.insert(3)

    def test_insert(self):
        """Ensures linked list can insert values"""
        self.assertEqual(self.sll.head.val, 1)
        self.assertEqual(self.sll.head.next.val, 2)
        self.assertEqual(self.sll.head.next.next.val, 3)

    def test_contains(self):
        """Return boolean indicating whether linked list contains given value"""
        self.assertTrue(self.sll.contains(3))
        self.assertFalse(self.sll.contains(4))

        self.sll.insert(4)

        self.assertTrue(self.sll.contains(4))


if __name__ == "__main__":
    unittest.main()

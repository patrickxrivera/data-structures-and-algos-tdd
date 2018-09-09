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

    def test_search(self):
        """Return node with given value if it exists in linked list, otherwise returns False"""
        target_node = self.sll.search(2)

        self.assertEqual(target_node.val, 2)
        self.assertEqual(target_node.next.val, 3)

        self.assertFalse(self.sll.search(4))

    def test_remove_head(self):
        self.assertEqual(self.sll.head.val, 1)

        self.sll.remove_head()

        self.assertEqual(self.sll.head.val, 2)
        self.assertEqual(self.sll.head.next.val, 3)
        self.assertEqual(self.sll.head.next.next, None)

    def test_remove_head_only(self):
        self.sll.remove_node(3)
        self.sll.remove_node(2)

        self.assertEqual(self.sll.head.val, 1)
        self.assertEqual(self.sll.head.next, None)

        self.sll.remove_head()

        self.assertEqual(self.sll.head.val, None)

    def test_delete_node(self):
        self.sll.remove_node(2)

        self.assertEqual(self.sll.head.val, 1)
        self.assertEqual(self.sll.head.next.val, 3)

        self.sll.remove_node(1)

        self.assertEqual(self.sll.head.val, 3)

        self.sll.remove_node(3)

        self.assertEqual(self.sll.head.val, None)


if __name__ == "__main__":
    unittest.main()

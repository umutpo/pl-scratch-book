import unittest
from linkedList import Node

class Queue:
    def __init__(self):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def dequeue(self):
        raise NotImplementedError()

    def enqueue(self, value):
        raise NotImplementedError()

class QueueLinkedList(Queue):
    """
    Queue implementation using Linked List
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def empty(self):
        """
        Return whether the Queue is empty or not
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        return self.size <= 0
    
    def dequeue(self):
        """
        Remove and return the first element
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        if self.size > 0:
            value = self.head.value
            node = self.head

            self.head = node.next
            del node
            self.size -= 1

            return value
        
        return None
    
    def enqueue(self, value):
        """
        Insert the value as the last element
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        node = Node(value)
        if self.size > 0:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

        self.size += 1

class QueueArray(Queue):
    """
    Queue implementation using Dynamic Array

    Note: Python's own Deque(Double-ended queue implemented with doubly-linked list/circular array) 
          module is much more performant than its List due to the expensive operation of 
          inserting/popping at the beginning of a List
    """
    def __init__(self):
        self.list = []
        self.size = 0
    
    def empty(self):
        """
        Return whether the Queue is empty or not
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        return self.size <= 0
    
    def dequeue(self):
        """
        Remove and return the first element
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        if self.size > 0:
            self.size -= 1
            return self.list.pop(0)
        
        return None
    
    def enqueue(self, value):
        """
        Insert the value as the last element
        - Time Complexity: O(1) with linear amortized time
                           since O(n) over n pushes with
                           correct growth scale
        - Space Complexity: O(1)
        """
        self.size += 1
        self.list.append(value)

# Testing
if __name__ == "__main__":
    class TestQueue(unittest.TestCase):
        def test_Queue_linked_list(self):
            queue = QueueLinkedList()
            self.assertTrue(queue.empty())
            queue.enqueue(3)
            self.assertFalse(queue.empty())
            queue.enqueue(2)
            queue.enqueue(1)
            self.assertEqual(queue.dequeue(), 3)
            self.assertNotEqual(queue.dequeue(), 1)
            self.assertEqual(queue.dequeue(), 1)
        
        def test_Queue_array(self):
            queue = QueueArray()
            self.assertTrue(queue.empty())
            queue.enqueue(3)
            self.assertFalse(queue.empty())
            queue.enqueue(2)
            queue.enqueue(1)
            self.assertEqual(queue.dequeue(), 3)
            self.assertNotEqual(queue.dequeue(), 1)
            self.assertEqual(queue.dequeue(), 1)

    unittest.main()
import unittest

class Node:
    """
    Basic Node implementation for Linked List
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return "[{0}] -> {1}".format(self.value, self.next)

class Stack:
    def __init__(self):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def pop(self):
        raise NotImplementedError()

    def push(self):
        raise NotImplementedError()

class StackLinkedList(Stack):
    """
    Stack implementation using Linked List
    """
    def __init__(self):
        self.head = None
        self.size = 0
    
    def empty(self):
        """
        Return whether the Stack is empty or not
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        return self.size <= 0
    
    def pop(self):
        """
        Remove and return the top element
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
    
    def push(self, value):
        """
        Insert the value as the top element
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

class StackArray(Stack):
    """
    Stack implementation using Dynamic Array
    """
    def __init__(self):
        self.list = []
        self.size = 0
    
    def empty(self):
        """
        Return whether the Stack is empty or not
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        return self.size <= 0
    
    def pop(self):
        """
        Remove and return the top element
        - Time Complexity: O(1)
        - Space Complexity: O(1)

        Note: Using the last element as top for performance reasons
        """
        if self.size > 0:
            self.size -= 1
            return self.list.pop()
        
        return None
    
    def push(self, value):
        """
        Insert the value as the top element
        - Time Complexity: O(1) with linear amortized time
                           since O(n) over n pushes with
                           correct growth scale
        - Space Complexity: O(1)

        Note: Using the last element as top for performance reasons
        """
        self.size += 1
        self.list.append(value)

# Testing
if __name__ == "__main__":
    class TestStack(unittest.TestCase):
        def test_stack_linked_list(self):
            stack = StackLinkedList()
            self.assertTrue(stack.empty())
            stack.push(3)
            self.assertFalse(stack.empty())
            stack.push(2)
            stack.push(1)
            self.assertEqual(stack.pop(), 1)
            self.assertNotEqual(stack.pop(), 3)
        
        def test_stack_array(self):
            stack = StackArray()
            self.assertTrue(stack.empty())
            stack.push(3)
            self.assertFalse(stack.empty())
            stack.push(2)
            stack.push(1)
            self.assertEqual(stack.pop(), 1)
            self.assertNotEqual(stack.pop(), 3)

    unittest.main()
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

class LinkedList:
    """
    Linked List implementation with utility functions
    """
    def __init__(self, head=None):
        self.head = head
    
    def print(self):
        """
        Print the linked list in order
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        def print_recur(node):
            if node != None:
                print(node.value, end=", ")
                print_recur(node.next)

        print_recur(self.head)
    
    def print_reverse(self):
        """
        Print the linked list in reverse order
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        def print_recur(node):
            if node != None:
                print_recur(node.next)
                print(node.value, end=", ")

        print_recur(self.head)
    
    def get_value(self, index):
        """
        Get the value in given index
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        def get_node_recur(index, node):
            if index == 0:
                return node.value
            elif node != None:
                return get_node_recur(index - 1, node.next)
            else:
                return None
        
        return get_node_recur(index, self.head)

    def get_node(self, value):
        """
        Get the node with the given node
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        current = self.head
        while current != None:
            if current.value == value:
                return current
        
        return None

    def insert(self, index, value):
        """
        Insert the given value in given index
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        new_node = Node(value)

        prev = None
        current = self.head
        while index > 0 and current != None:
            prev = current
            current = current.next
            index -= 1
        
        if prev == None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = current
            prev.next = new_node

    def insert_at_front(self, value):
        """
        Insert the given value at the front of the list
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        self.insert(0, value)
    
    def remove(self, index):
        """
        Remove the node at the given index
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        prev = None
        current = self.head
        while index > 0 and current != None:
            prev = current
            current = current.next
            index -= 1

        # Remove at the beginning
        if prev == None:
            self.head = current.next
        # Remove at the end
        elif current == None:
            prev.next = None
        # Remove in the middle
        else:
            prev.next = current.next
        
        del current
        
    def reverse(self):
        """
        Reverse the linked list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        self.head = prev

# Testing
if __name__ == "__main__":
    def create_long_linked_list():
            linked_list = LinkedList()
            for i in range(5, -1, -1):
                linked_list.insert_at_front(i)
            return linked_list

    class TestLinkedList(unittest.TestCase):
        def test_node_constructor(self):
            node = Node(2)
            self.assertEqual(node.value, 2)
            self.assertEqual(node.next, None)
        
        def test_linked_list_constructor(self):
            node = Node(2)
            linked_list = LinkedList(node)
            self.assertEqual(linked_list.head, node)
            self.assertEqual(linked_list.head.next, None)
        
        def test_linked_list_insert_at_front(self):
            linked_list = create_long_linked_list()
            ptr = linked_list.head
            ptr_value = 0
            while ptr != None:
                self.assertEqual(ptr.value, ptr_value)
                ptr_value += 1
                ptr = ptr.next
        
        def test_linked_list_insert(self):
            linked_list = create_long_linked_list()
            linked_list.insert(2, 20)
            self.assertEqual(linked_list.get_value(2), 20)

        def test_linked_list_remove(self):
            linked_list = create_long_linked_list()
            linked_list.remove(2)
            self.assertEqual(linked_list.get_value(1), 1)
            self.assertEqual(linked_list.get_value(2), 3)
        
        def test_linked_list_reverse(self):
            linked_list = create_long_linked_list()
            linked_list.reverse()
            ptr = linked_list.head
            ptr_value = 5
            while ptr != None:
                self.assertEqual(ptr.value, ptr_value)
                ptr_value -= 1
                ptr = ptr.next

    unittest.main()
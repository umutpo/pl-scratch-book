import unittest

class Node:
    """
    Basic Node implementation for Linked List
    """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return "[{0}] -> {1}".format(self.data, self.next)

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
                print(node.data, end=", ")
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
                print(node.data, end=", ")

        print_recur(self.head)
    
    def get_node(self, index):
        """
        Get the node in given index
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        def get_node_recur(index, node):
            if index == 0:
                return node
            elif node != None:
                return get_node_recur(index - 1, node.next)
            else:
                return None
        
        return get_node_recur(index, self.head)

    def get_node(self, data):
        """
        Get the node with the given node
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        current = self.head
        while current != None:
            if current.data == data:
                return current
        
        return None

    def insert(self, index, node):
        """
        Insert the given node in given index
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        prev = None
        current = self.head
        while index > 0 and current != None:
            prev = current
            current = current.next
            index -= 1
        
        if prev == None:
            node.next = self.head
            self.head = node
        else:
            node.next = current
            prev.next = node

    def insert_at_front(self, node):
        """
        Insert the given node at the front of the list
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        self.insert(0, node)
    
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
                linked_list.insert_at_front(Node(i))
            return linked_list

    class TestLinkedList(unittest.TestCase):
        def test_node_constructor(self):
            node = Node(2)
            self.assertEqual(node.data, 2)
            self.assertEqual(node.next, None)
        
        def test_linked_list_constructor(self):
            node = Node(2)
            linked_list = LinkedList(node)
            self.assertEqual(linked_list.head, node)
            self.assertEqual(linked_list.head.next, None)
        
        def test_linked_list_insert_at_front(self):
            linked_list = create_long_linked_list()
            ptr = linked_list.head
            ptr_data = 0
            while ptr != None:
                self.assertEqual(ptr.data, ptr_data)
                ptr_data += 1
                ptr = ptr.next
        
        def test_linked_list_insert(self):
            linked_list = create_long_linked_list()
            new_node = Node(20)
            linked_list.insert(2, new_node)
            self.assertEqual(linked_list.get_node(2), new_node)

        def test_linked_list_remove(self):
            linked_list = create_long_linked_list()
            linked_list.remove(2)
            self.assertEqual(linked_list.get_node(1).data, 1)
            self.assertEqual(linked_list.get_node(2).data, 3)
        
        def test_linked_list_reverse(self):
            linked_list = create_long_linked_list()
            linked_list.reverse()
            ptr = linked_list.head
            ptr_data = 5
            while ptr != None:
                self.assertEqual(ptr.data, ptr_data)
                ptr_data -= 1
                ptr = ptr.next

    unittest.main()
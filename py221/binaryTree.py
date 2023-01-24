import unittest

class Node:
    """
    Basic Node implementation for Binary Tree
    """
    def __init__(self, value, *, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 0 # Height is used in AVL trees for more performant operations
        
    def get_height(self):
        """
        Returns the height of the Binary Tree Node
            where the height is the longest path from this node to a leaf node      
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes 
        - Space Complexity: O(1)
        """
        def _get_height(node):
            if node != None:
                return 1 + max(_get_height(node.left), _get_height(node.right))
            return -1
        
        return _get_height(self)

    def get_balance(self):
        """
        Returns the balance of the Binary Tree Node
            where the balance is the height difference between its right and left child 
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes 
        - Space Complexity: O(1)
        """
        right_height = 0
        if self.right != None:
            right_height = self.right.height + 1
        
        left_height = 0
        if self.left != None:
            left_height = self.left.height + 1
        
        return right_height - left_height
    
    def left_rotate(self):
        """
        Rotating the node left, mostly used in AVL Tree implementations for balancing
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        right_node = self.right
        self.right = right_node.left
        right_node.left = self

        self.height = self.get_height()
        right_node.height = right_node.get_height()
        return right_node

    def right_rotate(self):
        """
        Rotating the node right, mostly used in AVL Tree implementations for balancing
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        left_node = self.left
        self.left = left_node.right
        left_node.right = self

        self.height = self.get_height()
        left_node.height = left_node.get_height()
        return left_node

class BinaryTree:
    """
    Binary Tree implementation with utility functions
    - Full Binary Tree: Every node has 2 or 0 children
    - Perfect Binary Tree: All non-leaf nodes have 2 children and all leaves have same depth
    - Complete Binary Tree: Every non-leaf level is filled and the leaf level has all nodes to most-left
    """
    def __init__(self, root=None):
        self.root = root
    
    def get_height(self):
        return self.root.get_height()
    
    def print_preorder_traversal(self):
        """
        Print the nodes by traversing current -> left -> right
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes 
        - Space Complexity: O(1)
        """
        def _print_preorder_traversal(node):
            if node != None:
                print(node.value, end=", ")
                _print_preorder_traversal(node.left)
                _print_preorder_traversal(node.right)
        
        _print_preorder_traversal(self.root)
    
    def print_inorder_traversal(self):
        """
        Print the nodes by traversing left -> current -> right
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes 
        - Space Complexity: O(1)
        """
        def _print_inorder_traversal(node):
            if node != None:
                _print_inorder_traversal(node.left)
                print(node.value, end=", ")
                _print_inorder_traversal(node.right)
        
        _print_inorder_traversal(self.root)
    
    def print_postorder_traversal(self):
        """
        Print the nodes by traversing left -> right -> current
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes 
        - Space Complexity: O(1)
        """
        def _print_postorder_traversal(node):
            if node != None:
                _print_postorder_traversal(node.left)
                _print_postorder_traversal(node.right)
                print(node.value, end=", ")
        
        _print_postorder_traversal(self.root)

class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree implementation with utility functions

    Note: Technically can be used to implement a dictionary if "Key" is added to
    Node class
    """
    def find(self, value):
        """
        Find the node with the given value in the Binary Search Tree
        - Time Complexity: O(h) where h = height
        - Space Complexity: O(1)
        """
        def _find(node):
            if node != None:
                if node.value > value:
                    return _find(node.left)
                elif node.value < value:
                    return _find(node.right)
                else:
                    return node
        
        return _find(self.root)

    def insert(self, value):
        """
        Insert a new node with the given value to the Binary Search Tree
        - Time Complexity: O(h) where h = height
        - Space Complexity: O(1)
        """
        def _insert(node):
            if node == None:
                return Node(value)
            else:
                if node.value > value:
                    node.left = _insert(node.left)
                elif node.value < value:
                    node.right = _insert(node.right)
                else:
                    raise ValueError("The given value already exists in the Binary Search Tree")
                return node

        self.root = _insert(self.root)

    def remove(self, value):
        """
        Remove the node with the given value from the Binary Search Tree
        - Time Complexity: O(h) where h = height
        - Space Complexity: O(1)
        """
        def getRightMostChild(node):
            if node.right == None:
                return node
            return getRightMostChild(node.right)
        
        def _remove(node, value):
            if node != None:
                if node.value > value:
                    node.left = _remove(node.left, value)
                elif node.value < value:
                    node.right = _remove(node.right, value)
                else:
                    if node.right == None:
                        left = node.left
                        del node
                        return left
                    elif node.left == None:
                        right = node.right
                        del node
                        return right
                    else:
                        new_node = getRightMostChild(node.left)
                        node.value = new_node.value
                        node.left = _remove(node.left, new_node.value)

                return node
                    
        self.root = _remove(self.root, value)

    def print(self):
        """
        Print the nodes in the Binary Search Tree by their order
        - Time Complexity: O(2^h or n) where h = height and n = number of nodes
        - Space Complexity: O(1)
        """
        self.print_inorder_traversal()

class AVLTree(BinarySearchTree):
    """
    A self rotating Binary Search Tree named after its inventors Adelson-Velsky-Landis

    Since the AVL tree is always balanced, all operations take O(logn), unlike BST where
    operations take O(h) where h might be much larger than logn in certain cases

    For a node to be balanced, it should have the propery of |height(right) - height(left)| <= 1
    """
    def find(self, value):
        """
        Find the node with the given value in the AVL Tree
        - Time Complexity: O(logn) where n = number of nodes
        - Space Complexity: O(1)
        """
        self.find(value)
    
    def insert(self, value):
        """
        Insert a new node with the given value to the AVL Tree and rotate the tree to balance
        - Time Complexity: O(logn) where n = number of nodes
        - Space Complexity: O(1)
        """
        def _insert(node):
            if node == None:
                return Node(value)
            else:
                if node.value > value:
                    node.left = _insert(node.left)
                elif node.value < value:
                    node.right = _insert(node.right)
                else:
                    raise ValueError("The given value already exists in the Binary Search Tree")
                
                node.height = node.get_height()
                balance_factor = node.get_balance()
                if balance_factor > 1 and node.right.get_balance() >= 1:
                    return node.left_rotate()
                elif balance_factor < -1 and node.left.get_balance() <= -1:
                    return node.right_rotate()
                elif balance_factor > 1 and node.right.get_balance <= - 1:
                    node.right = node.right.right_rotate()
                    return node.left_rotate()
                elif balance_factor < -1 and node.left.get_balance() >= 1:
                    node.left = node.left.left_rotate()
                    return node.right_rotate()
                
                return node
        
        self.root = _insert(self.root)
    
    def remove(self, value):
        """
        Remove the node with the given value to the AVL Tree and rotate the tree to balance
        - Time Complexity: O(logn) where n = number of nodes
        - Space Complexity: O(1)
        """
        def getRightMostChild(node):
            if node.right == None:
                return node
            return getRightMostChild(node.right)
        
        def _remove(node, value):
            if node != None:
                if node.value > value:
                    node.left = _remove(node.left, value)
                elif node.value < value:
                    node.right = _remove(node.right, value)
                else:
                    if node.right == None:
                        left = node.left
                        del node
                        return left
                    elif node.left == None:
                        right = node.right
                        del node
                        return right
                    else:
                        new_node = getRightMostChild(node.left)
                        node.value = new_node.value
                        node.left = _remove(node.left, new_node.value)
            
                node.height = node.get_height()
                balance_factor = node.get_balance()
                if balance_factor > 1 and node.right.get_balance() >= 0:
                    return node.left_rotate()
                elif balance_factor < -1 and node.left.get_balance() <= 0:
                    return node.right_rotate()
                elif balance_factor > 1 and node.right.get_balance() < 0:
                    node.right = node.right.right_rotate()
                    return node.left_rotate()
                elif balance_factor < -1 and node.left.get_balance() > 0:
                    node.left = node.left.left_rotate()
                    return node.right_rotate()

                return node
                    
        self.root = _remove(self.root, value)
        
        def print(self):
            """
            Print the nodes in the AVL Tree by their order
            - Time Complexity: O(2^h or n) where h = height and n = number of nodes
            - Space Complexity: O(1)
            """
            self.print_inorder_traversal()

        


if __name__ == "__main__":
    def get_test_binary_tree():
        root = Node(0, left=Node(1, left=Node(2), right=Node(3, right=Node(4))), right=Node(5, left=Node(6), right=Node(7, left=Node(8), right=Node(9, left=Node(10, left=Node(11))))))
        return BinaryTree(root)
    
    def get_test_binary_search_tree():
        tree = BinarySearchTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(12)
        tree.insert(3)
        tree.insert(-1)
        tree.insert(70)
        tree.insert(11)
        tree.insert(4)
        return tree
    
    def get_test_avl_tree():
        tree = AVLTree()
        tree.insert(10)
        tree.insert(5)
        tree.insert(12)
        tree.insert(3)
        tree.insert(-1)
        tree.insert(70)
        tree.insert(11)
        tree.insert(4)
        return tree
    
    class TestBinaryTree(unittest.TestCase):
        def test_get_height(self):
            tree = get_test_binary_tree()
            self.assertEqual(tree.get_height(), 5)
    
        def test_print_preorder(self):
            """
            Should print 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            """
            tree = get_test_binary_tree()

            print("Pre-order Traversal Test: ")
            tree.print_preorder_traversal()
            print("\n")
        
        def test_print_inorder(self):
            """
            Should print 2, 1, 3, 4, 0, 6, 5, 8, 7, 11, 10, 9,
            """
            tree = get_test_binary_tree()

            print("In-order Traversal Test: ")
            tree.print_inorder_traversal()
            print("\n")
        
        def test_print_postorder(self):
            """
            Should print 2, 4, 3, 1, 6, 8, 11, 10, 9, 7, 5, 0,
            """
            tree = get_test_binary_tree()

            print("Post-order Traversal Test: ")
            tree.print_postorder_traversal()
            print("\n")

        def test_bst_insert(self):
            """
            Should print -1, 3, 4, 5, 10, 11, 12, 70, 
            """
            tree = get_test_binary_search_tree()

            print("Binary Search Tree Insert Test: ")
            tree.print()
            print("\n")
        
        def test_bst_find(self):
            tree = get_test_binary_search_tree()
            self.assertEqual(tree.find(3).left.value, -1)
            self.assertEqual(tree.find(3).right.value, 4)
        
        def test_bst_remove(self):
            tree = get_test_binary_search_tree()
            tree.remove(3)
            self.assertEqual(tree.root.left.left.value, -1)
            self.assertEqual(tree.root.left.left.right.value, 4)

        def test_bst_balance(self):
            tree = get_test_binary_search_tree()
            tree.insert(-3)
            balance_factor = tree.root.right.get_height() - tree.root.left.get_height()
            self.assertEqual(balance_factor, -2)

        def test_avl_balance_insert(self):
            tree = get_test_avl_tree()
            tree.insert(-3)
            self.assertEqual(tree.root.get_balance(), -1)
            tree.insert(0)
            tree.insert(-5)
            self.assertEqual(tree.root.get_balance(), 0)
            self.assertEqual(tree.root.value, 3)
        
        def test_avl_balance_remove(self):
            tree = get_test_avl_tree()
            tree.remove(70)
            tree.remove(11)
            self.assertEqual(tree.root.get_balance(), 0)
            self.assertEqual(tree.root.value, 5)

    unittest.main()
        
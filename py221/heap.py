import unittest

class MinBinaryHeap:
    """
    Minimum Binary Heap ADT implemented with a dynamic array

    Note: By using Python's list which benefits from the internal
    implementation of a dynamic array, we do not have to manually manage 
    the underlying data structure to grow and shrink 
    """
    def __init__(self, array=None):
        if array != None:
            self.build_heap(array)
        else:
            self.heap = []

    def build_heap(self, array):
        """
        Build the heap from the given array by calling heapify down on non-leaf children
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        """
        self.heap = array[:]
        for i in range(len(array) // 2, -1, -1):
            self.heapify_down(i)

    def heapify_up(self, index):
        """
        Swap the given child with its parent recursively until it is larger than its parent
        - Time Complexity: O(logn)
        - Space Complexity: O(1)
        """
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.heapify_up(parent_index)
    
    def heapify_down(self, index):
        """
        Swap the given child with its children recursively until it is smaller than both of its children
        - Time Complexity: O(logn)
        - Space Complexity: O(1)
        """
        def get_min_child_index(index):
            last_index = len(self.heap) - 1
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            smaller_index = -1
            if left_child_index <= last_index and right_child_index <= last_index:
                smaller_index = left_child_index if self.heap[left_child_index] < self.heap[right_child_index] else right_child_index
            elif left_child_index <= last_index:
                smaller_index = left_child_index
            elif right_child_index <= last_index:
                smaller_index = right_child_index
            
            return smaller_index
        
        min_child_index = get_min_child_index(index)
        if min_child_index >= 0 and self.heap[index] > self.heap[min_child_index]:
            self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
            self.heapify_down(min_child_index)
    
    def insert(self, value):
        """
        Insert the given value while preserving the heap property
        - Time Complexity: O(logn)
        - Space Complexity: O(1)
        """
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)
    
    def remove_min(self):
        """
        Remove the minimum value while preserving the heap property
        - Time Complexity: O(logn)
        - Space Complexity: O(1)
        """
        if len(self.heap) == 1:
            return self.heap.pop()

        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return minimum

    def peek(self):
        """
        Returns the minimum element in the heap based on its priority
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        """
        if len(self.heap) < 1:
            return None
        
        return self.heap[0]

if __name__ == "__main__":
    def get_test_heap():
        heap = MinBinaryHeap()
        heap.insert(10)
        heap.insert(50)
        heap.insert(20)
        heap.insert(5)
        heap.insert(30)
        return heap
    
    class TestHeap(unittest.TestCase):
        def test_insert(self):
            heap = get_test_heap()
            heap.insert(3)
            heap.insert(15)
            heap.insert(4)
            self.assertEqual(heap.peek(), 3)
        
        def test_remove_min(self):
            heap = get_test_heap()
            self.assertEqual(heap.remove_min(), 5)
            self.assertEqual(heap.peek(), 10)
            self.assertEqual(heap.remove_min(), 10)
            self.assertEqual(heap.peek(), 20)

        def test_build_heap(self):
            array = [100, 55, 80, 15, 10, 245, 50, 45]
            heap = MinBinaryHeap()
            heap.build_heap(array)
            self.assertEqual(heap.remove_min(), 10)
            self.assertEqual(heap.peek(), 15)
            self.assertEqual(heap.remove_min(), 15)
            self.assertEqual(heap.peek(), 45)
            heap.insert(46)
            heap.insert(44)
            heap.insert(47)
            self.assertEqual(heap.peek(), 44)
    
    unittest.main()

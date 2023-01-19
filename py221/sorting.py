import unittest
import random

def selectionSort(array):
    """
    Selection Sort: Every iteration, SELECT the smallest element in rest of the 
                    array and swap it with the current element. Basically, divides
                    the array into unsorted and sorted parts where sorted part grows by
                    repeatedly finding the smallest element in the unsorted part.
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    """
    for i in range(len(array)):
        
        # Find the index of the smallest element
        current_min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current_min_index]:
                current_min_index = j
        
        # Swap the smallest element with the current element
        array[current_min_index], array[i] = array[i], array[current_min_index]
    
    return array

def insertionSort(array):
    """
    Insertion Sort: Every iteration, slide the previous elements that are greater to 
                    the right and INSERT the current element in the opened gap. Basically,
                    finds the correct place in the sorted part to place the first element
                    of the unsorted part.
    - Time Complexity: O(n^2)
    - Space Complexity: O(1)
    """
    for i in range(1, len(array)):
        current_element = array[i]
        
        # Shuffle up all sorted items > array[i]
        j = i
        while j > 0 and array[j - 1] > current_element:
            array[j] = array[j - 1]
            j -= 1
        
        # Insert the current element
        array[j] = current_element
    
    return array

def mergeSort(array):
    """
    Merge Sort: Divide the array in half recursively until each subarray has one element left, 
                then MERGE the sorted left half and the sorted right half. Basically,
                a divide and conquer algorithm where sorting happens during the merge step
    - Time Complexity: O(nlogn)
    - Space Complexity: O(1)
    """
    if len(array) > 1:
        middle = len(array) // 2
        
        # Sort the left half
        left_array = mergeSort(array[:middle])
        
        # Sort the right half
        right_array = mergeSort(array[middle:])

        # Merge the sorted left and right halves
        left, right, main = 0, 0, 0
        while left < len(left_array) and right < len(right_array):
            if left_array[left] < right_array[right]:
                array[main] = left_array[left]
                left += 1
            else:
                array[main] = right_array[right]
                right += 1
            main += 1
        
        while left < len(left_array):
            array[main] = left_array[left]
            left += 1
            main += 1

        while right < len(right_array):
            array[main] = right_array[right]
            right += 1
            main += 1
        
    return array

def quickSort(array):
    """
    Quick Sort: Choose a random pivot and put all the smaller elements to its left
                and all the larger elements to its right, then recursively do the same
                for left and right subarrays of the pivot.
    - Time Complexity: O(nlogn)
    - Space Complexity: O(1)
    """
    def partition(array, low, high):
        # Choose the rightmost element as pivot
        pivot = array[high]
        
        # Compare each element to pivot and swap their location
        current_index = low - 1
        for i in range(low, high):
            if array[i] <= pivot:
                current_index += 1
                array[current_index], array[i] = array[i], array[current_index]
        
        # Put the pivot in its correct location
        array[current_index + 1], array[high] = array[high], array[current_index + 1]

        return current_index + 1
    
    def _quickSort(array, low, high):
        if low < high:
            # Find the pivot and put the smaller/larger elements to its left/right
            pivot = partition(array, low, high)

            # Sort the left subarray of the pivot
            _quickSort(array, low, pivot - 1)

            # Sort the right subarray of the pivot
            _quickSort(array, pivot + 1, high)

        return array
    
    return _quickSort(array, 0, len(array) - 1)

if __name__ == "__main__":
    def testAllAlgorithms(assertEqualFunc, unsorted_array, sorted_array):
        sorting_algorithms = [selectionSort, insertionSort, mergeSort, quickSort]
        for i in range(len(sorting_algorithms)):
                assertEqualFunc(sorting_algorithms[i](unsorted_array[:]), sorted_array)

    class TestSorting(unittest.TestCase):
        def test_sort_empty_array(self):
            empty_array = []
            testAllAlgorithms(self.assertEqual, empty_array, empty_array)

        def test_sort_array(self):
            array = [5, 3, 2, 4, 1]
            sorted_array = [1, 2, 3, 4, 5]
            testAllAlgorithms(self.assertEqual, array, sorted_array)
        
        def test_sort_random_array(self):
            random_array = random.sample(range(0, 100), 50)
            sorted_array = sorted(random_array)
            testAllAlgorithms(self.assertEqual, random_array, sorted_array)
    
    unittest.main()
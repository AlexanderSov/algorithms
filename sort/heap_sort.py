"""Heap sort.

Complexity: O(n*log n)
Memory: O(1) Auxiliary

Heap sort is array with next properties:
- element of array is node of binary tree:
    - parent of i have index floor i/2 (e.g. (i-1)//2)
    - left child of i element have index 2*i + 1
    - right child have index 2*i + 2
- array satisfy main heap property:
    array[parent[i]] >= array[i] in case non-increasing heap
    array[parent[i]] <= array[i] in case non-decreasing heap
            0
        /       \
      1           2
    /  \        /   \
   3    4      5     6
  / \  / \    / \    / \
 7  8  9 10  11 12  13  14

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

Height of of above heap equel 3 (floor of log n, where n = heap_size)
"""
A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]


def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def heapify_max(array: list, index, heap_size):
    """Keeping main heap property (recursive).

    :param index: vertex index

    Complexity: O(log n)
    """
    left = left_child(index)
    right = right_child(index)
    if left < heap_size and array[left] > array[index]:
        largest = left
    else:
        largest = index
    if right < heap_size and array[right] > array[largest]:
        largest = right
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify_max(array, largest, heap_size)


def build_heap(array: list):
    """Build heap from list.

    Complexity: O(n)
    """
    for i in range(len(array)//2, -1, -1):
        heapify_max(array, i, len(array))


def heap_sort(array: list):
    """Heap sort

    Complexity: O(n*log n)
    """
    build_heap(array)
    heap_size = len(array)
    for i in range(heap_size-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        heapify_max(array, 0, heap_size)


def extract_max_heap(array: list) -> int:
    """Extract max element from heap.

    Complexity: O(1), but recovery main heap property require log n
    operations.

    :param array: list with heap
    :return: maximum heap element
    """
    if len(array) < 1:
        raise ValueError('Heap is empty')
    max_ = array[0]
    array[0] = array[-1]
    array.pop()
    heapify_max(array, 0, len(array))
    return max_


def insert_in_heap(array: list, value):
    """Insert value in heap.

    Complexity: O(log n)
    """
    array.append(value)
    i = len(array) - 1
    while i > 0 and array[parent(i)] < value:
        array[i] = array[parent(i)]
        i = parent(i)
    array[i] = value


if __name__ == '__main__':
    print(A)
    build_heap(A)
    insert_in_heap(A, 100)
    print(A)

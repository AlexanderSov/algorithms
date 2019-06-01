"""Quick sort.

Complexity: O(n*log n) in average and O(n**2) in worst case.
    Worst case occurs when dividing the list in task to subtasks with
    size n-1 and 1.

Memory: without additional memory
"""


def partition(array, first=None, last=None):
    """Find index of split point.

    Complexity: O(n)

    :param array: list with numbers
    :param first: start index of array
    :param last: last index of array
    :return: index of split point
    """
    x = array[first]
    i = first + 1
    j = last
    while True:
        while i <= j and array[i] <= x:
            i += 1
        while i <= j and array[j] >= x:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[first], array[j] = array[j], array[first]
    return j


def quick_sort(alist, p, r):
    """Quick sort."""
    print(alist)
    if p < r:
        q = partition(alist, p, r)
        print(q)
        quick_sort(alist, p, q - 1)
        quick_sort(alist, q + 1, r)

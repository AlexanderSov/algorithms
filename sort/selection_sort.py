def selection_sort(alist):
    """
    Complexity: O(n^2)
    Memory: in place
    Performs fewer permutations than bubble sort.
    """
    for i in range(len(alist)-1, 0, -1):
        position_max = 0
        for location in range(1, i+1):
            if alist[location] > alist[position_max]:
                position_max = location
        alist[i], alist[position_max] = alist[position_max], alist[i]

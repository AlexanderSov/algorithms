def insertion_sort(_list):
    """Insertion Sort

    Complexity: O(n^2)
    Memory: in place
    Useful for short arrays.
    """
    for i in range(1, len(_list)):
        value = _list[i]
        j = i - 1
        while j >= 0 and value < _list[j]:
            _list[j+1] = _list[j]
            j -= 1
        _list[j+1] = value
    return _list

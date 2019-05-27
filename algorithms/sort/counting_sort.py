def counting_sort(_list, k):
    """Counting sort.

    Sort is stable (Save order of equal elements from input list).
    Sorted values must be natural. It's use values like index of new
    list and write in value number of repeating values number of all
    previous sums.

    Complexity: O(n)
    Memory: use additional memory (2 lists) for saving index's and
            values. Length of additional lists equal k+n.

    :param _list: list for sorting.
    :param k: maximum value from _list.
    :return: sorted list
    """
    output = [0 for _ in range(len(_list))]
    helper = [0 for _ in range(k)]
    for i in range(0, len(_list)):
        helper[_list[i] - 1] = helper[_list[i] - 1] + 1
    previous_sum = helper[0]
    for i in range(1, k):
        if helper[i]:
            helper[i] += previous_sum
            previous_sum = helper[i]
    for i in range(len(_list) - 1, -1, -1):
        output[helper[_list[i] - 1] - 1] = _list[i]
        helper[_list[i] - 1] -= 1
    return output

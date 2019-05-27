"""Quick sort.

Complexity: O(n*log n) in average and O(n**2) in worst case.
    Worst case occurs when dividing the list in task to subtasks with
    size n-1 and 1.

Memory: without additional memory
"""


def partition(alist, p, r):
    """Find index of split point.

    Complexity: O(n)

    :param alist: list with numbers
    :param p: first element index
    :param r: last element index
    :return: index of split point
    """
    x = alist[p]
    i = p
    j = r
    while True:
        while i < j and alist[j] >= x:
            j -= 1
        while i < j and alist[i] < x:
            i += 1
        if i < j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            return j


def quick_sort_v1(alist, p, r):
    """Quick sort."""
    print(alist)
    if p < r:
        q = partition(alist, p, r)
        print(q)
        quick_sort_v1(alist, p, q)
        quick_sort_v1(alist, q + 1, r)


def get_middle_value(alist, start, end):
    largest = alist[start]
    if largest < alist[end]:
        largest = alist[end]
    from_middle = alist[(end-start)//2]
    if largest < from_middle:
        largest = from_middle
    return largest


def quick_sort_v2(alist, first, last):
    print(alist)
    if first < last:
        q = partion_v2(alist, first, last)
        quick_sort_v2(alist, first, q-1)
        quick_sort_v2(alist, q+1, last)


def partion_v2(alist, first, last):
    x = alist[first]
    i = first + 1
    j = last
    while True:
        while i <= j and alist[i] <= x:
            i += 1
        while i <= j and alist[j] >= x:
            j -= 1
        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            break

    alist[first], alist[j] = alist[j], alist[first]
    return j


if __name__ == '__main__':
    import random
    a = [random.randrange(100) for i in range(20)]
    quick_sort_v2(a, 0, len(a) - 1)
    print(a)

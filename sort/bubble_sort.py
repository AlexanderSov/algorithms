def bubble_sort(alist):
    """Bubble sort

    Complexity: O(n^2)
    Memory: in place
    """
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i+1] < alist[i]:
                alist[i+1], alist[i] = alist[i], alist[i+1]


def short_bubble_sort(alist):
    """Short bubble sort

    Complexity: O(n^2)
    Memory: in place
    Can be useful in case sorted sequence.
    """
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i+1] < alist[i]:
                exchanges = True
                alist[i+1], alist[i] = alist[i], alist[i+1]
        passnum -= 1

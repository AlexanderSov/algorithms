class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        return self._data.pop(0)

    def is_empty(self):
        return self._data == []

    def size(self):
        return len(self._data)


class Deque:
    def __init__(self):
        self._data = []

    def add_front(self, item):
        self._data.insert(0, item)

    def add_rear(self, item):
        self._data.append(item)

    def remove_front(self):
        return self._data.pop(0)

    def remove_rear(self):
        return self._data.pop()

    def is_empty(self):
        return self._data == []

    def size(self):
        return len(self._data)

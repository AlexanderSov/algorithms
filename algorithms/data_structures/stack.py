class Stack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return self._data == []

    def push(self, item):
        self._data.append(item)

    def peek(self):
        return self._data[-1]

    def pop(self):
        return self._data.pop()

    def size(self):
        return len(self._data)


# Simple Balance Parentheses
# To solve this problem can be used Stack

def check_parentheses_balance(string):
    s = Stack()
    balanced = True
    for i in string:
        if i == '(':
            s.push(i)
        else:
            try:
                s.pop()
            except IndexError:
                balanced = False
                break
    if balanced and s.is_empty():
        return True
    else:
        return False


def check_parentheses_balance_common(string):
    s = Stack()
    balanced = True
    for i in string:
        if i in '({[':
            s.push(i)
        else:
            try:
                if not check_symbol_match(s.pop(), i):
                    s.pop()
                else:
                    balanced = False
                    break
            except IndexError:
                balanced = False
                break
    if balanced and s.is_empty():
        return True
    else:
        return False


def check_symbol_match(open_, close_):
    opens = '({['
    closers = ')}]'
    return opens.index(open_) == closers.index(close_)


def convert_decimal_binary(number):
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number = number // 2
    bin_str = ''.join([str(s.pop()) for _ in range(s.size())])
    return bin_str

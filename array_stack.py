"""Array-based stack with a fixed capacity (LIFO)."""

class StackUnderflowError(Exception):
    """Raised when pop/peek is used on an empty stack."""


class StackOverflowError(Exception):
    """Raised when push is used on a full stack."""


class ArrayStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.items = [None] * capacity
        self.capacity = capacity
        self.top = -1

    def push(self, item):
        if self.is_full():
            raise StackOverflowError("Stack overflow: cannot push; stack is full.")
        self.top += 1
        self.items[self.top] = item

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot pop; stack is empty.")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot peek; stack is empty.")
        return self.items[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def display(self):
        return self.items[:self.top + 1]

    def __len__(self):
        return self.top + 1

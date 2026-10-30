"""Linked-list stack (LIFO), with no fixed capacity."""

class StackUnderflowError(Exception):
    """Raised when pop/peek is used on an empty stack."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot pop; stack is empty.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise StackUnderflowError("Stack underflow: cannot peek; stack is empty.")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.data)
            current = current.next
        return values

    def __len__(self):
        return self.size

"""Linked-list queue (FIFO), with head and tail references."""

class QueueUnderflowError(Exception):
    """Raised when dequeue/peek_front is used on an empty queue."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("Queue underflow: cannot dequeue; queue is empty.")
        item = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return item

    def peek_front(self):
        if self.is_empty():
            raise QueueUnderflowError("Queue underflow: cannot peek; queue is empty.")
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

"""Circular array queue (FIFO), using front and size."""

class QueueUnderflowError(Exception):
    """Raised when dequeue/peek_front is used on an empty queue."""


class QueueOverflowError(Exception):
    """Raised when enqueue is used on a full queue."""


class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.items = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise QueueOverflowError("Queue overflow: cannot enqueue; queue is full.")
        rear = (self.front + self.size) % self.capacity
        self.items[rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise QueueUnderflowError("Queue underflow: cannot dequeue; queue is empty.")
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.front = 0
        return item

    def peek_front(self):
        if self.is_empty():
            raise QueueUnderflowError("Queue underflow: cannot peek; queue is empty.")
        return self.items[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def display(self):
        return [
            self.items[(self.front + i) % self.capacity]
            for i in range(self.size)
        ]

    def __len__(self):
        return self.size

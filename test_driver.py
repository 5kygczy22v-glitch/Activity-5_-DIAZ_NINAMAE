"""Automated tests for the four stack and queue implementations."""

from array_stack import ArrayStack, StackUnderflowError, StackOverflowError
from linked_stack import LinkedStack
from array_queue import ArrayQueue, QueueUnderflowError, QueueOverflowError
from linked_queue import LinkedQueue
from main import balanced_parentheses


def test_array_stack():
    stack = ArrayStack(2)
    stack.push("A")
    stack.push("B")
    assert stack.peek() == "B"
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    assert stack.is_empty()
    try:
        stack.pop()
        assert False, "Expected underflow"
    except StackUnderflowError:
        pass
    stack.push("X")
    stack.push("Y")
    try:
        stack.push("Z")
        assert False, "Expected overflow"
    except StackOverflowError:
        pass


def test_linked_stack():
    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty()


def test_array_queue_and_wraparound():
    queue = ArrayQueue(3)
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    assert queue.dequeue() == "A"
    queue.enqueue("D")  # Uses the freed physical slot at the start.
    assert queue.display() == ["B", "C", "D"]
    assert queue.peek_front() == "B"
    assert queue.dequeue() == "B"
    assert queue.dequeue() == "C"
    assert queue.dequeue() == "D"
    assert queue.is_empty()
    try:
        queue.dequeue()
        assert False, "Expected underflow"
    except QueueUnderflowError:
        pass
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    try:
        queue.enqueue(4)
        assert False, "Expected overflow"
    except QueueOverflowError:
        pass


def test_linked_queue():
    queue = LinkedQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.peek_front() == "A"
    assert queue.dequeue() == "A"
    assert queue.dequeue() == "B"
    assert queue.is_empty()
    assert queue.head is None and queue.tail is None


def test_parentheses():
    assert balanced_parentheses("([]{})")
    assert balanced_parentheses("print((2 + 3) * [4])")
    assert not balanced_parentheses("([)]")
    assert not balanced_parentheses("(((")


if __name__ == "__main__":
    test_array_stack()
    test_linked_stack()
    test_array_queue_and_wraparound()
    test_linked_queue()
    test_parentheses()
    print("All tests passed.")

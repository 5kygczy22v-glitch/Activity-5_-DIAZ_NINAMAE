"""Menu-driven test driver for stacks, queues, and applications."""

from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def balanced_parentheses(expression):
    """Return True when (), [], and {} are correctly balanced."""
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack = []
    for character in expression:
        if character in opening:
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
    return len(stack) == 0


def print_queue_simulation():
    """Enqueue print jobs and process them in FIFO order."""
    from collections import deque

    jobs = deque()
    print("\nPRINT QUEUE SIMULATION")
    count = read_int("How many print jobs? ")
    for number in range(count):
        job_id = input(f"Job {number + 1} ID: ").strip()
        pages = read_int("Number of pages: ")
        jobs.append((job_id, pages))
        print(f"Enqueued {job_id}. Queue: {list(jobs)}")

    total_pages = 0
    print("\nPrinting in FIFO order:")
    while jobs:
        job_id, pages = jobs.popleft()
        total_pages += pages
        print(f"Printing {job_id} ({pages} pages). Remaining: {list(jobs)}")

    print(f"All jobs completed. Total pages: {total_pages}.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def show_state(structure):
    print("Current state:", structure.display())
    print("Empty:", structure.is_empty())
    if hasattr(structure, "is_full"):
        print("Full:", structure.is_full())


def stack_menu():
    print("\nChoose stack implementation:")
    print("1. ArrayStack (fixed capacity)")
    print("2. LinkedStack")
    choice = input("Choice: ").strip()

    if choice == "1":
        capacity = read_int("Stack capacity: ")
        try:
            stack = ArrayStack(capacity)
        except ValueError as error:
            print(error)
            return
    elif choice == "2":
        stack = LinkedStack()
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nSTACK MENU: 1 Push | 2 Pop | 3 Peek | 4 Display | 0 Back")
        option = input("Choose an operation: ").strip()
        try:
            if option == "1":
                value = input("Value to push: ")
                stack.push(value)
                print("Pushed:", value)
            elif option == "2":
                print("Popped:", stack.pop())
            elif option == "3":
                print("Top item:", stack.peek())
            elif option == "4":
                pass
            elif option == "0":
                break
            else:
                print("Invalid option.")
                continue
            show_state(stack)
        except (Exception,) as error:
            # The custom exceptions have descriptive messages.
            print("Error:", error)
            show_state(stack)


def queue_menu():
    print("\nChoose queue implementation:")
    print("1. Circular ArrayQueue (fixed capacity)")
    print("2. LinkedQueue")
    choice = input("Choice: ").strip()

    if choice == "1":
        capacity = read_int("Queue capacity: ")
        try:
            queue = ArrayQueue(capacity)
        except ValueError as error:
            print(error)
            return
    elif choice == "2":
        queue = LinkedQueue()
    else:
        print("Invalid choice.")
        return

    while True:
        print("\nQUEUE MENU: 1 Enqueue | 2 Dequeue | 3 Peek front | 4 Display | 0 Back")
        option = input("Choose an operation: ").strip()
        try:
            if option == "1":
                value = input("Value to enqueue: ")
                queue.enqueue(value)
                print("Enqueued:", value)
            elif option == "2":
                print("Dequeued:", queue.dequeue())
            elif option == "3":
                print("Front item:", queue.peek_front())
            elif option == "4":
                pass
            elif option == "0":
                break
            else:
                print("Invalid option.")
                continue
            show_state(queue)
        except Exception as error:
            print("Error:", error)
            show_state(queue)


def main():
    while True:
        print("\n===== STACKS AND QUEUES LAB =====")
        print("1. Stack operations")
        print("2. Queue operations")
        print("3. Balanced parentheses checker")
        print("4. Print queue simulation")
        print("0. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            stack_menu()
        elif choice == "2":
            queue_menu()
        elif choice == "3":
            expression = input("Enter an expression: ")
            if balanced_parentheses(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are NOT balanced.")
        elif choice == "4":
            print_queue_simulation()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

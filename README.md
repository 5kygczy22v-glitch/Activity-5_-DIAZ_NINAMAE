# Stacks and Queues: Array vs. Linked List

**Student:** Niña Mae P. Diaz  
**Course/Section:** BSIT-1B  
**Laboratory:** Stacks and Queues: Array vs. Linked List

## Description

This project implements four data structures from first principles:

1. `ArrayStack` — fixed-capacity stack using a `top` index.
2. `LinkedStack` — linked-list stack using a head reference.
3. `ArrayQueue` — circular array queue using `front` and `size`.
4. `LinkedQueue` — linked-list queue using head and tail references.

The menu-driven program also includes a balanced-parentheses checker and a FIFO print-queue simulation.

## Files

- `array_stack.py` — array-based stack.
- `linked_stack.py` — linked-list stack.
- `array_queue.py` — circular array queue.
- `linked_queue.py` — linked-list queue.
- `main.py` — interactive menu and application exercises.
- `test_driver.py` — automated tests for the four implementations.
- `sample-runs.md` — example program runs, including error handling and wrap-around.
- `analysis.md` — written answer to the analysis question.

## Requirements

- Python 3.8 or newer
- No third-party packages are required.

## How to Run

1. Download or clone the repository.
2. Open a terminal in the project folder.
3. Run the menu-driven program:

   ```bash
   python main.py
   ```

4. Run the automated tests:

   ```bash
   python test_driver.py
   ```

The expected test result is `All tests passed.`

## Notes

Array implementations require a positive capacity. They raise descriptive overflow or underflow exceptions when an operation cannot be completed. Linked-list implementations grow as items are added and raise underflow exceptions when an empty structure is accessed.

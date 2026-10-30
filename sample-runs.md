# Sample Runs

The following are representative sample runs. The exact prompts may vary slightly depending on the Python environment.

## 1. Array stack — push, pop, and overflow

```text
===== STACKS AND QUEUES LAB =====
1. Stack operations
2. Queue operations
3. Balanced parentheses checker
4. Print queue simulation
0. Exit
Enter choice: 1

Choose stack implementation:
1. ArrayStack (fixed capacity)
2. LinkedStack
Choice: 1
Stack capacity: 2

STACK MENU: 1 Push | 2 Pop | 3 Peek | 4 Display | 0 Back
Choose an operation: 1
Value to push: Book
Pushed: Book
Current state: ['Book']
Empty: False
Full: False

Choose an operation: 1
Value to push: Pen
Pushed: Pen
Current state: ['Book', 'Pen']
Empty: False
Full: True

Choose an operation: 1
Value to push: Bag
Error: Stack overflow: cannot push; stack is full.
Current state: ['Book', 'Pen']
Empty: False
Full: True
```

## 2. Stack underflow

```text
Choose an operation: 2
Popped: Pen
Current state: ['Book']
Empty: False
Full: False

Choose an operation: 2
Popped: Book
Current state: []
Empty: True
Full: False

Choose an operation: 2
Error: Stack underflow: cannot pop; stack is empty.
Current state: []
Empty: True
Full: False
```

## 3. Circular array queue — wrap-around

```text
===== STACKS AND QUEUES LAB =====
Enter choice: 2

Choose queue implementation:
1. Circular ArrayQueue (fixed capacity)
2. LinkedQueue
Choice: 1
Queue capacity: 3

Choose an operation: 1
Value to enqueue: A
Enqueued: A
Current state: ['A']

Choose an operation: 1
Value to enqueue: B
Enqueued: B
Current state: ['A', 'B']

Choose an operation: 1
Value to enqueue: C
Enqueued: C
Current state: ['A', 'B', 'C']
Full: True

Choose an operation: 2
Dequeued: A
Current state: ['B', 'C']
Full: False

Choose an operation: 1
Value to enqueue: D
Enqueued: D
Current state: ['B', 'C', 'D']
Full: True
```

The queue accepts `D` by reusing the physical array position that became free after `A` was dequeued. This demonstrates circular wrap-around.

## 4. Queue overflow and underflow

```text
Choose an operation: 1
Value to enqueue: E
Error: Queue overflow: cannot enqueue; queue is full.

Choose an operation: 2
Dequeued: B
Current state: ['C', 'D']
```

If dequeue is selected again after all remaining items have been removed, the program reports:

```text
Error: Queue underflow: cannot dequeue; queue is empty.
```

## 5. Balanced parentheses checker

```text
Enter choice: 3
Enter an expression: ([{}])
The parentheses are balanced.

Enter choice: 3
Enter an expression: ([)]
The parentheses are NOT balanced.
```

## 6. Print queue simulation

```text
Enter choice: 4
How many print jobs? 2
Job 1 ID: P001
Number of pages: 4
Enqueued P001. Queue: [('P001', 4)]
Job 2 ID: P002
Number of pages: 2
Enqueued P002. Queue: [('P001', 4), ('P002', 2)]

Printing in FIFO order:
Printing P001 (4 pages). Remaining: [('P002', 2)]
Printing P002 (2 pages). Remaining: []
All jobs completed. Total pages: 6.
```

## 7. Automated test result

Run `python test_driver.py`.

```text
All tests passed.
```

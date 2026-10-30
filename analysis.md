# Analysis Question

A linked-list stack pushes and pops at the head because the head can be updated directly, so both operations take O(1) time. Popping at the tail of a singly linked list would require searching from the head to find the node before the tail, which takes O(n) time. A circular array queue is used so that freed positions at the beginning of the array can be reused after the rear reaches the physical end. The `front` index and `size` counter distinguish the logical front and the number of stored items, making wrap-around possible without shifting elements.

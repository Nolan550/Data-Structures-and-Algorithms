# Stack (Data Structure)

## Overview

A **Stack** is a linear data structure that follows the **LIFO (Last-In First-Out)** principle.
The last element to be added in the stack will be the first element to be removed from the stack. A real-world scenario of how a stack works is a pile of plates, the last plate to be  kept in the pile will be the first plate to be removed.

Stacks are commonly used in:
- Undo/Redo operations
- Browser history
- Expression evaluation
- Recursion(call stack)

---
| Operation | Description |
|-----------|-------------|
| `push(data)`| Inserts an element at the top |
| `pop()` | Removes the top element |
| `peek()` | Returns the top element without removing it |
| `is_empty()` | Checks if the stack is empty |
|`display()` | Prints the stack from the top to bottom |

---

## Implementation Used: Linked List
This stack is implemented in **Java** and **Python** programming languages using *Linked list* as the underlying storage structure.
- Each node contains `data` and a `next` pointer
- `top` stores the pointer to the most recent node

  ---

  ## Project Structure
  This folder contains *stack.py*, *stack.java*, and a *readme.md* file.

  ## Example Usage

  ```
  python
  s = stack()

  s.push(10)
  s.push(11)
  s.push(12)
  s.push(13)
  s.push(14)
  s.push(15)


  s.display()

  ```
  **Sample Output**
  
  Stack (top → bottom): 15 --> 14 --> 13 --> 12 --> 11 --> 10

  ## What is Expected to learn from a stack
  - LIFO architecture
  - Implementing stacks using linked lists
  - Pointer movement and node creations
  - Handling underflow conditions

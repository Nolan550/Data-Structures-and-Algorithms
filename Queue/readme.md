# Queue(Data Structures)

## Overview
A **Queue** is a linear data structure that follows the **FIFO(First-In First-Out)** principle.
The first element to be inserted is the first element to be removed. A real-life example is people waiting in a line at the coffee shop or a theme park ride.

## Common Uses:
- Printer(printing queue)
- CPU scheduling
- Data buffering
- Handling requests in servers


## Key Operations
| Operation | Description |
| ----------- | ----------- |
|`enqueue(data)` | Inserts an element at the rear |
| `dequeue()` | Removes element from the front |
|`peek()` | Returns the front element without removing it |
|`is_empty()` | Checks if the queue is empty |
| `display()` | Shows elements from front to rear |


## Implementation Used: Linked List
This **Queue** data structure is implemented by using both **Java** and **Python** programming languages using linked list as the underlying storage structure.
- `front` pointer -> first element
- `rear` pointer -> last element
- Each node contains `data` and `next`

## Project Structure
This folder contains *queue.py*, *queue.java*, and a *readme.md* files.

## Example Usage
```
python
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")

q.display()
```
### Sample output:

Queue(front -> rear): A --> B --> C --> D --> E

## What is expected to learn from Queue
- FIFO mechanism
- Managing two pinters(front and rear)
- Preventing underflow
- Tarversing queues using linked lists



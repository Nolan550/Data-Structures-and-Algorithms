## Linked list(Data Structures)

This folder contains implementations of two types of linked lists:

- **Singly Linked List (SLL)**
- **Doubly Linked List (DLL)**

A linked List is a linear data structure where each element (node) contains `data` and `pointers` that link to other nodes.


# Singly Linked List (SLL)
A **Singly Linked List** stores each node with:
- `data`
- `next` -> pointer to the next node

  ## Available Methods
  | Method | Description |
  |-----------|-----------|
  | `append(data)` | Adds a new node at the end of the list |
  | `prepend(data)` | Adds a new node at the beginning of the list |
  | `deleteValue(data)` | Deletes the first node containing the given value |
  | `displayList()` | Prints all elements in the list in forward order |
  | `search(data)` | Checks if a value exists in the given list |

  ## Time Complexity (Singly Linked List)
  | Operation | Time Complexity |
  | ----------|-----------------|
  | Append | O(n) |
  |Prepend | O(1) |
  | Delete by value | O(n) |
  | Search | O(n) |
  | Display | O(n) |

  ## Example usage Singly Linked List
  ```
  python
  list = singlyLinkedList()
  list.append(10)
  list.append(11)
  list.append(12)
  list.append(13)
  list.append(14)

  list.prepend(5)

  list.displayList()
  print(list.search(12))
  list.deleteValue(10)
  list.displayList()
  ```
  **Output:**
  5 -> 10 -> 11 -> 12 -> 13 -> 14 -> NULL

  **True**

  5 -> 11 -> 12 -> 13 -> 14 -> NULL


# Doubly Linked List(DLL)

A **Doubly Linked List** stores each node with:
- `data`
-  `prev` -> pointer to the previous node
- `next` -> pointer to the next node

This makes forward and backward traversal possible.

## Available Methods
  
| Method | Description |
| -------------- | -------------- |
| `append(data)` | Adds a new node at the end of the list |
| `prepend(data)` | Adds a new node at the beginning of the list |
| `deleteValue(data)` | Deletes the first node containing the given value |
| `displayList()` | Displays the list from head to tail |
| `displayreverse()` | Displays the list from tail to head |
| `search(data)` | Returns *True* if the value exists, otherwise *False* |

## Time Complexity
| Operation | Time Complexity |
|----------|------------------|
| Append | O(n) |
| Prepend | O(1) |
| Delete by Value | O(n) |
| Search | O(n) |
| Display Forward | O(n) |
| Display Reverse | O(n) |

## Example Usage
```
dll = doublyLinkedList()
dll.append(10)
dll.append(11)
dll.append(12)
dll.append(13)
dll.append(14)

dll.prepend(0)

dll.displayList()
dll.displayreverse()

print(dll.search(12))

dll.deleteValue(12)
dll.displayList()
```
**Output:**
0 <-> 10 <-> 11 <-> 12 <-> 13 <-> 14 <-> NULL

14 <-> 13 <-> 12 <-> 11 <-> 10 <-> 0 <-> NULL

**True**

0 <-> 10 <-> 11 <-> 13 <-> 14 <-> NULL

## Applications of Linked List
- Implementation of Data Structures
- Browser History
- Music Players and Playlist: Playing next or previous song
  

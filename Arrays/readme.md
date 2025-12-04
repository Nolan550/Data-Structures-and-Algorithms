# Linked Lists(Data Structures)
## Overview
A **Custom Array** is a user-defined implementation of an array data structure.
Unlike python's list, this array imitates the behavior of low-level arrays, including:

- Fixed capacity
- Manual index management
- Insertions and deletions
- Searching and traversal

## Key Features
| Feature | Description |
|---------|------------- |
| `insert(index, value)` | insert value at a position |
| `delete(index)` | Remove value at an index |
| `search(value)` | Find value and return index |
|`update(index, value)` | Change value at index|
| `display()` | Print array elements |


## How it works

- Uses a Python list internally, but capacity is manually controlled
- Index validation is implemented to simulate real arrays
- Error handling for overflowing and invalid indexes

## Project Structure
This folder contains CustomArray implementation done in **Java** and **Python** together with its **readme.md** file.

## Example Usage
```
python
arr = CustomArray(5)
arr.insert(0, 10)
arr.insert(1, 11)
arr.insert(2, 12)
arr.insert(3, 13)
arr.insert(4, 14)

arr.display()

```

## Sample Output
Array elements: [10, 11, 12, 13, 14]

## What is Expected to learn
- How arrays work internally
- Manual memeory-like capacity simulation
- Index-based insertion and deletion
- Error handling for overflow and bounds


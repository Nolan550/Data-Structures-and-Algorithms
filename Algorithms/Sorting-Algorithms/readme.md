# 📊 Sorting Algorithms

This folder contains implementations of fundamental **sorting algorithms** used in Data Structures and Algorithms (DSA). Sorting algorithms arrange data in a particular order (usually ascending or descending) and are essential for efficient searching, data analysis, and system optimization.

---

## 📚 Algorithms Included

### 1. Bubble Sort
- Repeatedly swaps adjacent elements if they are in the wrong order.
- Simple but inefficient for large datasets.

**Time Complexity**
- Best Case: `O(n)` (already sorted)
- Average Case: `O(n^2)`
- Worst Case: `O(n^2)`

---

### 2. Selection Sort
- Repeatedly selects the minimum element and places it in the correct position.
- Works well for small datasets, easy to understand.

**Time Complexity**
- Best, Average, Worst Case: `O(n^2)`

---

### 3. Insertion Sort
- Builds the sorted array one element at a time by inserting elements into their correct position.
- Efficient for nearly sorted datasets.

**Time Complexity**
- Best Case: `O(n)` (already sorted)
- Average Case: `O(n^2)`
- Worst Case: `O(n^2)`

---

### 4. Merge Sort
- Divides the array into halves, recursively sorts them, and merges the results.
- Stable and efficient for large datasets.

**Time Complexity**
- Best, Average, Worst Case: `O(n log n)`

---

### 5. Quick Sort
- Picks a pivot element and partitions the array around it.
- Efficient for most practical datasets but not stable.

**Time Complexity**
- Best, Average Case: `O(n log n)`
- Worst Case: `O(n^2)` (rare, depends on pivot selection)

---

### 6. Heap Sort
- Builds a heap and repeatedly extracts the maximum (or minimum) to sort the array.
- Not stable but efficient.

**Time Complexity**
- Best, Average, Worst Case: `O(n log n)`

---

## 🧠 When to Use Sorting Algorithms

Sorting is widely used in applications such as:

- Database management
- Search optimization
- Data analytics
- File systems
- Algorithm optimization (like searching and graph algorithms)

Selecting the appropriate algorithm depends on:
- Dataset size
- Memory constraints
- Need for stability
- Data distribution

---

## 📂 Folder Structure

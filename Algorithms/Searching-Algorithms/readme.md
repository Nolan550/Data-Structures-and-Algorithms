# 🔎 Searching Algorithms

This folder contains implementations of fundamental **searching algorithms** used in Data Structures and Algorithms. Searching algorithms are used to locate a specific element within a data structure such as an array, list, tree, or graph.

They are essential for optimizing performance in many computer science applications including databases, search engines, and artificial intelligence systems.


## 📚 Algorithms Included

### 1. Linear Search
Linear search checks each element in the list sequentially until the target element is found.

**Characteristics**
- Works on **unsorted data**
- Simple to implement

**Time Complexity**
- Best Case: `O(1)`
- Average Case: `O(n)`
- Worst Case: `O(n)`



### 2. Binary Search
Binary search repeatedly divides the search interval in half to locate the target element.

**Characteristics**
- Works only on **sorted data**
- Much faster than linear search for large datasets

**Time Complexity**
- Best Case: `O(1)`
- Average Case: `O(log n)`
- Worst Case: `O(log n)`



### 3. Jump Search
Jump search works by jumping ahead by fixed steps instead of checking each element sequentially.

**Characteristics**
- Requires a **sorted array**
- Faster than linear search for large datasets

**Time Complexity**
- Average Case: `O(√n)`



### 4. Interpolation Search
Interpolation search improves binary search by estimating the likely position of the target element.

**Characteristics**
- Works best with **uniformly distributed sorted data**

**Time Complexity**
- Best Case: `O(log log n)`
- Worst Case: `O(n)`


### 5. Exponential Search
Exponential search first finds a range where the element may exist and then applies binary search.

**Characteristics**
- Useful for **very large or unbounded arrays**

**Time Complexity**
- Average Case: `O(log n)`



## 🧠 When to Use Searching Algorithms

Searching algorithms are used in many real-world applications:

- Database systems
- Search engines
- Artificial intelligence
- File systems
- Data analysis tools

Choosing the correct searching algorithm depends on:
- Whether the data is **sorted or unsorted**
- The **size of the dataset**
- Performance requirements


## 📂 Folder Structure


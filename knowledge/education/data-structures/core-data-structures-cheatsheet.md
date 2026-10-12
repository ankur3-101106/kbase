---
title: Core Data Structures Complexity & Reference Cheatsheet
type: reference
area: education
topics:
  - data-structures
  - algorithms
  - exam-prep
status: evergreen
created: 2026-10-12
updated: 2026-10-12
---

# Core Data Structures Complexity & Reference Cheatsheet

## 1. Complexity Comparison Matrix

| Data Structure | Access (Avg / Worst) | Search (Avg / Worst) | Insertion (Avg / Worst) | Deletion (Avg / Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Array** | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Dynamic Array** | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)^*$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Singly Linked List** | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (head) | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (head) | $\mathcal{O}(n)$ |
| **Doubly Linked List** | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ | $\mathcal{O}(n)$ |
| **Stack (LIFO)** | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (push) | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (pop) | $\mathcal{O}(n)$ |
| **Queue (FIFO)** | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (enqueue) | $\mathcal{O}(1)$ / $\mathcal{O}(1)$ (dequeue) | $\mathcal{O}(n)$ |
| **Hash Table** | N/A | $\mathcal{O}(1)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(n)$ | $\mathcal{O}(1)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **Binary Search Tree** | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(n)$ |
| **AVL / Red-Black Tree** | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ | $\mathcal{O}(n)$ |
| **Binary Min/Max Heap** | N/A | $\mathcal{O}(n)$ / $\mathcal{O}(n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ / $\mathcal{O}(\log n)$ (extract) | $\mathcal{O}(n)$ |

*\* Denotes amortized time complexity.*

---

## 2. Memory Layout & Cache Locality

### Arrays vs. Linked Lists
- **Arrays:** Contiguous memory blocks. High CPU L1/L2 cache locality and automatic prefetching. Best for iteration and indexing.
- **Linked Lists:** Non-contiguous pointer nodes. High pointer overhead (8 bytes per pointer on 64-bit systems) and frequent cache misses. Prefer array-backed circular buffers or deques when possible.

### Tree Traversal Ordering
- **In-order (Left, Root, Right):** Produces keys in sorted ascending order for BSTs.
- **Pre-order (Root, Left, Right):** Used for cloning trees or serializing prefix expressions.
- **Post-order (Left, Right, Root):** Used for bottom-up cleanup (freeing nodes) and postfix calculation.

---

## 3. High-Yield Edge Cases & Traps
1. **Hash Table Worst-Case:** When poorly distributed hash functions or hash collisions cause all keys to fall into a single bucket, search degrades from $\mathcal{O}(1)$ to $\mathcal{O}(n)$ (or $\mathcal{O}(\log n)$ in Java 8+ HashMap red-black tree binning).
2. **Unbalanced BST:** Inserting sorted input (`[1, 2, 3, 4, 5]`) into an un-balanced BST degrades the tree into a linked list with $\mathcal{O}(n)$ height.
3. **Binary Heap Peek vs. Find:** Finding the minimum/maximum in a binary heap is $\mathcal{O}(1)$, but finding an arbitrary element requires $\mathcal{O}(n)$ linear search.

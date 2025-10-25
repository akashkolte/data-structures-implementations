# 🧠 Data Structures Implementation – Python

This repository contains **from-scratch implementations** of all major Data Structures in Python.  
Goal: Build deep understanding, not just API usage — to crush MAANG-level interviews 💪  

---

## 📘 Tier 1 – Core Data Structures

### 🧱 Arrays
-  Implement Dynamic Array (custom `list`):
  -  append, insert, delete, resize, get, set, length

### 🔗 Linked Lists
-  Singly Linked List:
  -  insert_at_head, insert_at_tail, delete, search, reverse
  -  detect_cycle (Floyd’s algorithm)
-  Doubly Linked List:
  -  insert_front, insert_end, delete_node, traverse_forward/backward

### 🥞 Stack
-  Stack using Array:
  -  push, pop, peek, is_empty
-  Stack using Linked List:
  -  push, pop, peek, is_empty
-  Application:
  -  Evaluate postfix expression

### 🧾 Queue
-  Queue using Array:
  -  enqueue, dequeue, is_empty
-  Circular Queue
-  Queue using Two Stacks

### 🧮 Hash Table (HashMap)
-  Hash Table using Separate Chaining:
  -  put, get, remove, contains
  -  handle collisions & rehashing (load factor > 0.7)

### ⛰️ Heap (Priority Queue)
-  Min Heap:
  -  insert, extract_min, heapify, decrease_key
-  Max Heap (bonus using negation)

### 🌲 Binary Search Tree (BST)
-  Insert, search, delete
-  Traversals: inorder, preorder, postorder
-  find_min, find_max
-  Validate BST

---

## ⚙️ Tier 2 – Advanced Structures

### 🌳 AVL Tree (Self-Balancing BST)
-  insert, delete
-  left_rotate, right_rotate, get_balance

### 🕸️ Graphs
-  Representations: adjacency list & matrix
-  DFS, BFS
-  Topological Sort
-  Dijkstra’s Shortest Path
-  Detect Cycle (directed & undirected)
-  Kruskal’s MST (use DSU)
-  Prim’s MST

### 🔤 Trie (Prefix Tree)
-  insert, search, starts_with, delete
-  autocomplete(prefix)

### 🔗 Disjoint Set Union (Union-Find)
-  find with path compression
-  union by rank
-  detect_cycle using DSU

### 📈 Segment Tree
-  build_tree (range sum)
-  query(l, r)
-  update(idx, val)

---

## 🚀 Tier 3 – Bonus / System Design Level

### ⚡ LRU Cache
-  Implement using Doubly Linked List + HashMap
-  get(key), put(key), display_cache()

### 🌸 Bloom Filter (optional)
-  Bit array, multiple hash functions
-  add(item), check(item)

### 🪜 Skip List
-  Random level generation
-  insert, search, delete

### 🔠 Suffix Trie / Array
-  Build suffix trie
-  Search for substring pattern

---

## 🧩 Extra Structures
-  MinStack (getMin in O(1))
-  Deque (double-ended queue)
-  Circular Buffer (fixed-size queue)

---

## 🎯 Goal
✔️ Understand internals of every DS  
✔️ Code each one from scratch  
✔️ Solve related problems afterward  
✔️ Document complexity & edge cases  

---

## 🏁 Progress Tracker
| Category | Status | Notes |
|-----------|---------|-------|
| Tier 1 (Core DS) | ⏳ In Progress | Foundational level |
| Tier 2 (Advanced) | ⏳ Pending | Focus after mastery |
| Tier 3 (Bonus) | 🔒 Optional | For system design depth |

---

## 💬 About
Built by **Akash Jagannath Kolte** – Software Engineer building intelligent systems 🚀  
*Learning by implementing every line of code, the hard way — the real way.*

---

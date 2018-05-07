# Basic Data-Structures Study

## Binary Heap, Fibonacci heaps
 1. Binomial Heap (To make Union efficient)
 2. Recursive, B_k has 2**k nodes, height k
 3. C(k, i) nodes at depth i
 4. Root has degree k (larger than any other nodes)
 5. Members: parent, key, degree, child, sibling
 6. Fibonacci Heaps
 7. Make-heap O(1) / O(1) / O(1)
 8. Insert, O(log n) / O(log n) / O(1)
 9. Minimum, O(1) / O(log n) / O(1)
 10. Extract-min, delete and return min O(log n) / O(log n) / O(log n)
 11. Union(H1, H2) O(n) / O(log n) / O(1)
 12. decrease key(H, x, k) O(log n) / O(log n) / O(1)
 13. delete O(log n) / O(log n) / O(log n)
 14. All Heaps are not designed for Search

## Data Structures for Disjoint sets
 1. (S1, S2, ...), each one with a representative
 2. Make-set
 3. Union(x, y)
 4. Find-Set(x)
 5. Linked-list, representative: first node
 6. Weighted Union: Always append shor to longer lists when union
 7. Disjoint-set forest:
 8. Heuristic 1: Union by rank (root with smaller rank points to root with larger rank)
 9. Heuristic 2: path compression

## Tree related
### BST:
  1. search: O(log(N)) just go left/right if larger/smaller
  2. insert: always at leaf
  3. delete:

### Red-Black Tree:
 1. Members: key(x), color(x), left(x), right(x), parent(x)
 2. Every node is either red or black.
 3. Every leaf (NIL) is black.
 4. If a node is red, then both its children are black.
 5. Every simple path from a node to a descendant leaf contains the same number of black nodes.
 6. Lemma 14.1 A red-black tree with n internal nodes has height at most 2*lg(n + 1).
```python
##  Left/right rotate
#    y         x
#  x   z <-> a   y
# a b           b z
##  Insert: insert a red node, then adjust until all properties are met
# case 1: property 3 violated (recolor)
# case 2: rotate left
# case 3: rotate right
# other structures: AVL tree, may require O(log n) rotations
# 2-3 Tree (Hopcroft)
# B-Tree
# i-th order statistics
# augment RB-tree with size(x)

# B-trees
# better at mimizing disk I/O operations
```
### Sement-Tree (store ops of an interval, really good problem 307, 308)
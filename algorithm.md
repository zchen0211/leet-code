# Summary of All different Algorithms

## Number Theory
- gcd (greatest common divider)
- The Chinese remainder theorem:
    - n = n1 * n2 * n3 * ... * nk
    - Given a, a1, a2, ..., ak, find a s.t. ai = a mod ni
    - let mi = n1 * n2* n_i-1 * n_i+1 * ... * nk
    - ci = mi(mi^-1 mod ni)
    - a = a1*c1 + a2*c2 + ... + ak*ck
- Power set
    - a ** phi(n) = 1 (mod n), phi(n) Euler-Phi function size of (Z*n)
    - when p is prime, a ** (p-1) = 1 (mod p)
- RSA public-key cryptosystem

## Graphs
- BFS
- DFS
- DAG, topologcial sort (DFS) b/c runtime
- MST (Minimum Spanning Tree)
- Kruskal: Add an edge to connect two disjoint trees
    - O(E log(E))
- Prim:
    - O(E logV) with Priority Queue implemented by Heap
- can be improved to O(E+ VlogV) by Fibonnaci Heap
- All-pairs shortest paths: the Floyd-Warshall Algorithm

## Sorting
- bubble, selection, insert
- Quick-sort, Merge-sort, Heap-sort
- Radix sort, bucket-sort,
- External sort

## Computational Geometry
- Cross Product: 
    - (x1, x2) and (y1, y2)
    - >0 if clockwise; <0 counter-clockwise
- To check if two line sgements p1->p2, p3->p4 intersect
    - intersect: (p3-p1)x(p2-p1), (p4-p1)x(p2-p1) different sign
    - do not intersect: (p3-p1)x(p2-p1), (p4-p1)x(p2-p1) same sign
- Convex Hull:
    - Graham's Scan: O(n*logn)
    - Jarvis' March
- Finding Closest Pair of Points
    - T(n) = 2 T(n/2) + O(n) if n > 3
    - T(n) = O(1) if n <= 3

## Stable Matching
- David Gale and Lloyd Shapley (G-S)
    - M={m1, ..., mn}, W={w1, ..., wn}

## Greedy

## Divide and Conquer

## Dynamic Programming

## Max-flow
- Constraint 1: 0 <= f(e) <= c(e)
- Constraint 2: 0 sum_into_v f(e) = sum_outof_v f(e)
- Ford-Fulkerson Algorithm
- Augment path in a residual graph, increase by bottleneck 
- Choosing Good Augmenting Paths: with bottleneck at least delta
- Preflow-push Algorithm

## NP-Complete

## Approximate Algorithms

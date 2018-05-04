## Geometry

## Convex Hull
- http://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
- Jarvis's Algorithm for Wrapping
```
 1) Initialize p as leftmost point.
 2) Do following while we don’t come back to the first (or leftmost) point.
   a) The next point q is the point such that the triplet (p, q, r) is counterclockwise for any other point r.
   b) next[p] = q (Store q as next of p in the output convex hull).
   c) p = q (Set p as q for next iteration).
 Time complexity: O(m * n)
   m: convex points
```

## Graham Scan
- http://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/
```
 Sort
 Go through from left to right
  reject by polar angle
 Time Complexity: O(nlogn)
```

## Line Intersection
- http://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
```
 (p1, q1), (p2, q2)
 Check if (p1, q1, p2) and (p1, q1, q2) have different orientations?
  Y: no intersection
  N: intersection
```

## Interview Tree
- http://www.geeksforgeeks.org/interval-tree/
- Idea: to augment a self-balancing Binary Search Tree (BST)
- Data Structure:
```
  TreeNode
    i (begin, end)
    max_

 Interval overlappingIntervalSearch(root, x)
  1) If x overlaps with root's interval, return the root's interval.
  2) If left child of root is not empty and the max  in left child is greater than x's low value, recur for left child
  3) Else recur for right child.
```

## Matrix Exponential
- http://www.geeksforgeeks.org/matrix-exponentiation/
```
 F(n) = a*F(n-1) + b*F(n-2) + c*F(n-3)   for n >= 3 
```

## Maxflow Ford Furkerson Algo and Edmond Karp Implementation
- http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
- Ford-Fulkerson Algorithm 
```
  1) Start with initial flow as 0.
  2) While there is a augmenting path from source to sink. 
           Add this path-flow to flow.
  3) Return flow.
```

## Min-cut
- http://www.geeksforgeeks.org/minimum-cut-in-a-directed-graph/

## Stable Marriage Problem
- http://www.geeksforgeeks.org/stable-marriage-problem/
```
Initialize all men and women to free
while there exist a free man m who still has a woman w to propose to 
{
    w = m's highest ranked such woman to whom he has not yet proposed
    if w is free
       (m, w) become engaged
    else some pair (m', w) already exists
       if w prefers m to m'
          (m, w) become engaged
           m' becomes free
       else
          (m', w) remain engaged    
}
```

## Hopcroft–Karp Algorithm for Maximum Matching
- http://www.geeksforgeeks.org/hopcroft-karp-algorithm-for-maximum-matching-set-1-introduction/
```
 Bipartite Graph: find max edge number without endpoint sharing
  1. Ford-Fulkerson: O(V * E)
  2. Hopcroft-Karp: O(sqrt(V) * E)
```

## Dinic’s algorithm for Maximum Flow
- http://www.geeksforgeeks.org/dinics-algorithm-maximum-flow/
```
 Edmond Karp Implementation: O(VE^2)
 Dinic's Implementation: O(EV^2)
 In Edmond’s Karp algorithm, we use BFS to find an augmenting path and send flow across this path.
 In Dinic’s algorithm, we use BFS to check if more flow is possible and to construct level graph. In level graph
```

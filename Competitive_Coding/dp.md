# Dynamic Programming

## Longest Common Subsequence
- http://www.geeksforgeeks.org/longest-common-subsequence/

## Longest Increasing Subsequence
- http://www.geeksforgeeks.org/longest-increasing-subsequence/

## Edit Distance
- http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
- insert
- remove
- replace

## Minimum Partition
- http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/

## Ways to cover a distance
- http://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/

## Longest path in a Matrix
- http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/

## Subset Sum
- http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/

## optimal strategy for a game
- http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/

## 0-1 Knapsack Problem
- http://www.geeksforgeeks.org/knapsack-problem/

## Assembly Line Scheduling
- http://www.geeksforgeeks.org/dynamic-programming-set-34-assembly-line-scheduling/

## Bellman-Ford Algorithm
- http://www.geeksforgeeks.org/dynamic-programming-set-23-bellman-ford-algorithm/
- A src to all vertices
    - Init dis as 0 for src and Infinity for others;
    - Do following for each edge u-v for |V-1| times:
    If dist[v] > dist[u] + weight of edge uv, then update dist[v]
      dist[v] = dist[u] + weight of edge uv
    - This step reports if there is a negative weight cycle in graph. 
    - Do following for each edge u-v
    -   If dist[v] > dist[u] + weight of edge uv, 
    -     then "Graph contains negative weight cycle"

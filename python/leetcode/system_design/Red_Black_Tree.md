# Red-Black Tree

## Java: TreeMap
```java
tree = new TreeMap<>();
```
- Add
```java
tree.put(val, new Interval(val, val));
```
- Remove
```java
tree.remove(v);
```
- Query O(log(n))
```java
tree.containKey(val)
```
- Delete O(log(n))
```java
tree.remove(h);
```
- Query lower-key O(log(n))
```java
Integer l = tree.lowerKey(val);
```
- Query higher-key O(log(n))
```java
Integer l = tree.higherKey(val);
```
- Typical problem: 352 (disjoint interval)
- Problem 128 (longest consecutive sequence)

## Java: TreeSet

## Java: HashMap

## C++: multiset
```cpp
multiset<int> window(nums.begin(), nums.begin()+k);
```
- **Multiple elements can have the same values**
- Query kth smallest;
```cpp
auto mid = next(window.begin(), k / 2);
```
- Insert:
```cpp
window.insert(nums[i]);
```
- Erase:
```cpp
window.erase(item);
```
- Lower bound (first <= item):
```cpp
window.lower_bound(item);
```
- Problem 480: Sliding Window median;

## Python: bisect
- Keep a list in sorted order:
```python
import bisect
kls = nums[:k]
kls.sort()
def update(num1, num2):
    # remove num1, add num2 to kls
    id1 = bisect.bisect_left(kls, num1)
    del kls[id1]
    bisect.insort(kls, num2)

    if k % 2 == 0:
        return sum(kls[k/2-1:k/2+1]) / 2.
    else:
        return float(kls[k/2])
```
- Query:
```python
bisect.bisect_left(array, x)
bisect.bisect_right(array, x)
bisect.bisect(array, x) # same as bisect_right
```
- Insert:
```python
bisect.insort_left(array, x)
bisect.insort_right(array, x)
bisect.insort(array, x)
```
- Problem 480: Sliding Window median;
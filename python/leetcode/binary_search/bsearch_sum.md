# Binary Search Summary

## Find index, otherwise -1
- problem 74, 704
```python
left, right = 0, n-1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target: return mid
    elif nums[mid] > target: right = mid - 1
    else: left = mid + 1
return -1
```
- problem 34, search target range
```python
i, j = 0, n-1
left, right = -1, -1
# search left
while i < j:
	mid = (i + j) // 2
    if A[mid] < target: i = mid + 1
    else: j = mid
if A[i] != target: return [left, right]
else: left = i
# search right
j = n-1
while i < j:
	mid = (i + j) // 2 + 1 # towards right?
	if A[mid] > target: j = mid - 1
    else: i = mid
right = j
return [left, right]
```

## Find item > than target
- 744
```python
# edge condition can't be handled
if target >= letters[-1]: return letters[0]
left, right = 0, n
while left < right:
    mid = (left + right) // 2
    if letters[mid] <= target: left = mid + 1
    else: right = mid
return letters[left]
```

## Search with function
- 275 (h-index)
```python
"""
find maximum ind in [0, n-1] s.t. A[ind] >= n-ind
"""
left, right = 0, n-1
while left <= right:
    mid = (left+right) // 2
    if A[ind] == n - ind: return A[ind]
    elif citations[mid] > (n-mid): right = mid - 1
    else: left = mid + 1
return n - right + 1
```
- 278 (find first bad, [true, true, ..., false])
```python
start = 1, n # included left, right
while start < end:
    mid = (end + start) // 2
    if not isBadVersion(mid): start = mid + 1
    else: end = mid            
return start
```
- 1014 (separate numbers with min-sum)
```python
"""
find minimum number x in [min_, max_], s.t. f(x) <= D
x smaller, f(x) larger
can query f(x)
"""
start_, end = max(weights), sum(weights)
while start_ < end_:
    mid = (start_ + end_) // 2
    # print(start_, end_, mid, helper(mid), D)
    if helper(mid) <= D: end_ = mid
    else: start_ = mid + 1
return start_
```

## More Fancy
- Rotated Array: 33, 81, 153, 154
- Find peak: 162
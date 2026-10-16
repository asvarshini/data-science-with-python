# LeetCode 349: Intersection of Two Arrays

## Problem
Given two integer arrays `nums1` and `nums2`, return an array containing their **unique common elements**. The order does not matter.

Example:
```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3]

Output: [2]
```

---

## Method 1: Nested Loops

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        result = []

        for i in nums1:
            for j in nums2:
                if i == j and i not in result:
                    result.append(i)

        return result
```

**Logic:** Compare every element in the first array with every element in the second array. Add common elements only once.

- Time: O(n × m) worst case
- Extra space: O(u), where u is the number of unique common elements
- Best for: Understanding nested loops and comparisons.

---

## Method 2: Sets and Intersection (Shortest)

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
```

**Logic:**
- `set()` removes duplicates.
- `&` finds common elements.
- `list()` converts the result back to a list.

- Average time: O(n + m)
- Extra space: O(n + m)
- Best for: Short, readable solutions.

---

## Method 3: One Set and One Result Set

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        s = set(nums1)
        result = set()

        for i in nums2:
            if i in s:
                result.add(i)

        return list(result)
```

**Logic:** Store the first array in a set, check whether each element of the second array exists in it, and collect matches without duplicates.

- Average time: O(n + m)
- Extra space: O(n + u)
- Best for: Learning set membership and duplicate removal.

---

## Method 4: Sort and Use Two Pointers

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result
```

**Logic:**
- Sort both arrays.
- If elements match, add the value once.
- If the first value is smaller, move pointer `i`.
- Otherwise, move pointer `j`.

- Time: O(n log n + m log m)
- Auxiliary space: O(1) for the pointer variables, excluding sorting implementation and output storage
- Best for: Learning two pointers and sorted-array techniques.

Note: This sorts the input arrays in place.

---

## Method 5: Built-in `intersection()`

```python
class Solution(object):
    def intersection(self, nums1, nums2):
        a = set(nums1)
        b = set(nums2)

        return list(a.intersection(b))
```

**Logic:** `intersection()` returns elements present in both sets.

- Average time: O(n + m)
- Extra space: O(n + m)
- Best for: Readable code using a built-in set method.

---

## Comparison

| Method | Time complexity | Extra space |
|---|---|---|
| Nested loops | O(n × m) worst case | O(u) with result membership checks |
| Set `&` | O(n + m) average | O(n + m) |
| One set + result set | O(n + m) average | O(n + u) |
| Sorting + two pointers | O(n log n + m log m) | Depends on sorting implementation |
| `intersection()` | O(n + m) average | O(n + m) |

Here, `n` and `m` are array lengths, and `u` is the number of unique common elements. Set complexities are average-case expectations.

---

## Final Recommendation

- **For the simplest solution:** Method 2.
- **For learning DSA:** Method 3.
- **For practicing two pointers:** Method 4.
- **For interviews:** Explain the set approach first, then discuss time and space trade-offs.

## Important Learning
A set stores unique elements, so duplicates are automatically removed. Set membership checks are O(1) on average, which makes this problem more efficient than comparing every pair with nested loops.

## [Problem](https://leetcode.com/problems/wiggle-subsequence/)

A **wiggle sequence** is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

- For example, `[1, 7, 4, 9, 2, 5]` is a **wiggle sequence** because the differences `(6, -3, 5, -7, 3)` alternate between positive and negative.
- In contrast, `[1, 4, 7, 2, 5]` and `[1, 7, 4, 5, 5]` are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.

A **subsequence** is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

*Given an integer array `nums`, return the length of the longest **wiggle subsequence** of `nums`.*

 

## Example 1



```
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

```


## Example 2


```
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).
```

## Logic
  - Runtime $\mathcal{O}(n\log_2{n})$ appraoch: sort the list, append alternatively to a list one from the start and one from the end. e.g.
      - [9, 8, 4, 1, 7, 6, 3, 5] -> [1, 3, 4, 5, 6, 7, 8, 9]
      - [1, 3, 4, 5, 6, 7, 8, 9] -> pick 1 and 9 -> [1,9] -> pick 3 an 8 ->[1,9,3,8] and repeat
  - Runtime $\mathcal{O}(n) approach$
## Solution
### Runtime: 

```python

```

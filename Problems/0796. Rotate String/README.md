## [Problem](https://leetcode.com/problems/rotate-string/)

Given two strings `s` and `goal`, return true `if and only if` `s` _can become_ `goal` after some number of **shifts** on s.

A **shift** on `s` consists of moving the leftmost character of s to the rightmost position.

- For example, if `s = "abcde"`, then it will be `"bcdea"` after one shift.

## Example 1

```
Input: s = "abcde", goal = "cdeab"
Output: true
```

## Example 2

```
Input: s = "abcde", goal = "abced"
Output: false

```

## Logic

### Approach 1: Brute Force

Check character each scenario by moving $i$ leftmost characters to the rightmost for $i\in |s|$.

Runtime = $\Theta(|s|^2)$ because it has a loop of string concatenation which the runtime for that is $O(n^2)$

```python
class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            if (s[i:] + s[:i]) == goal:
                return True
        return False
```

### Approach 2:

Check substring of `s+s`. If `goal` is in `s+s` then it means that it start somewhere `(s+s)[h:t]` for $h$ head index and $t$ tail index.

```
Example 1:
Input: s = "abcde", goal = "cdeab"
Then s+s = "abcde"+"abcde" = "abcdeabcde"
Output: true

```

### Approach 3: Rolling Hash

Create a hash function such that it will take each **positional character** and apply some math f(x) to it and sum up all the product of them and apply modulus.

$hash(Str) = (Str[0] P^0 + Str[1]P^1 + Str[2]P^2 + ... + Str[k]P^k)\pmod{ Q}$

(Underlying Logic Is Fairly complicated, uses finite field $\mathbb{F}_{MOD}$ and modular inverse)

## Solution

### Runtime:

Very possibly $\Theta(|s|^2)$, but very pythonic.

> ✅ Trading runtime for readability

```python

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        return goal in s+s and len(s)==len(goal)

```

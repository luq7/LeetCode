## [Problem](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, return _true_ if `t` is an anagram of `s`, and _false_ otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Example 1

```
Input: s = "anagram", t = "nagaram"
Output: true
```

## Example 2

```
Input: s = "rat", t = "car"
Output: false
```

## Logic

Initialize a dictionary based on alphabets as keys. And all values are 0. Loop through each character of `s` and add 1 to the occurance in the dictionary. Loop through each character of `t` and subtract 1 occurance from the dictionary.

## Solution

### Runtime:

$\Theta(3|s|)\Rightarrow\Theta(|s|)$

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        sums={element:0 for element in "abcdefghijklmnopqrstuvwxyz"}
        for i in range(len(s)):
            sums[s[i]]+=1
            sums[t[i]]-=1
        for key in sums:
            if sums[key]!=0:
                return False
        return True


```

## [Problem](https://leetcode.com/problems/two-sum/)
Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

## Example 1
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

## Example 2
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Diff. approach Logics
- Two Pass Hash Table: Runtime O(2n):
  1. Add each ele. from the list to the dict key=element,value=occurance
  2. Loop thru each ele. in the list. 
  3. Hash the difference of the TARGET - IthElement if exists then found. And if TARGET = IthElement + IthElement, check if it occured twice.

- One Pass Hash Table:
    1. Loop thru each ele. in the list: Runtime O(n)
    2. Hash the difference of the TARGET - IthElement. If it exits then we have found it, otherwise we keep looping until we find the other part that hashes into an existing value on the map.

## Solution: Two Pass Hash Table: Runtime O(2n)=> O(n)
```python3
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 2:
            return [0,1]
        else:
            hashyTable = {}
            for i in nums:
                hashyTable[i]=target - i
            for i in nums:
                if target-i in hashyTable:
                    if target-i==i:
                        if nums.count(i)>1:
                            return [nums.index(i),nums.index(i,nums.index(i)+1)]
                    else:
                        return [nums.index(target-i),nums.index(i)]
```

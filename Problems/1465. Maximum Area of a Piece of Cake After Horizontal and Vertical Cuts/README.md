## [Problem](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

You are given a rectangular cake of size $h\times w$ and two arrays of integers `horizontalCuts` and `verticalCuts` where:
- `horizontalCuts[i]` is the distance from the top of the rectangular cake to the `ith` horizontal cut and similarly, and
- `verticalCuts[j]` is the distance from the left of the rectangular cake to the `jth` vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays `horizontalCuts` and `verticalCuts`. Since the answer can be a large number, return this $\pmod{10^9 + 7}$.

## Example 1
![Example 1](https://github.com/luq7/LeetCode/blob/main/Problems/1465.%20Maximum%20Area%20of%20a%20Piece%20of%20Cake%20After%20Horizontal%20and%20Vertical%20Cuts/leetcode_max_area_2_example1.png)
```
Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. 
After you cut the cake, the green piece of cake has the maximum area.
```

## Example 2
![Example 2](https://github.com/luq7/LeetCode/blob/main/Problems/1465.%20Maximum%20Area%20of%20a%20Piece%20of%20Cake%20After%20Horizontal%20and%20Vertical%20Cuts/leetcode_max_area_3_example2.png)
```
Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. 
Red lines are the horizontal and vertical cuts. 
After you cut the cake, the green and yellow pieces of cake have the maximum area.
```

## Logic

- Find longest distance between 2 points for both vertical and horizontal cut. Then multiply them and mod it against the given number.
  - To guarantee that we can find the longest 2 points in either cut, we need to ensure that they are sorted. 


## Solution
### Rutime: $\Theta(nlog_2{n}) + \Theta(mlog_2{m}) + \Theta(1)\Rightarrow max\big(\mathcal{O}(nlog_2{n}),\mathcal{O}(mlog_2{m}))\big)$

```python
class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        # Sort the cuts to ensure a faster find, otherwise would require O(n^2)
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        maxHDist = 0
        maxVDist = 0
        
        # The distance between 0 to the first cut
        maxHDist = max(maxHDist,abs(0-horizontalCuts[0]))
        maxVDist = max(maxVDist,abs(0-verticalCuts[0]))
        
        # Loops to find the distances within each cut
        for i in range(1,len(horizontalCuts)):
            maxHDist = max(maxHDist, horizontalCuts[i]-horizontalCuts[i-1])
        
        for i in range(1,len(verticalCuts)):
            maxVDist = max(maxVDist,verticalCuts[i]-verticalCuts[i-1])
        
        # The distance between the last cut and the end of the cake
        maxHDist = max(maxHDist,h-horizontalCuts[-1])
        maxVDist = max(maxVDist,w-verticalCuts[-1])
        
        return (maxHDist * maxVDist) % (pow(10,9)+7)

```




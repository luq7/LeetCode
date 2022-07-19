## [Problem](https://leetcode.com/problems/pascals-triangle/)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![pascalTriangle](PascalTriangleAnimated2.gif)

## Example 1

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

## Example 2

```
Input: numRows = 1
Output: [[1]]

```

## Logic

Have an array that holds for the previous row, and an array for the current row. Always, initialize the current row with 1, then we start iterate from the second elements from the previous array. At each iteration we will add the current element and the previous element to the current array. And once we exit the array, we append the trailing 1 to the current array. Finally, add the current array into another list and repeat as many time as the numRows.

## Solution

### Runtime:

$n=\text{numRows}$
$\Theta(\underbrace{\frac{n(n+1)}{2}}_{Summation})\Rightarrow \Theta((n^2+n)/2)\Rightarrow \Theta(n^2)$

```python

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_of_rows = [[1]] # Base case
        pre_row = [1]
        for i in range(numRows-1): # Since we have a base case already
            cur_row=[1]
            for j in range(1,len(pre_row)):
                cur_row.append(pre_row[j] + pre_row[j-1])
            cur_row.append(1)
            pre_row=cur_row
            list_of_rows.append(cur_row)

        return list_of_rows

```

# Result

![Result](result.png)

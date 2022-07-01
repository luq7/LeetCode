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

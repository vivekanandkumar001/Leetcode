class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            else:
                prevMap[n]=i
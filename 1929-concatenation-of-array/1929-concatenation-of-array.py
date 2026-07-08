class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1=nums.copy()
        for i in nums1:
            nums.append(i)
        return nums
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        output = []
        for i in nums:
            counts = 0
            for j in nums:
                if i>j:
                    counts+=1
            output.append(counts)
        return output
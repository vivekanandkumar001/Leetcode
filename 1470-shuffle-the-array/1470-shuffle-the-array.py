class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        z = []
        x = nums[0:n]
        y = nums[n:]
        for i in range(n):
            z.append(x[i])
            z.append(y[i])
        return z
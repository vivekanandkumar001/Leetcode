class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num= nums1 + nums2
        num.sort()
        if ((len(num))%2==0):
            n = len(num)//2
            sum = (num[n-1]+num[n])/2.0
            return sum

        else:
            
            return float(num[len(num) // 2])
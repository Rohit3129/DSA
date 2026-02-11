class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=0:
            return 0
        l = 0
        res = 0
        prod = 1
        n = len(nums)
        for r in range(n):
            prod *=nums[r]
            while l<=r and prod >=k:
                prod = prod // nums[l]
                l +=1
            res += (r - l + 1)
        return res
            
        
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <=1:
            return 0
        if len(nums) == 0: return 0
        l = 0
        ans = 0
        pro = 1
        for r in range(len(nums)):
            pro *= nums[r]
            while pro >= k:
                pro //= nums[l]
                l +=1
            ans += r - l + 1
        return ans
       
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        r = 0
        ans = 0
        n = len(nums)
        while r < n:
            if nums[r] == 0:
                ans = max(ans, r - l)
                while r < n and nums[r] == 0:
                    r += 1
                l = r
            else:
                r += 1
        return max(ans, r - l)

        
        
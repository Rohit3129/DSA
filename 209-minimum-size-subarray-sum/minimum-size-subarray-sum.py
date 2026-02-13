class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                min_length = min(min_length, r-l+1)
                sum -= nums[l]
                l += 1
        return min_length if min_length < float("inf") else 0
            
        
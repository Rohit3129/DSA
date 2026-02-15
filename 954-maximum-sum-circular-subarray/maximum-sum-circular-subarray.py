class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globmax , globmin = nums[0], nums[0]
        currmax = 0
        currmin = 0
        total = 0
        for n in nums:
            currmax = max(currmax + n, n)
            currmin = min(currmin + n, n)
            total += n
            globmax = max(globmax, currmax)
            globmin = min(globmin, currmin)
        return max(globmax, total - globmin) if globmax > 0 else globmax
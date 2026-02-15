class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        currsum = 0
        for i in range(len(nums)):
            currsum += nums[i]
            maxsum = max(maxsum, currsum)
            if currsum < 0:
                currsum = 0
        
        return maxsum
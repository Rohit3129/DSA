class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first():
            ans=  -1
            l = 0
            h = len(nums)- 1
            while l <= h:
                m = (l + h) // 2
                if target == nums[m]:
                    ans = m
                    h = m - 1
                elif nums[m] < target:
                    l = m  + 1
                else:
                    h = m - 1
            return ans
        def last():
            ans = -1
            l = 0
            h = len(nums) - 1
            while l <= h:
                m = (l + h) // 2
                if target == nums[m]:
                    ans = m
                    l = m + 1
                elif nums[m] < target:
                    l = m  + 1
                else:
                    h = m - 1
            return ans
        return [first(), last()]
        
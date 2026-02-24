class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        max_count = -1
        ans = -1
        for key, value in counter.items():
            if value > max_count:
                max_count = value
                ans = key
        return ans

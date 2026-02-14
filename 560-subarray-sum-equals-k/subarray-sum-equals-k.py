class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = { 0:1}
        ps = 0
        rs = 0
        for i in nums:
            ps += i
            rs += dct.get(ps - k,0)
            dct[ps] = dct.get(ps, 0) + 1
        return rs
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def is_pali(s, l, r):
            count = 0
            while l >=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r +=1
            return count
        for i in range(len(s)):
            l = r = i
            res += is_pali(s, l, r)

            l = i
            r = i+1
            res += is_pali(s, l, r)
        return res


            
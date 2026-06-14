class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        RV = 0
        while x > RV:
            RV = RV * 10 + x % 10
            x //= 10
        return x == RV or x == RV // 10
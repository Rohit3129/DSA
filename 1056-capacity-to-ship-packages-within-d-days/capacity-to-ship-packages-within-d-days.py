class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def cantake(largest):
            sub_A = 1
            curr_sum = 0
            for w in weights:

                if curr_sum + w > largest:
                    curr_sum = w
                    sub_A += 1
                else:    
                    curr_sum += w
            return sub_A <= days
        l = max(weights)
        r = sum(weights)
        res = r
        while l <= r:
            c = (l + r) // 2
            if cantake(c):
                res = c
                r = c - 1
            else:
                l = c + 1
        return res
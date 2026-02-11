class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(i, j):
            if height[i] < height[j]:
                return height[i] * (j - i)
            else:
                return height[j] * (j - i)
        i = 0
        l = len(height)
        j = l-1
        result = 0
        maxheight = max(height)
        while i < j:
            result = max(area(i, j), result)
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
            if (j-i)*maxheight <result:
                return result
        return result
            

        
        
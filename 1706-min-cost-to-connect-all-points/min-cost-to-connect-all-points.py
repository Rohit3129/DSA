from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        msts = []
        for x,y in points:
            msts.append((float('inf'), x, y))
        msts[0] = (0, points[0][0], points[0][1])
        heapq.heapify(msts)
        cost = 0
        while len(msts) > 0:
            currwt, currx, curry = heapq.heappop(msts)
            cost += currwt
            for i in range(len(msts)):
                wt, x, y = msts[i]
                matn = abs(x - currx) + abs(y - curry)
                wt = min(wt, matn)
                msts[i] = (wt,x ,y)
            heapq.heapify(msts)
        return cost

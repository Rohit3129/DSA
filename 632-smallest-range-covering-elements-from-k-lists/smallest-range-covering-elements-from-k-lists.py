import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        curr_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            curr_max = max(curr_max, nums[i][0])
        result_r = [-10**5, 10**5]
        while min_heap:
            curr_min, list_id, el_id = heapq.heappop(min_heap)
            if curr_max - curr_min < result_r[1] - result_r[0]:
                result_r = [curr_min, curr_max]
            if el_id + 1 == len(nums[list_id]):
                break
            next_el = nums[list_id][el_id + 1]
            heapq.heappush(min_heap, (next_el, list_id, el_id + 1))
            curr_max = max(curr_max, next_el)
        return result_r

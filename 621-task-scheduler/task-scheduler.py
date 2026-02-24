class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        for i in tasks:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        lst = sorted(d.values(), reverse = True)
        max_num = lst[0]
        i = 0
        counter = 0

        while i < len(lst) and lst[i] == max_num:
            counter += 1
            i += 1
        ret = (max_num - 1) * (n + 1) + counter
        return max(ret, len(tasks))




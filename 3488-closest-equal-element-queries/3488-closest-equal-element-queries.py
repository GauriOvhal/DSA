import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = {}
        for i, num in enumerate(nums):
            pos.setdefault(num, []).append(i)

        res = []

        for q in queries:
            arr = pos[nums[q]]

            if len(arr) == 1:
                res.append(-1)
                continue

            i = bisect.bisect_left(arr, q)

            left = arr[i-1] if i > 0 else arr[-1]
            right = arr[i+1] if i < len(arr)-1 else arr[0]

            d1 = min(abs(q - left), n - abs(q - left))
            d2 = min(abs(q - right), n - abs(q - right))

            res.append(min(d1, d2))

        return res
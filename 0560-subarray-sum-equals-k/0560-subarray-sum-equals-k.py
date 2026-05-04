class Solution(object):
    def subarraySum(self, nums, k):
        current = 0
        count = 0

        prefix = {0: 1}

        for num in nums:
            current += num


            if current - k in prefix:
                count += prefix[current - k]

            prefix[current] = prefix.get(current , 0) + 1

        return count
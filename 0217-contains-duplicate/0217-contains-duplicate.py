class Solution(object):
    def containsDuplicate(self, nums):
        count = dict.fromkeys(nums , 0)

        for i in nums:
            count[i] += 1

        for c in count.values():
            if c >= 2:
                return True
                break
        return False     
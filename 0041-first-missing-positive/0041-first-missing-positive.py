class Solution(object):
    def firstMissingPositive(self, nums):

        visited = set(nums)

        i = 1

        while True:
            if i not in visited:
                return i
            
            i += 1
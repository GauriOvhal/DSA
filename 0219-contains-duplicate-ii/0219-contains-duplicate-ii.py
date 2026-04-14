class Solution(object):
    def containsNearbyDuplicate(self, nums, k):

        visited = {}

        for i in range(len(nums)):
            if nums[i] in visited:
                if i - visited[nums[i]] <= k:
                    return True

            visited[nums[i]] = i
        return False 
        
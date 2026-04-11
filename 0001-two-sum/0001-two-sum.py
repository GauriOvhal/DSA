class Solution(object):
    def twoSum(self, nums, target):
        
        n = len(nums)

        visited = {}

        for i in range(n):
            x = target - nums[i]

            if x in visited:
                return [visited[x] , i]
            
            visited[nums[i]] = i
        
class Solution(object):
    def productExceptSelf(self, nums):
        
        n = len(nums)

        answer = [0] * n

        answer[0] = 1
        
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        j = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * j
            j = j * nums[i]

        return answer
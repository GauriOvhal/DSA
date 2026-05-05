class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        hm = {0 : -1}

        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

            remainder = sum % k

            if remainder in hm:
                if i - hm[remainder] >= 2:
                    return True
            else:
                    hm[remainder] = i
        
        return False

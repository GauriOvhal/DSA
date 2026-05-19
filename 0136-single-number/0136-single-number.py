class Solution(object):
    def singleNumber(self, nums):
        
        otp = 0

        for num in nums:
            otp ^= num

        return otp
        
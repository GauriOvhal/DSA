class Solution(object):
    def minElement(self, nums):
        
        sum_list = []

        for n in nums:
            digit_sum = sum(int(digit) for digit in str(n))

            sum_list.append(digit_sum)

        return min(sum_list)
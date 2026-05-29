class Solution(object):
    def getLucky(self, s, k):

        num_string = ""
        for ch in s:
            num_string  += str(ord(ch) - ord('a') + 1)

        for i in range(k):
            num_sum = 0

            for ch in num_string:
                num_sum += int(ch)

            num_string = str(num_sum)
        
        return int(num_string)
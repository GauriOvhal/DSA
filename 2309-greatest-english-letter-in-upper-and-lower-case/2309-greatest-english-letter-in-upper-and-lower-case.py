class Solution(object):
    def greatestLetter(self, s):
       
        ch_set = set(s)

        for ch in range(ord('Z') , ord('A') -1 , -1):
            upper = chr(ch)
            lower = chr(ch).lower()

            if upper in ch_set and lower in ch_set:
                return upper

        return ""
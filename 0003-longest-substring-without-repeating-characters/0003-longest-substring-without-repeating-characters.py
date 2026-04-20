class Solution(object):
    def lengthOfLongestSubstring(self, s):

        char_map = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            
            char_map[s[end]] = end
        
            current_window_size = end - start + 1
            max_length = max(max_length, current_window_size)
            
        return max_length
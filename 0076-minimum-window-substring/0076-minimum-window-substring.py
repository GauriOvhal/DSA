class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        window = {}
        have = 0
        need = len(count_t)

        left = 0
        res = ""
        res_len = float('inf')

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = s[left:right+1]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1

                left += 1
        
        return res
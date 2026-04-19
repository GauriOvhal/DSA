class Solution(object):
    def isAnagram(self, s, t):

        s1 = s.replace(" ", "")
        t1 = t.replace(" ", "")

        if len(s1) != len(t1):
            return False
        
        c1 = {}
        for ch in s1:
            if ch in c1:
                c1[ch] += 1
            else:
                c1[ch] = 1
        
            
        for ch in t1:
            if ch not in c1:
                return False
            if ch in c1:
                c1[ch] -= 1
            else:
                c1[ch] = 1
        
        result = all(v == 0 for v in c1.values())
        return result
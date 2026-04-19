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
        
        c2 = {}
        for ch2 in t1:
            if ch2 in c2:
                c2[ch2] += 1
            else:
                c2[ch2] = 1
        
        if c1 == c2:
            return True
        else:
            return False
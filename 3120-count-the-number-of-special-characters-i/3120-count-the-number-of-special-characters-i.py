class Solution(object):
    def numberOfSpecialChars(self, word):
        
        small = set()
        capital = set()

        for ch in word:
            if ch >= 'a' and ch <= 'z':
                small.add(ch)
            else:
                capital.add(ch)

        count = 0
        for ch in small:
            if ch.upper() in capital:
                count += 1
                

        return count
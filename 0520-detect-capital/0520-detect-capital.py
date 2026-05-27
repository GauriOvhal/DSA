class Solution(object):
    def detectCapitalUse(self, word):
        
        if word.isupper() or word.islower():
            return True

        elif word.istitle():
            return True
        
        else:
            return False
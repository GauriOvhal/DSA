class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        
        for n in arr1:
            while n > 0:
                prefix_set.add(n)
                n //= 10

        res = 0
        
        for n in arr2:
            while n > 0 and n not in prefix_set:
                n //= 10
            
            if n > 0:
                res = max(res, len(str(n)))

        return res
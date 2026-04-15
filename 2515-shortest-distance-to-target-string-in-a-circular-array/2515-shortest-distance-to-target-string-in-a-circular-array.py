class Solution(object):
    def closestTarget(self, words, target, startIndex):
        n = len(words)

        min_dist = float('inf')

        for i in range(n):
            if words[i] == target:
                d = abs(i - startIndex)
                distance = min( d , n-d)
                
                min_dist = min(min_dist , distance)

        
        return min_dist if min_dist != float('inf') else -1
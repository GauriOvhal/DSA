class Solution(object):
    def findThePrefixCommonArray(self, A, B):

        n = len(A)

        C =[]
        visited = set()

        common_count = 0
    
        for i in range(n):
            if A[i] in visited:
                common_count += 1
            else:
                visited.add(A[i])
                
            if B[i] in visited:
                common_count += 1
            else:
                visited.add(B[i])
                
            C.append(common_count)
            
        return C
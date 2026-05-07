class Solution(object):
    def groupAnagrams(self, strs):

        clc = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in clc:
                clc[key] = []

            clc[key].append(word)

        return list(clc.values())
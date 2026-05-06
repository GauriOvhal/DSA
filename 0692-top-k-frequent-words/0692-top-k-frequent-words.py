class Solution(object):
    def topKFrequent(self, words, k):

        count = {}

        for word in words:
            count[word] = count.get(word , 0) + 1


        arr = list(count.keys())

        arr.sort(key=lambda word: (-count[word], word))

        return arr[:k]
    
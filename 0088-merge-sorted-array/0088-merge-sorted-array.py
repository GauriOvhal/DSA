class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = nums1[:m] + nums2

        temp.sort()

        for i in range(len(temp)):
            nums1[i] = temp[i]
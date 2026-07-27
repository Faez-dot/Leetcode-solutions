class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1+nums2
        combined.sort()

        total_len = len(combined)
        mid = total_len//2

        if total_len % 2 != 0:
            return float(combined[mid])
        else:
            return (combined[mid-1] + combined[mid]) / 2.0
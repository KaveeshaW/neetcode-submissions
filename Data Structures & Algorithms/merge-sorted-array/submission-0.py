class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = m
        end = m + n
        i = 0
        print(nums1)
        print(nums2)
        print(start)
        print(end)
        while start < end:
            nums1[start] = nums2[i]
            start += 1
            i += 1
        nums1.sort()
        
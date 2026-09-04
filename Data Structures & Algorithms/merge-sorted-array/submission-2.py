class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 index
        idx = 0

        # copy index
        i = 0

        # nums2 index
        j = 0

        copy = nums1[:m]
        while idx < n + m:
            # use the value from nums1 if
            # 1) j is equal or greater than the number of elements in nums2
            # 2) i is within the range of valid numbers and copy[i] < nums2[j]
            if j >= n or (i < m and copy[i] <= nums2[j]):
                nums1[idx] = copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            idx += 1
        
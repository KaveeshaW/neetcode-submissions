class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # start from the end
        last = m + n - 1

        # compare the values and add to the end of the array
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
        
        # since we are comparing m > 0 first, if that is false, make sure there are no values for nums2

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        
        
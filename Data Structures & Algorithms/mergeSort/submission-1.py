# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # empty array - nothing to sort so return
        if not pairs:
            return pairs
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        
    def mergeSortHelper(self, pairs, s, e):
        # is there only one element
        if e - s + 1 == 1:
            return pairs
        
        # find the middle
        m = (e + s) // 2

        #'sort' the left and right
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        # merge the values together
        self.merge(pairs, s, m, e)
        return pairs


    def merge(self, pairs, s, m, e):
        #set up the left and right array
        L = pairs[s: m+1]
        R = pairs[m+1: e+1]

        # set up the pointers to go through the lists
        i = 0
        j = 0
        k = s # starting point may not be at 0

        # merge the values in
        while i < len(L) and j < len(R):
            # put the L value in the array, achieving stable sorting
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # merge in the other values
        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1
        





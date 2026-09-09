class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binarySearch(row, target) == True:
                return True
        return False
    
    def binarySearch(self, row: List[int], target: int) -> bool:
        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2
            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True
        return False
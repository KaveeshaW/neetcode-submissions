class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        # search the first column to see if a row might have the number
        while top <= bottom:
            row = (top + bottom) // 2
            print(f"top{top}, col{bottom}, {row}")
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                # row has the element in the range potentially
                break
        
        # a row that has the value does not exist
        if top > bottom:
            return False
        
        row = (top + bottom) // 2
        l, r = 0, len(matrix[row])

        # check the row if it has the number
        while l <= r:
            m = (l + r) // 2
            if target < matrix[row][m]:
                r = m - 1
            elif target > matrix[row][m]:
                l = m + 1
            else:
                return True
        return False
        
    
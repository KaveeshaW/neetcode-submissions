class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue

                if(val in row_set[row] or
                   val in col_set[col] or
                   val in square_set[(row // 3, col // 3)]):
                    return False
                
                row_set[row].add(val)
                col_set[col].add(val)
                square_set[(row // 3, col // 3)].add(val)


        return True
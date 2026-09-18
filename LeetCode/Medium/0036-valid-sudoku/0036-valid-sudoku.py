class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.is_valid_unit(row):
                return False
        for col in range(0,9,):
            column = [board[row][col] for row in range (9)]
            if not self.is_valid_unit(column):
                return False
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range (box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        box.append(board [i][j])
                if not self.is_valid_unit(box):
                    return False
        return True
    
    def is_valid_unit(self, unit):
        seen = set()
        for cell in unit:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
        return True
            
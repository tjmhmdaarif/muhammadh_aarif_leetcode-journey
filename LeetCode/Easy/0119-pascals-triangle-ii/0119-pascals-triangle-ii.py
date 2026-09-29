class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = [1]
        for j in range (1,rowIndex + 1): 
            prev_row = result
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])
            new_row.append(1)
            result = new_row
        return result
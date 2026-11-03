class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Number of ')' needed to balance open '('
        
        for char in s:
            if char == '(':
                # If we have an odd number of ')' needed, complete the pair 
                # by inserting a single ')' before opening a new '('
                if open_needed % 2 != 0:
                    insertions += 1
                    open_needed -= 1
                open_needed += 2
            else:  # char == ')'
                open_needed -= 1
                # If we encounter a ')' without a matching '(', insert '(' before it
                if open_needed < 0:
                    insertions += 1  # Insert '('
                    open_needed += 2 # A '(' expects 2 ')', minus 1 seen -> 1 needed
                    
        return insertions + open_needed
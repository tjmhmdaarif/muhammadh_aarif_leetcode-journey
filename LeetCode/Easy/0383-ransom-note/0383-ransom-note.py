class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letter_count = {}
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        for letter in ransomNote:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            letter_count[letter] -= 1
        return True
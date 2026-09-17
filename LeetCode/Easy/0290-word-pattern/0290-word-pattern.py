class Solution:
    def wordPattern(self, pattern: str, words: str) -> bool:
        word_list = words.split()

        if len(pattern) != len(word_list):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for char, word in zip(pattern, word_list):
            if char in pattern_to_word:
                if pattern_to_word[char] != word:
                    return False
            else:
                pattern_to_word[char] = word

            if word in word_to_pattern:
                if word_to_pattern[word] != char:
                    return False
            else:
                word_to_pattern[word] = char
        return True
        
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_map = {}

        for letter in s:
            if letter in letters_map:
                letters_map[letter] += 1
            else:
                letters_map[letter] = 1

        for letter in t:
            if letter not in letters_map or letters_map[letter] == 0:
                return False
            letters_map[letter] -= 1

        return True
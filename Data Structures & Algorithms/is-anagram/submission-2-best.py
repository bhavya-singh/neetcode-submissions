class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_map = {}

        for letter in s:
            letters_map[letter] = 1 + letters_map.get(letter, 0)

        for letter in t:
            if letter not in letters_map or letters_map[letter] == 0:
                return False
            letters_map[letter] -= 1

        return True

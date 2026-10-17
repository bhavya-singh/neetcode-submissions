class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strings = [(s, {}), (t, {})]

        for index, string in enumerate(strings):
            for letter in string[0]:
                if letter in strings[index][1]:
                    strings[index][1][letter] += 1
                else:
                    strings[index][1][letter] = 1

        return strings[0][1] == strings[1][1]
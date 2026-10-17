class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mapS = {}

        for char in s:
            mapS[char] = 1 + mapS.get(char, 0)
        
        for char in t:
            if char not in mapS or mapS.get(char, 0) == 0:
                return False
            mapS[char] -= 1
        
        return True
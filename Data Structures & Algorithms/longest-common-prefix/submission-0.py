class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)
        max_pre = ""
        for pos in range(min_len):
            char = strs[0][pos]
            for string in strs:
                if string[pos] != char:
                    return max_pre
            max_pre += char
        return max_pre
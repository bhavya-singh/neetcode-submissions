class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store the map of key:value pairs where key will be tuple of freq and value will be the list of strings that have that alphabet frequency
        alphabets_map = {}

        
        # go through each string
        for string in strs:
            # initiate the freq counting array
            freq_array = [0]*26
            # go through every char and add 1 to the freq_array for that char
            for char in string:
                # increment the count at the char position in freq_array
                freq_array[ord(char) - ord('a')] += 1
                
            # now the freq_array for current string is ready, conv to tuple
            key = tuple(freq_array)

            # if it doesn't already exist, we initiate it
            if key not in alphabets_map:
                alphabets_map[key] = []

            # add string to the map
            alphabets_map[key].append(string)

        return list(alphabets_map.values())
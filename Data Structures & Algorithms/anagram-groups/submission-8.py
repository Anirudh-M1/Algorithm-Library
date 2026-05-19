from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = defaultdict(list)
        for string in strs: 
            charCounts = [0]*26
            
            for char in string:
                charCounts[ord(char)-ord("a")] += 1 

            groupedAnagrams[tuple(charCounts)].append(string)

        return list(groupedAnagrams.values())
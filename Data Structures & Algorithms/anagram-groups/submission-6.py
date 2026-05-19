class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = {}
        for string in strs: 
            charCounts = [0]*26
            tupCounts = tuple([""])
            for char in string:
                charCounts[ord(char)-ord("a")] += 1 
                tupCounts = tuple(charCounts)
                
            if tupCounts in groupedAnagrams: 
                groupedAnagrams[tupCounts].append(string)
            else:
                groupedAnagrams[tupCounts] = [string]
            
        return list(groupedAnagrams.values())
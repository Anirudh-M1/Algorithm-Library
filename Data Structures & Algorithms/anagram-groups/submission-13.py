class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs: 
            stringProfile = 26 * [0]
            for char in s:
                stringProfile[ord(char) - ord("a")] += 1 
            
            key = tuple(stringProfile)

            anagrams[key].append(s)

        return list(anagrams.values())
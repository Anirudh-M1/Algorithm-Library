class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            profile = [0] * 26
            
            for c in word:
                profile[ord(c) - ord("a")] += 1
            
            anagrams[tuple(profile)].append(word)

        return list(anagrams.values()) 
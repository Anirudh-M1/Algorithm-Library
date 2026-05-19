class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        words = defaultdict(list)
        for s in strs:
            key = "".join(sorted(list(s)))
            words[key].append(s)

        print(words)
        return list(words.values()) 
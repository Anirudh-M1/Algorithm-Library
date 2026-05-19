class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end = 0
        chars = Counter(s)

        seenChars = defaultdict(int)
        ans = []
        size = 0
        for c in s:
            seenChars[c] +=1

            if seenChars[c] == chars[c]: 
                del seenChars[c]
            size += 1 
            if not seenChars:
                ans.append(size)
                size = 0

        
        return ans
            



        
            
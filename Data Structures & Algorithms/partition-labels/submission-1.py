class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charFreq = Counter(s)
        charSeenFreq = {}
        count = 0
        ans = []
        for char in s: 
            count +=1 
            charSeenFreq[char] = charSeenFreq.get(char, 0) + 1 

            if charSeenFreq[char] == charFreq[char]: 
                del charSeenFreq[char]


            if not charSeenFreq:
                ans.append(count)
                count = 0
        
        return ans
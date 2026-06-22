class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0
        
        neighbors = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "#" + word[j+1:]
                neighbors[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        
        
        count  = 0
        
        while queue:
            count+=1
            for _ in range(len(queue)): 
                w = queue.popleft() 
                if w == endWord:
                    return count 
                for j in range(len(w)): 
                    curPattern  = w[:j] + "#" + w[j+1:]
                    for nei in neighbors[curPattern]: 
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

        return 0
    

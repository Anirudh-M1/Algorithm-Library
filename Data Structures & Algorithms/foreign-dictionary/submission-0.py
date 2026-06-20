class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for word in words: 
            for c in word:
                adj[c] = []
        print(adj)
        for i in range(len(words) - 1): 
            cur, nxt = words[i], words[i + 1]

            minlen = min(len(cur), len(nxt))
            if len(cur) > len(nxt) and cur[:minlen] == nxt[:minlen]:
                return ""
            for c in range(minlen): 
                if cur[c] != nxt[c]: 
                    adj[cur[c]].append(nxt[c])
                    break
        
        visited = {} # 1 for visiting, 2 for done
        ans = []

        def dfs(c):
            if c in visited: 
                if visited[c] == 1:  
                    #cycle
                    return False
                else:
                    return True
            
            visited[c] = 1

            for nei in adj[c]:
                if not dfs(nei):
                    return False

            visited[c] = 2  
            ans.append(c)
            return True

        for c in adj:
            if not dfs(c):
                print("failed")
                return ""

        return "".join(ans[::-1])





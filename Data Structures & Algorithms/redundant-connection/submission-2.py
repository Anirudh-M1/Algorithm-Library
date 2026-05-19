class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        sets = []
        
        parrent = [i for i in range(len(edges) + 1) ]
        rank = [1] * (len(edges) + 1)

        def find(n): 
            p = parrent[n]
            while p != parrent[p]:
                parrent[p] = parrent[parrent[p]]
                p = parrent[p]
            return p

        def union(n1, n2): 
            p1, p2 = find(n1) , find(n2)

            if p1 == p2: 
                return False
            if rank[p1] > rank[p2]: 
                rank[p1]+=1
                parrent[p2] = p1
            else: 
                rank[p2]+=1
                parrent[p1] = p2
            return True
        
        for n1, n2 in edges: 
            if union(n1,n2) == False: 
                return [n1, n2]

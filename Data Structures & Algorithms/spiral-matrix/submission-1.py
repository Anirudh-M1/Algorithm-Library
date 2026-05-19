class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])

        directions = [(0,1), (1,0), (0, -1), (-1,0)]
        curDir = 0
        i, j = 0, 0
        ans = []
        while len(visited) != rows*cols:

            dirTup = directions[curDir%4]
            print(f"---curDir = {dirTup},idx = {curDir} ----")
            print(f"i = {i},j = {j}")
            print(ans)
            print(visited)
            if (i, j) not in visited:
                ans.append(matrix[i][j])
                visited.add((i,j))
            if  0 <= i + dirTup[0] < rows  and  0 <= j + dirTup[1] < cols and (i + dirTup[0] ,j+dirTup[1]) not in visited:
                i += dirTup[0]
                j += dirTup[1]
            else:
                print("incremmented dir")
                curDir+=1

        return (ans)


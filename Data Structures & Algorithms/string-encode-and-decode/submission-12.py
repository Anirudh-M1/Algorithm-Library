class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs: 
            arr.append(str(len(s)) + "#")
            arr.append(s)
        
        string = "".join(arr)
        return string
    def decode(self, s: str) -> List[str]:
        start = 0
        ans = []
        i = 0
        print(len(s))
        print(s)
        while len(s)!= 0:
            i = 0
            while s[i] != "#": 
                i +=1 
            endStr = int(s[0: i])
            i += 1
            ans.append(s[i:endStr+i])
            s = s[endStr+i:len(s)]
        
        return [""] if ans == None else ans